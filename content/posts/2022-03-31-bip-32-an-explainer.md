---
title: "BIP-32, an explainer"
date: 2022-03-31
slug: "bip-32-an-explainer"
source: https://tejaswin.com/2022/03/31/bip-32-an-explainer/
categories:
  - "bitcoin"
  - "crypto tricks"
  - "cryptography"
---

[BIP-32](<https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>) is a Bitcoin Improvement Proposal that allows Alice to start with a single private key, and generate a series of private and public keys from it, where the public keys can be generated independently from the private keys. This is not as easy as it sounds, because in most public key crypto-systems, you can generate a public key only if you have the private key in hand. BIP-32 uses a nifty little crypto-trick to generate public keys without having access to their corresponding private keys, and the trick is rather simple, once you know it.

### Warm Up

Let’s first start with a string “test” and build a chain of hashes from it. We hash “test” with the SHA256 algorithm and take the first 10 characters to get the word ” 9f86d0818″. We can keep repeating this step to get a chain of hashes: test->9f86d0818->1eb9527d0->4ac094e29->76dded382 and on. This “hash-chain” can be remembered by just remembering the word “test” and the algorithm we use to build the chain. As in, if we have the first word “test”, we can generate the rest of the words in the chain with little effort.

Let’s say we want to generate a series of private and public keys with the same “chain” relationship. As in, after we create the first key pair using true randomness, we create the rest of the chain using the previous keypair and a deterministic algorithm. If we have this feature, we can use a new keypair every time we want to receive Bitcoin. And more importantly, we don’t have to store all the private keys safely. We just have to store the first key. We can later recreate the rest of the keys using this first key. To spend any of the Bitcoin received by any public key in the “key-chain”, we have to generate the key-pairs again from scratch till we find the key-pair that was the recipient of the payment, and use that private key to spend the received money. 

This part is clear – what is not clear is how the algebraic relationship between the private key and the public key is maintained during this “chaining” process. 

### How are private and public keys connected?

First, a quick background on private and public keys. In most public key crypto-systems, we generate a private key using some randomness. We then use a deterministic algebraic formula to calculate the public key. For example, in the Diffie Hellman public key system, we have a fixed, well known, agreed-upon prime modulus and a generator, say p = 733 and g = 5. These are known to all users in the system and are considered system-wide constants. During our individual workflow, we pick a random private key, priv = 101 and then we calculate the public key pub = g^{priv}\mod p. Substituting g=5, priv=101, and p=733, we get the public key pub = 176. The cryptographic assumption is that given 176, it’s not possible to find 101. Similar steps are followed in most public key cryptosystems like RSA, ElGamal, Pallier, BLS, etc. 

Coming back to chaining, we now start with the private key 101, and hash it with SHA256 and take modulo 733 to get the next private key, and so forth to get the key chain – 101->9->191->263->170->381->so on. These correspond to the public keys: 176, 413, 131, 366, 400, 207, and so on. These were calculated using the same formula pub = g^{priv}\mod p. The actual private/public key pairs are (101, 176), (9, 413), (191, 131), (263, 366), (170, 400), (381, 207) and so on. The important thing here is that the private keys are chained, but the public keys are not. The public keys are dependent on the private keys, and given just the first public key (176), you cannot calculate the next public key (413) without knowing its corresponding private key (9). The chaining works, but only for private keys. If Alice wanted to give the first public key to Bob and ask him to generate the rest of the public keys using a deterministic algorithm, Bob would not be able to do it. The hashing that chained the private keys is fundamentally incompatible with the algebraic relationship between the private and public keys. Hashing is not an algebraic operation, so to speak. We need to find a way to chain private keys that works well with the algebraic formula that ties private and public keys. 

### Simplified BIP32

BIP32 uses a clever mathematical trick to chain private keys in such a way that the public keys can also be chained, and we get to maintain the 1:1 non-invertible correspondence between the i^{th} private key and the i^{th} public key of their chains. The algebraic trick is as old as algebra itself: The Product of Powers Property states that when multiplying two exponents with the same base, you can add the exponents and keep the base. That is if a^b = c, then a^{b+x} = c \times a^x. 

We saw earlier that the private key goes into the exponent part of the algebraic formula that calculates the public key. If we add something (say, x) to the private key to get a new private key, the corresponding new public key can be derived by multiplying the old public key with g^x. Both the private key chain generator and public key chain generator can agree on a standard way to derive x for each step. In my simplified version of BIP32, we use the hash of the public key (which both chain generators know) as the x that we add in each step on the private key chain. On the public key chain, we don’t add hash(prev\\_pub\\_key) – but instead we multiply the previous public key with g^{hash(prev\\_pub\\_key)} to get the new public key. The following Python Code should make it clear. 
    
    
    import hashlib
    
    P = 733
    G = 5
    
    def hash_and_mod_p(x):
      return int(hashlib.sha256(str(x).encode('utf-8')).hexdigest(), base=16) % P
    
    alice_priv = 101
    alice_pub = bob_pub = pow(G, alice_priv, P)
    
    # Private Key Chain, run by Alice
    for i in range(10):
      print(alice_priv, alice_pub)
      shared_randomness = hash_and_mod_p(alice_pub)
      alice_priv = (alice_priv + shared_randomness) % (P-1)
      alice_pub =  pow(G, alice_priv, P)
    print('-' * 10)
    
    # Public Key Chain, run by Bob
    for i in range(10):
      bob_priv = 'xxx'
      print(bob_priv, bob_pub)
      shared_randomness = hash_and_mod_p(bob_pub)
      bob_pub = (bob_pub * pow(G, shared_randomness, P)) % P
    print('-' * 10)

The two loops are run by Alice and Bob separately. Alice starts with a private key, and she shares the corresponding public key with Bob. From then on, Alice and Bob can generate their respective chains without Bob ever knowing the private keys to the public keys that he is generating. Alice doesn’t even have to build her chain up front. She can just store her first private key in a vault, and Bob can send her as many payments as he wants, each to a different Bitcoin address. The randomness that we “infuse” into the key-chain is shared between Alice and Bob, but a third party Carol cannot detect that the keys in the key chain are related to each other. In Carol’s eyes the keys look entirely random. 

The actual BIP32 is a bit more complex – as it allows for independent trees of key-chains, and the randomness function is a a lot more complex. But the main principle is about just using the Product of Powers property.
