---
title: "Bitcoin is Forever"
date: 2021-03-22
slug: "bitcoin-is-forever"
source: https://tejaswin.com/2021/03/22/bitcoin-is-forever/
categories:
  - "bitcoin"
---

The nature of Bitcoin is such that once version 0.1 was released, the core design was set in stone for the rest of its lifetime –  _Satoshi Nakamoto, creator of Bitcoin_

This goes against the more well understood motto of technology startups: “move fast and break things.” Unlike a startup, or even a big company, Bitcoin doesn’t move fast, or break things. Of course, I am **not** talking about its price as measured in USD or INR. I am talking about the entire Bitcoin system, or Bitcoin, the protocol. Bitcoin is stagnant, ossified, set-in-stone, resistant-to-change, and any number of such synonyms you can look up in a thesaurus. There are a few obvious questions that come out of this:

  * Why is ossification preferred over, say, innovation?
  * How do you achieve ossification in software?
  * Does it matter?



If you sit back and think, the answers to these questions are not obvious. Let’s address them.

### **Why?**

It seems obvious that innovation is good, innovation is right, and innovation works. Maybe it even captures the essence of the evolutionary spirit. So, why does Bitcoin **not** want to innovate? The answer lies in layers. By layers, I mean – in layers of abstraction. In any system, the base layer has to be set in stone for the layers above it to work. Think of civil engineering: it works because the laws of physics are set in stone. The value of the gravitational constant doesn’t change over time, thankfully, just because nature wants to innovate. 

Having an “innovative” base layer comes at a high cost to systems being built above it. Bitcoin was designed as a base layer for the world’s financial system. We can argue that that’s a stupidly ambitious goal, and is most likely not going to happen. That might very well be. Given the goal (stupid as it might be), innovation goes against Bitcoin’s purpose. An unchanging base layer of money allows innovation in layers above because a predictable foundation is a good foundation. Change-resistance tells its users that their initial trust in the system will not have to be recalibrated every now and then. A user’s understanding of Bitcoin doesn’t have to be updated after every recession. Money should be independent of booms and busts in the real economy. 

On the flip side, change-resistance resists all changes, good and bad. This is a philosophical preference, and reasonable sides have disagreed about this. Ethereum, the second most popular cryptocurrency, has argued that good changes are worth the cost, and is going ahead with radical changes to its base layer as we speak. And has done sweeping changes in the past.

### **How?**

Software is just text interpreted by a computer to perform some actions. How do you design a software system that cannot be changed easily? This goes into the weeds of decentralized distributed peer-to-peer systems, and a bit of the mechanics of how Bitcoin works. 

Bitcoin, the system, is made of tens of thousands of computers that run a specific piece of software. Each computer runs its own local copy of the software and maintains its own local copy of the so-called “coin-ownership database.” Satoshi released the first version of this software after 2 years of working on it (or so he/she claimed). This software’s source code is open, and anyone can modify it, or run it as it is. Many groups of people have modified this software as per their own vision. Each group has their own version of the software, which they hope users will run. 

The key thing to understand is that users decide what version of the software they want to run. All these users’ software together makes up the Bitcoin network. These users are not in a central database somewhere, with phone numbers or email addresses on which they can be contacted and asked to upgrade their software. They are not in a single country or jurisdiction where they can be coerced to upgrade their software, or else. They are spread all over the world in a loosely coordinated arrangement, interacting only through their already installed software. These could have been installed anytime over the last 11 years, and getting them all to agree on what software to run – is a coordination problem of mammoth proportions. Software that runs by itself on a device, while talking to a central server is reasonably easy to upgrade (like a gaming app on a phone). Software that **only** talks to peers will need other peers to also upgrade and follow the upgraded protocol for things to work. This kind of “protocol upgrade” is much harder to coordinate and enact. Cases in point: (a) the move from IPV4 addresses to IPV6 addresses on the Internet. (b) the disastrous set of upgrades from SSL 1.0->2.0->3.0->TLS 1.0->1.1->1.2->1.3 (SSL and TLS protocols enable the “S” in HTTPS).

