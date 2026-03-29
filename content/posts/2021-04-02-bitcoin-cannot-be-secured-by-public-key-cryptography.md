---
title: "Bitcoin cannot be secured by public-key cryptography"
date: 2021-04-02
slug: "bitcoin-cannot-be-secured-by-public-key-cryptography"
source: https://tejaswin.com/2021/04/02/bitcoin-cannot-be-secured-by-public-key-cryptography/
categories:
  - "bitcoin"
---

Bloomberg columnist Noah Smith wrote an article[1]Bloomberg [paywall link](<https://www.bloomberg.com/opinion/articles/2021-03-24/bitcoin-miners-are-on-a-path-to-self-destruction>). about Bitcoin’s energy consumption. “Blogger” Nic Carter wrote a [rebuttal](<https://medium.com/@nic__carter/noahbjectivity-on-bitcoin-mining-2052226310cb>) to it. Noah Smith wrote a [rebuttal](<https://noahpinion.substack.com/p/bitcoin-mining-and-resource-use>) to this rebuttal. Noah’s counter-rebuttal calls for its own rebuttal. 

Eventually, we will see why the following tweet from Nic follows quite naturally.

> “Proof-of-stake is just a fancy name for “exactly the same system that bitcoin was designed to be an alternative to”.
> 
> – [tweet](<https://twitter.com/nic__carter/status/1375521453286830088>) by Nic Carter.

Here are their arguments in a nutshell (paraphrased for brevity):

Noah: The more Bitcoin’s price goes up, the more resources it consumes. 

Nic: Gold extraction also consumes energy.[2]Independently, Nic Carter has many rebuttals against Bitcoin’s energy consumption FUD. See [here](<https://www.coindesk.com/the-last-word-on-bitcoins-energy-consumption>), [here](<https://www.coindesk.com/what-bloomberg-gets-wrong-about-bitcoins-climate-footprint>), and [here](<https://www.coindesk.com/frustrating-maddening-all-consuming-bitcoin-energy-debate>).

Noah: _Extraction_ is **not** the same as _Storage._ Stores of value like Gold, Stocks, our homes, etc. are not **that** expensive to store/maintain, as opposed to extract/create/build. The cost of secure storage of these traditional stores-of-value does not go up linearly with their value. Bitcoin is an exception, whose “cost of secure storage” (mining) goes up linearly with its price. It’s not a very efficient storage technology.

### Rebuttal

Now that the stage is set, we differentiate between the asymmetries of public-key cryptography and cryptographic hash functions. Stay with me here, this is super important. 

In public-key cryptography, there is asymmetry between the public key and the private key. Creating both keys is quite easy. For encryption, the public key locks, the private key unlocks. For digital signatures, the private key signs, the public key verifies the signature. For encryption, one cannot decrypt without the private key. For digital signatures, one cannot forge a signature without the private key. For the purposes of this article, let’s call these phenomena keyed-asymmetry. A cryptographic hash function, on the other hand, has no notion of keys. You have some information – you hash it, and you get a random looking fixed length string on the other side. Finding information that hashes to a specific non-random output is next to impossible. There is no private key that let’s you do this. The construction is just an algorithm, with no associated key-pair at all. To find a valid input that maps to a specific type of output, you need to try all possible inputs one at a time, for a long time – and hope to get lucky. Other than such brute forcing, there is no way around this asymmetry. Let’s call this keyless-asymmetry.

Given that background, let’s talk about the costs of secure storage of traditional store-of-value assets that Noah alluded to in his counter-rebuttal. My contention is that these assets are secured by poor physical world implementations of keyed-asymmetry. For example, Fort Knox is secured with a building, vaults, security protocols, and armed guards with guns. It’s assumed that unauthorized access through a break-in is impossible. But if you have authorization from someone in charge, you could walk in and walk out with the gold. This is equivalent to securing something with keyed-asymmetry. The private-key gives you access. Without the private key, even a James Bond villain cannot break in. Note that if the system didn’t allow the idea of a private key, that gold would be lost forever. A private-key is essential to making the gold visible/verifiable/transferable. A public good is being secured with a private-key, where the key-holder is supposedly competent and incorruptible.

In the digital world, public-key cryptography implements keyed-asymmetry in an ideal way, where security and authorized access are cheap, but unauthorized access is impossibly expensive. Digital signatures even go as far as revealing what the asset is, but just prevent forgery/confiscation of the asset. Physical manifestations of keyed-asymmetry, like the locks and vaults of Fort Knox, or social constructs like police-protection for your home, or even paper-and-pen signatures, are not even close to being as asymmetric in their nature as public-key cryptography is. They are poor substitutes, but we will give them a pass because they are, well, physical, and human ingenuity has not yet been able to import number theoretic cryptographic primitives to meat-space.

The key thing to note with keyed-asymmetry is that it is keyed. Access to the private key gives access to the asset. If you want to build a **public good** that has to be stored securely, is publicly visible, and doesn’t allow private key access – to anyone – governments, powerful corporations, venture capitalists, selective stakeholders – you just cannot use keyed-asymmetry. Something keyless has to be deployed: cryptographic hash functions. Used cleverly, they can store the asset securely, keep the asset publicly visible, and more importantly, prevent easy access – because cryptographic hash functions are truly one way functions (unless P=NP, but let’s not get into that). This clever way of using cryptographic hash functions to achieve an immutable public ledger is what Satoshi Nakamoto invented with Bitcoin. Remember that with hash functions, given that the output has to start with (say) 20 zeroes, one cannot find the corresponding input easily. They have to necessarily brute force it, by spending energy. This spent energy is what keeps Bitcoin’s public good, the blockchain, immutable – and not some key-holder’s competence and incorruptibility. 

Note that it is incidental that Bitcoin also separately uses public-key cryptography to protect individual bitcoins.[3]Satoshi’s admission about the choice of the secp256k1 curve for Bitcoin’s implementation of ECDSA as “I didn’t find anything to recommend a curve type so I just… picked … Continue reading

Back to the physical world: let’s say Fort Knox were transparent so that everyone could verify that there is gold inside. Now, everyone who needs to protect their purchasing power also wants to contribute their share in guarding Fort Knox so that even authorized entry is not possible. A physical world implementation of keyless-asymmetry. How could we do that? How much energy would that require? First of all, it’s not possible to contemplate such a physical system, but more importantly, even if you did contemplate such a system, it’s easy to see that it would consume an inordinate amount of public energy. I would be shocked if such a keyless-asymmetric security structure even existed in the physical world. Humans seem to have given up on that idea, and have come up with a trust based model where we go back to locks and vaults, but trust that key-holders are competent and incorruptible. Given this trust based model, Fort Knox like storage of gold is indeed cheaper[4]It’s ironic that Fort Knox itself is probably quite expensive to maintain. But that’s just poor implementation, and perhaps a bit of security theater. than Bitcoin’s expensive way of storing its equivalent of the gold.

Well, Satoshi didn’t go with the trust based model. Proof-of-work is a physical world realization of keyless-asymmetry. Bitcoin’s blockchain, being a public good – if it was secured using keyed-asymmetry – would have left us open to incompetence and corruption of key-holders. Bitcoin is, thankfully, secured by keyless-asymmetry. On the contrary, all physical goods (homes, paper documents, gold, country borders, etc.) and most digital goods (emails, bank ledgers, the Fed money printer, etc.) are secured by keyed-asymmetry. If a public good is secured with keyed-asymmetry, you should be worried. Key-holders have to be competent and incorruptible – forever. 

Keyed-asymmetry in the digital world is, of course, public-key cryptography, and hence, Bitcoin cannot be secured by public-key cryptography.

Given this setting, why proof-of-stake does not work for Bitcoin is just a corollary.

References[+]

References ↑1 | Bloomberg [paywall link](<https://www.bloomberg.com/opinion/articles/2021-03-24/bitcoin-miners-are-on-a-path-to-self-destruction>).  
---|---  
↑2 | Independently, Nic Carter has many rebuttals against Bitcoin’s energy consumption FUD. See [here](<https://www.coindesk.com/the-last-word-on-bitcoins-energy-consumption>), [here](<https://www.coindesk.com/what-bloomberg-gets-wrong-about-bitcoins-climate-footprint>), and [here](<https://www.coindesk.com/frustrating-maddening-all-consuming-bitcoin-energy-debate>).  
↑3 | Satoshi’s [admission](<https://pastebin.com/wA9Jn100>) about the choice of the secp256k1 curve for Bitcoin’s implementation of ECDSA as “I didn’t find anything to recommend a curve type so I just… picked one.” is quite illuminating in that Satoshi probably didn’t care as much about what public-key cryptography was used in Bitcoin as long as it did its job while maintaining a small footprint.  
↑4 | It’s ironic that Fort Knox itself is probably quite expensive to maintain. But that’s just poor implementation, and perhaps a bit of security theater.
