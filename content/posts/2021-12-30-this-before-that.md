---
title: "This Before That"
date: 2021-12-30
slug: "this-before-that"
source: https://tejaswin.com/2021/12/30/this-before-that/
categories:
  - "cryptography"
---

This article is ostensibly about why the challenge space in an interactive zero knowledge proof has to be large. Understanding this rather obscure theoretical aspect of zero knowledge proofs is quite rewarding intellectually. I promise. 

Let me start with a trivial question. How do you convince yourself that something happened before something else? 

Here’re some possible answers.

  1. You literally see Event-X happen. You wait for a bit. You then literally see Event-Y happen. You know that X happened before Y because you saw it yourself. You are convinced because you trust your memory of what you have seen.
  2. Sometimes, things are physically structured such that Y cannot happen before X. Let’s say I see you wearing socks and shoes, you could not have worn shoes before wearing socks.
  3. Someone you trust tells you that Event-X happened before Event-Y and you believe them.



These are so intuitive that you don’t bother to reflect on this till someone specifically asks you this question. In fact, the 2nd example is used in many magic tricks – you expect a certain order because of obvious structure, but the magician circumvents that order to enthrall you with his magic. One such trick is where the magician pretends to cut an unpeeled banana with an imaginary knife, and then peels the banana to reveal a precise cut in the same location on the inner fruit. The magic works because it belies the natural order of events that you are used to.

Now that I have asked this seemingly trivial question on ordering, let’s formalize these three modes of what _proves_ order: Witness, Structure, or Trusted Third Party.

  1. Witness: You personally witnessed something happen before something else.
  2. Structure: The structure of the two events is such that one cannot happen before the other. This could be due to physics, or the natural fixed dependency between two events, like birth and death. 
  3. Trusted Third Party: A newspaper, a notary, an atomic clock which knows “real time”, etc.



Now that we have set the building blocks of our discussion, we can get into the main question. Let’s say Alice sees 2 events happen in succession. She wants to convince Bob that this is the case, but Bob wasn’t there with her at the same time. Alice is convinced because of mode #1: she was herself a witness to the order. Bob was not there at that time. So, mode #1 is ruled out. How does Alice convince Bob of order using mode #2 or mode #3?

### Structure

If there is structure between these events, it’s self-evident to Bob that Alice is right. No real proof is required. But structure is not as straight forward as birth/death, socks/shoes, peeling/cutting a fruit, etc. Bob has to make sure that he verifies the structure thoroughly to see if Alice is playing any tricks. For example, in the pre-cut banana magic trick, Bob must look for a tiny pin-sized hole in the banana peel to see if Alice the great magician inserted a needle in the banana, moved it around to cut the fruit before beginning the trick. This would tell Bob that the banana was pre-prepared, and the structure assumption doesn’t hold anymore. Structure works, but only if Bob can convince himself that the structure was not tampered with by Alice. That there are no magic tricks or shoe-contortions that allows Alice to wear her socks after she has worn her shoes.

### Trusted Third Party (TTP)

TTP’s work, but there’s just not enough of them around. We have newspapers, atomic clocks, notaries, and such, but they don’t cover every event that we are interested in. How does Alice get a TTP to notarize that event X happened before event Y? 

Here’s one approach: Alice waits for a TTP to output a signed timestamp. The TTP doesn’t even know that Alice exists. A newspaper, for example, prints a copy on physical paper everyday. This counts as a signed timestamp. Alice then combines this signed timestamp and Event-X as two inputs to event Y. Bob sees event Y, and is convinced the output of Event-Y happened after Event-X. Bob is convinced because he sees that the timestamped newspaper is an input to Y, and that means that even X should have been available before Y. This is similar to how they show movie-kidnappers proving that their hostage is alive at certain time. They make a videotape of the hostage holding that day’s edition of a newspaper. In this example, the newspaper is the TTP; the hostage being alive is Event-X. The hostage holding the newspaper, being videotaped is equivalent to the timestamp and Event-X being given as inputs to Event-Y. 

In fact, this approach is a slightly modified take on mode #2 (structure). Alice is using the newspaper in the video to convince Bob that the newspaper was printed first. Alice then made a video with the newspaper clearly visible in it, and these two events could have happened only in that order. The only two ways it could have happened in the opposite order are:

  * Alice predicted in advance what the newspaper frontpage would look like in the future. She then prints that newspaper herself, and uses it in the video. The newspaper is eventually published exactly like she had predicted, and Bob is now convinced. Alice is unlikely to be able to pull this off because she doesn’t know the future. 
  * Alice is friends with the newspaper editor, and this editor will print a headline in the future that Alice has asked him to. That way, she can print her own copy of the newspaper with this headline, make the video and when the real newspaper is printed with this pre-determined headline, Bob can be fooled into thinking that the video was made after the newspaper was printed. But this scenario contradicts our assumption that the newspaper is a trusted third party, and cannot be manipulated by either Alice or Bob.



