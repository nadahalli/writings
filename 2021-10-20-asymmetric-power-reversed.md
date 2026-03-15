---
title: "Asymmetric power, reversed"
date: 2021-10-20
source: https://tejaswin.com/2021/10/20/asymmetric-power-reversed/
---

What is power, really? 

Power comes about when someone has the ability to destroy someone else’s accumulated capital. 

What is capital, then? 

### Capital

Capital comes about as a result of raw materials, labour, and time. A healthy body, stored grains, a house to live in, a bank account with money earned through a job, or any sort of owned property – all of that is capital. Capital comes about as a combination of raw materials, labour, and time. Capital can either be consumed directly by its owner, or can be exchanged for other things like the labour of others. 

If Bob has accumulated capital like this, and Alice has the ability to either destroy this capital, or make its value go down to zero, or coercively move the ownership rights of the capital from Bob to a new owner, I claim that Alice has power over Bob. In some primitive societies, Bob is never allowed to even accumulate capital because Alice controls Bob’s labour and time as well. The capital Bob creates is directly accumulated into Alice’s “account” short-circuiting Bob’s “account” entirely. This is sometimes called slavery.

The modern power dynamic is mostly as a result of Bob having accumulated capital to show for his investment of raw materials, labour, and time – all of which actually are physically not recoverable after the capital has been accumulated. The only thing Bob has to show for his raw materials, labour, and time is the accumulated capital. If Alice has the ability to take this capital away from Bob, Bob is rightfully afraid of Alice’s power. 

The key thing to note is that the power is quick and efficient to wield. If Alice’s use of her power takes her as long as it took Bob to accumulate capital, there is no point in using power. Alice could as well generate her own capital, which is more efficient than going through the extra step of waiting for Bob to generate his capital and then confiscating it. Power is meaningful only when it’s quickly and efficiently wieldable. We can look at a few examples.

  * A gun is powerful because the shooter can quickly and efficiently end the life of the victim. The victim, on the other hand, would have spent a lifetime of raw material, labour, and time to grow a healthy body. 
  * Police have power because they can easily jail people, thereby nullifying the past and future labour/time of their “victims”.
  * Governments have power because they can take a share of their citizens’ accumulated capital in the form of taxes. Tax collection is inherently quicker and more efficient than generating capital. 



There is an inherently asymmetric nature to power. Power is wielded quickly and efficiently on capital that is slow and inefficient to accumulate. It seems like this is almost natural. To counter this natural emergence of power in society, we have designed social mechanisms to keep these powers in check. Every once in a while, these mechanisms break, and we see humans resort to their more basic instincts.

### Cryptography

Cryptography – through the magic of arithmetic and large numbers, reverses this very natural seeming asymmetric nature of power. Every primitive in cryptography reverses this power dynamic: Encryption, digital signatures, hash functions, zero knowledge proofs, multi-party-computation, you name it. Each of these lets Bob quickly and efficiently secure information, and makes it very difficult for Alice to undermine that security. It’s almost surreal to watch it in action. 

Let me give a simple example from Elliptic Curve Digital Signature Algorithm, which secures ownership rights in Bitcoin. Bob randomly generates a private key, which is a very quick and efficient task for any computer, and somewhat quick and efficient even with paper, pencil, and a coin. The private key looks like this: 

0xc2cdf0a8b0a83b35ace53f097b5e6e6a0a1f2d40535eff1cf434f52a43d59d8f

From this private key, Bob generates its corresponding public key, which is made of two numbers, and looks like this: 

0x6fcc37ea5e9e09fec6c83e5fbd7a745e3eee81d16ebd861c9e66f55518c19798,

0x4e9f113c07f875691df8afc1029496fc4cb9509b39dcd38f251a83359cc8b4f7

The key thing to note is that the process of generating the public key from the private key is quick and efficient. In this case, a special well known number has to be repeatedly squared the private key number of times to generate the public key. Repeatedly squaring to calculate exponents is quick and efficient. Reversing this process, that is, taking the logarithm of the public key to recover the private key, seems to be very hard, and there are no known easy ways of doing it. 

Another example is the famous RSA algorithm for encryption and digital signatures. Here, the private key is made up of two large prime numbers, and the public key is the multiplicative product of these two numbers. The two private key numbers look like:

p = 101565610013301240713207239558950144682174355406589305284428666903702505233009

q = 89468719188754548893545560595594841381237600305314352142924213312069293984003

The public key p*q = 9086945041514605868879747720094842530294507677354717409873592895614408619688608144774037743497197616416703125668941380866493349088794356554895149433555027

Given p and q, it’s quick and efficient to generate p*q, but given p*q, it’s not known how to quickly and efficiently calculate p and q.

_As the numbers get larger, the degree of asymmetry between the creation of security and the breaking of it gets harder._

### How does it all come together?

Just having some arithmetic be easy from one direction and hard from the other direction is not enough. These structures have to be useful to secure information. Wise cryptographers have come up with clever tricks to secure information using these arithmetic asymmetries. That these arithmetic asymmetries are opposite to the more naturally occurring power asymmetries in society is poetic justice of sorts. Mull over that for a second: the asymmetric nature of physical power where creation was expensive, but destruction was cheap – has been changed to a new order where creation is cheap, but destruction is expensive. All thanks to the quirks of how numbers work together. Just good old numbers.

To tie this to Bitcoin – we just have to understand that Bitcoin transforms capital to information. What used to be the best form of capital in the analog world (gold), is now digital. To prevent capture of analog capital (gold), owners used to build vaults and fortresses to make the oppressor’s power wielding inefficient. To prevent the capture of digital capital, all owners have to do is perform some arithmetic.
