---
title: "Homomorphism"
date: 2022-01-31
slug: "homomorphism"
source: https://tejaswin.com/2022/01/31/homomorphism/
categories:
  - "crypto tricks"
  - "cryptography"
---

If Zero Knowledge Proofs are the kind of magic seen in a full fledged opera theater, Homomorphisms in Cryptography are like intimate card tricks done in a 1-1 setting. Less grand, less machinery at work, but elegant and counter-intuitive all the same.

You hear about homomorphism in encryption first. They also appear in commitment schemes – and given my interest in Bitcoin, homomorphic commitments more appropriate for this blog. But let’s see encryption first, as it’s a bit more accessible. 

### Homomorphic Encryption

The idea of homomorphic encryption can be captured in these steps.

  1. You have a secret number 42, and you encrypt it to get gibberish – which happens to look like 592ed4fa.
  2. You have another secret number 3, and you encrypt it to get some other gibberish, which looks like 85ab8927.
  3. It just so happens that the product 592ed4fa*85ab8927 is the encryption of 42*3 = 126!



And the initial encryption was not a toy encryption either. It’s a classic algorithm, and has all the security that you could want in the world. To appreciate how other worldly this is, you have to understand that encrypted text, for all purposes, should be random. Of course, it’s not entirely random, it’s actually the encryption of some non-random text. But it should _be_ random for everyone else. Now this random gibberish can be used in a mathematical operation, and the result actually has a tie back to un-encrypted plaintext is what I would qualify as magic. 

Of course, genius level magic is when you can apply _any_ mathematical operation on encrypted blobs and make it reflect in the un-encrypted world. In the previous illustration, we assumed that the homomorphism works only for multiplication. Fully Homomorphic Encryption, where every mathematical operation is allowed, was invented quite recently (2009) by [Craig Gentry](<https://en.wikipedia.org/wiki/Craig_Gentry_\(computer_scientist\)>). 

Let’s see one encryption scheme where it’s quite simple to see how homomorphism is quite natural, and doesn’t even need any advanced knowledge of mathematics: Elgamal Encryption.

Encryption:

  1. Generate private key x randomly, create public key h = g^x from it (g is a universally known constant).
  2. Let’s say you want to encrypt message m with the public key h.
  3. Choose y randomly, and calculate s = h^y. Also calculate c_1 = g^y and c_2 = m \cdot s. Your encrypted blob is (c_1, c_2).



Decryption:

  1. The decrypter has access to x, g, h,  and (c_1, c_2). Remember that the encryption was done with the public key h, and decryption needs private key x.
  2. Calculate s = c_1^x. Convince yourself that this is the same s that was calculated in Step.3 of the Encryption algorithm. 
  3. Calculate the secret message m = c_2 \cdot s^{-1}.



Homomorphism:

  1. E(m_1) = (g^{y_1}, m_1 \cdot h^{y_1}), and E(m_2) = (g^{y_2}, m_2 \cdot h^{y_2}) after encryption.
  2. The product of the encrypted blobs is the pairwise product of the two parts of the blob. It’s quite easy to see that this is the encryption of the product of the messages.
  3. E(m_1) * E(m_2) = (g^{y_1 + y_2}, m_1 * m_2 * h^{y_1 + y_2}) = E(m_1 * m_2). This can be decrypted with the same private key x.
  4. Voila!



Let me say that again: you can perform mathematical operations on what looks like gibberish, and get back something that is the encryption of something else valid. The first time I heard that this was possible, it had me convinced that such advanced mathematical trickery had to be beyond understanding. To see it just be about exponents being added, is almost anti-climactic. But that’s a good thing, right?

### Homomorphic Commitments

We saw cryptographic commitments in a previous article, but here’s a short introduction that should be enough to read the rest of this post. Say you want to commit to something – but don’t want to reveal it in the present, but only reveal it in the future – how do we do that? Typically, you could write down your choice on a piece of paper and put it in an envelope, and your counterparty is convinced that when the envelope is eventually opened, the contents were written during the commitment phase. In Cryptography, this is done using – you guessed it – numbers and some arithmetic operations. 

Homomorphic commitments take it a bit further. You commit to two messages 42 and 3, and you get commitments which look like gibberish. You multiply the gibberish commitments, and you get a commitment to the sum 45. The arithmetic looks quite similar to the one shown above for Elgamal encryption, with exponents being added when you multiply the base numbers (surprisingly useful trick!!). The thing that makes homomorphic commitments interesting to Bitcoiners is that we can hide the value of the money being spent, without being able to cheat.

What?

Yes, you could easily design systems similar to Bitcoin where the validating nodes are convinced that you didn’t spend money you didn’t own and you didn’t create money out of thin air without ever seeing the actual amount you spent. All they have do do is verify the homomorphic commitments to the value, and check if the commitments add up properly. There is a bit more complexity around proving that you are operating in the right range of numbers (say, [0, intmax]) or some such, but those are just details. In Bitcoin-land, these are called confidential transactions and have seen some implementation in other currencies like the Mimblewimble protocol based Grin. Sadly, this will probably never make it to Bitcoin and we are doomed to disclose our spending amounts publicly, but the fact that it’s possible to hide the amounts you spend, without being able to cheat – is quite cool.