The Bitcoin network agrees on a shared coin-ownership database despite every user running their own version of the software. If one user’s coin-ownership database differed from another user, Bitcoin would cease to work. So, how does it work then? This is where the idea of distributed consensus through proof of work comes in. Bitcoin nodes (each computer running the Bitcoin software is abstractly called a “node”) that also validate transactions and assign coin-ownership to users are called mining nodes, and these nodes have to burn enough electrical power to qualify every 10 minutes to propose valid transactions (a “block” of transactions) that the rest of the network accepts. The network rejects this block if it contains invalid transactions. What is valid/invalid was written in software by Satoshi in the first version of Bitcoin, and changing that requires the collective software upgrade that we encountered earlier. Additionally, this notion of what constitutes burnt electrical power is universal in nature, and all nodes can agree on this without relying on any trusted third party. This is the reason Bitcoin burns more power than your friendly neighboring country – to trustlessly determine who owns what through the universal physics of electricity.

But let’s say that some mining node decides to make a block with a transaction that allocates itself some additional money. An invalid transaction, so to speak. Let’s say this mining node can convince half the nodes in the network to change their software and accept that this block is valid. This half would accept this invalid block as valid and update their local copy of the coin-ownership database. The rest of the network would reject this block, and would have a different coin-ownership database. We have what is called a hard fork.

Bitcoin has had many hard forks in its history – almost all of them by design. And none of them with a 50-50 split; all of them were lopsided splits. A few people wanted to change the rules of the game over the years, got a few more people to agree with them, and decided to have different versions of the coin-ownership database. Think of how, before the partition of India in 1947 – there was one Rupee, and a database of who owns how many rupees. This database was, of course, not maintained on a computer – but through ownership of bearer notes. After partition, there were two versions of the Rupee, with two databases of who owns what. Each Bitcoin hard-fork can be thought of as a similar partition of a currency with separate coin-ownership databases going their own way after partition. The fork with the largest set of miners, users, economic value, and other intangible metrics takes the moniker of “Bitcoin.” Others call themselves “Bitcoin Cash,” “Bitcoin Cash SV,”, “Bitcoin Cash ABC” and so forth.

There is also a softer notion of partition called the “soft-fork”, which is a bit more technical and nuanced. Soft-forks **do** change the notion of what Bitcoin means, but affecting these soft-forks over the entire network takes many years of coordination, and can only be done for the least controversial changes. And there is no guarantee that they might ever see the light of the day. The last successful Bitcoin soft-fork (fork-name: SegWit) was in 2017 and the forking/upgrade process left such a scar on the system that the next fork/upgrade (fork-name: Taproot) though code-complete, and almost entirely uncontroversial, might take years to roll out – if at all.

If they are so hard, how does Ethereum pull off forks? These are some of my reasons (ranked in order of how controversial they could be):

  * Ethereum’s [BDFL](<https://en.wikipedia.org/wiki/Benevolent_dictator_for_life>) is well known in real life, very active, and has strong opinions on how Ethereum should evolve. His word commands respect in the community, and is able to affect change. Bitcoin’s creator disappeared in 2010, and has not been heard of since.
  * Ethereum’s nodes are comparatively harder to run, and are thus run by fewer people – who can coordinate upgrades more easily. Bitcoin nodes have a lighter CPU, memory, and network footprint, and can be run by more people.
  * Ethereum’s users want newer features and are willing to upgrade more easily. Bitcoin users are more resistant to change.



### **What now?**

I claim that Bitcoin’s resistance to change is one of its biggest value propositions, and gives us a form of money whose monetary policy, rules of the game, and general contract with the outside world are almost set in stone. You can buy bitcoin, bury the private key, come back to it in 50 years, and it will still be valid, and perhaps, more valuable.