### Interactive Proofs

With this background, we now get into interactive proofs. It so happens that interactive proofs rely on Alice and Bob’s shared acceptance that Event-X happened before Event-Y because Alice and Bob together orchestrate these events and are both witnesses to it. In the “Where is Waldo” example from [our previous article on Zero Knowledge Proofs](<https://tejaswin.com/2021/08/29/zero-knowledge/>), we saw that Alice does Event-X first (places a piece of paper on the picture, called a “commitment”), Bob later comes in and gives Alice a challenge (either open the paper and show the image inside, or cut a hole in the paper to reveal just Waldo through the paper). Alice then does what Bob asks of her, and Bob can verify the response (called the “response”) They can repeat this sequence a few times for Bob to be convinced that Alice knows where Waldo is. Alice and Bob repeat this sequence of “commitment-challenge-response” (randomly changing the commitment and challenge each time) a few times and if it works each time, Bob knows that it’s overwhelmingly likely that Alice knows where Waldo is. 

The catch is – only Bob can be convinced of this. If Bob goes to Carol and shows her this sequence of “commitment-challenge-response” triples, Carol doesn’t have to be convinced. Carol knows that Bob can create a similar sequence by doing the slightly different ordering of “challenge-commitment-response” (commitment and challenge are swapped) and trick her. In the Where is Waldo example, Bob makes up a valid commitment to both his possible challenges. Here’s how.

  * Challenge #1. Reveal that the picture under the paper is the original Where is Waldo image. If Bob wants this to be the challenge, the equivalent commitment is random. The paper can be anywhere on the image.
  * Challenge #2. Cut a hole in the paper and reveal Waldo. If Bob wants this to be the challenge, he make a new picture with just one image of Waldo in the middle, covers it with the paper, and then cuts it open to reveal Waldo.



In both these cases, Bob doesn’t know where Waldo is in the original picture. So, without actually knowing where Waldo is, Bob can write down a sequence of “Commitment-Challenge-Response”, by generating the challenge first, and not the commitment. 

### Why Order Matters

When Alice and Bob were doing the interactive proof, Alice could not trick Bob this way, because Bob saw in person that Alice did the commitment first, and then had to respond to Bob’s challenge without changing the commitment. Bob knows the ordering of “commitment-challenge-response” because he was there, and saw it happen. But he can never convince Carol of this because Carol also knows that Bob can create such a sequence himself without knowing where Waldo is, by just changing the order of “commitment-challenge-response” to “challenge-commitment-response”. Even if Bob is honest, he cannot convince Carol that Alice proved it to him that Alice knows where Waldo is. Carol can only be convinced if Alice and Carol do the interactive proof between just the two of them, and Carol can be witness to the ordering of “commitment-challenge-response”.

### Challenge Space

The Where is Waldo proof doesn’t work as a general interactive proof because Bob cannot use it to convince Carol that Alice knows the secret. This is because the sequence “commitment-challenge-response” relies on mode #1 order proof (witness). What if the “commitment-challenge-response” sequence has some structure that proves that the commitment happened before the challenge? That could convince Carol that the sequence was generated in the right order, and not the cheating-order. In the Where is Waldo proof, there is no obvious way of imposing structure on the ordering between the commitment and the challenge. 

In other interactive proofs (like the Schnorr protocol), Bob’s challenge is just a large number. Alice has to do some arithmetic operations with her previous commitment and Bob’s challenge number to come up with a response that satisfies Bob. In these kinds of proofs, it is possible that we could impose some structure between Alice’s commitment and Bob’s challenge such that it’s obvious to Carol that Bob could not have created the challenge before Alice made her commitment. 

One obvious example of such a structure is a secure hash function like SHA256, where Bob’s challenge is the hash digest of Alice’s commitment. Carol knows that Bob cannot first come up with a challenge and then make up Alice’s commitment – because the hash function cannot be inverted. In such a proof system, Bob always makes up his challenge by hashing Alice’s commitment. So, the sequence is “commitment-hash(commitment)-response”. The challenge is always hash(commitment). If Bob now takes a series of such triples to Carol, Carol is sure that these triples were generated honestly by either Alice and Bob using an interactive proof, or Bob knows the secret and was able to prepare the proof himself. Either way, Carol can accept the proof. This is how digital signature schemes are constructed, where Bob can show Carol that Alice signed something, and Carol will believe that Bob is not lying (if Carol can independently confirm what Alice’s public key is).

### So…..

We touched upon many concepts of Zero Knowledge Proofs in an informal way here. C-Simulatability in Sigma Protocols and the Fiat-Shamir heuristic, mostly. There are graduate level text books on these topics, and I have barely scratched the surface here.
