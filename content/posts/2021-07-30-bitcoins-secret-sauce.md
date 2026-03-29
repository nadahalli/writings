---
title: "Bitcoin’s secret sauce"
date: 2021-07-30
slug: "bitcoins-secret-sauce"
source: https://tejaswin.com/2021/07/30/bitcoins-secret-sauce/
categories:
  - "bitcoin"
---

Bitcoin’s secret sauce, and how it works, was on full display these last few weeks. Bitcoin was designed to work against the most powerful of adversaries, and boy – did the adversary show up!

### China Ban

A few months ago, 45% to 75% of Bitcoin mining happened inside China. Then the Chinese government banned it.

There are anecdotal accounts from people on the ground who are seeing Bitcoin mining operations being shut down by law enforcement agents. And there are similar accounts from people on the ground elsewhere in the world where they are receiving containers full of mining hardware.

And then there is the Bitcoin blockchain – the source of absolute truth. I have a copy of the Bitcoin blockchain on my computer, and could actually run the numbers myself and see that the production of Bitcoin blocks slowed down dramatically. Here’s a plot of how long it took, on average, to find 2016 blocks from 12-May-2014 to 18-July-2021. 

![](/images/interblock_gaps-1.png)

Bitcoin blocks, on an average, are supposed to be generated once every 600 seconds. But you can see the spike in this number on the graph towards the end, going all the way up to 832 seconds. This means that during that period, the total number of active miners went down dramatically, and that led to the inter-block average-gap increasing equally dramatically from 600 seconds to 832 seconds. 

Putting the anecdotal and canonical sources of data together, we can be reasonably certain that the Chinese mining ban lead to a global drop in Bitcoin mining.

Does it matter?

Not really. Miners come, miners go – Bitcoin chugs along. This is not an accident. This is by very careful design. Bitcoin targets a block production rate of 600 seconds per block. If Bitcoin’s design had been naïve, whenever its dollar value went up, more miners would enter the system to make more money, and blocks would arrive faster than 600 seconds. Similarly, if its value went down (or if governments kicked them out), miners would leave the system, and blocks would arrive much slower than 600 seconds. The block production rate on either side of 600 would persist, and reflect the total number of miners in the system.

But no, that’s not what happens. No matter how many miners are in the system, it always takes around 600 seconds to mine a block. This is done through the difficulty adjustment algorithm, also known as Satoshi’s stroke of genius.

### Difficulty Adjustment a.k.a Bitcoin’s secret sauce

Before we get to the difficulty adjustment algorithm, we have to first understand why keeping the inter-block interval of 600 seconds is important. Bitcoin works because everyone can check whether their perceived ownership of their own Bitcoin is fact or fiction. To check this, you need access to Bitcoin’s data. Where is this data? How big is it? How do I access it? Bitcoin’s data is not held by some central custodian, or a bank. It’s held by everyone who is interested. It includes all transactions from the genesis block onwards – from January 2009. But storing everything with everyone sounds crazy – and to be honest, it is crazy. But the more you think about it, the more you realize that there are no other easier ways of doing self-validation, other than offloading the “do I control my money or not?” question to someone else – and trusting them. Bitcoin prefers the opposite: self-validation.

So, if we accept the crazy idea that everyone stores a copy of the blockchain, we have a fundamental tradeoff – the blockchain cannot get very big (by growing very fast). It also cannot stay static: new transactions need to be added every so often to facilitate economic activity. Currently, the blockchain is around 377 GB, and growing by around 50 GB per year. If it grows too fast, not everyone will be able to hold their own copy. If it doesn’t grow fast enough, there is not enough transaction space to accommodate the demand for transactions. Under these constraints, Satoshi decided that a 1MB block every 10 minutes is a good tradeoff. To keep this tradeoff constant, blocks cannot be generated slower or faster. 

What happens if Bitcoin’s value skyrockets and everyone wants to be a miner? Remember that a miner who generates a new block gets to keep the newly minted Bitcoin that comes out of each block. So, if the value of Bitcoin goes up, expect more miners to materialize. To accommodate this, Satoshi designed a simple algorithm that makes mining harder or easier depending on how long it takes to generate the previous 2016 blocks. 

The Bitcoin protocol contains a positive number called “difficulty”, whose value is currently 13,672,594,272,814. This number controls how hard or easy it is to mine a block. Let’s say the total time taken to mine the previous 2016 blocks was greater than 2016 times 600 seconds, by a factor of X. This difficulty number is then adjusted lower by the same factor X. If the time taken to mine the previous 2016 blocks was lower, the difficulty number is adjusted upwards – again by the factor X. That’s it. 

As far as “algorithms” go, this is as simple as it gets. It’s middle school level arithmetic. Turns out that this is not simple at all and was never done before. Other than combining existing ideas from cryptography and distributed systems, Satoshi’s only novel contribution was this middle school level formula. The genius, as they say, is in the simplicity of it.

When these erstwhile Chinese miners turned down their mining hardware around end of June/beginning of July 2021, Bitcoin’s mining difficulty dropped from 19 trillion to 14 trillion, by around 5 trillion – which is around 28%. The reduced difficulty made it easier for the remaining online Bitcoin miners to start generating blocks every 10 minutes again. The next 2016 block average was 630 seconds. Voila!

As Bitcoin’s value increased from 0 to wherever it is today, miners have only entered the system – and have rarely left. Difficulty has always gone up – to accommodate this increase in value. So, how does this difficulty number actually make it easier or harder to mine a Bitcoin block?

### The Proof of Work Function

Bitcoin, famously, relies the “partial hash-preimage puzzle” to build its Proof of Work function. A lot of people argue that miners using tons of custom built hardware and scouting the earth for cheap electricity to solve this puzzle many many times over is a waste of resources. That comes down to whether we consider Bitcoin itself to be a waste of resources. That’s a debate for another time. But if we consider that Bitcoin has value – we have to take a moment to appreciate how difficult it is to design a function that has all the properties of Bitcoin’s Proof of Work function.

The proof of work function is:

![](/images/1.png)

That’s it. You double hash data from the block you want to generate, and check if that hash value is less than the target on the right hand side of the equation. If it’s not, you change the block data, and try again, and again, and again, and again…

For example, if I double hash make-believe block-data, say the string “Bitcoin forever!”, I get the number: 

99399038078883646938846821706752581723151100264172406332358249387420489004987\. 

The current value of the target is:

1971823790658122626473078926498088015421759366553927680\. 

So, it doesn’t work. I need to keep trying the function again and again with different block-data to hit gold. The actual previous Bitcoin block’s hash was 888160945014446794317532755205888398236464272495427689, which is under the required target, and that miner struck gold – so to speak. If the difficulty number goes up, the mining target goes down, and finding block-data that double-hashes to a number lower than that target gets harder. It’s like tossing a 6 sided dice and wanting to hit a number less than or equal to 1. It happens only once every 6 times. If difficulty were to reduce, the target would move to a number less than or equal to 2. That happens every 3 times – mining just got easier.

Why go into the nitty gritty details of this function, with all the associated arithmetic and probability? I want to get into the 3 properties that this unique function has, that makes it ideal for Bitcoin mining – and resisting nation state attacks. Not everyday do you see nation-states attacking simple computations like these, and… losing.

**Parameterizability** : The function provides very fine degree of control over how much harder or easier we want the function evaluation to be. If you increase or decrease the difficulty number, the function becomes easier or harder to evaluate, respectively.

**Memorylessness or Progress-free ness** : Even if you have already run the function a million times, it still doesn’t give you any advantage over the next run. Each run of the function is what is called a Bernoulli trial – with the odds of hitting gold the same no matter how many times you have tried in the past. This makes sure that larger miners have no other advantage than just the larger chance of producing a block. If this property weren’t there, the largest miner would *always* win, even if they had just 0.0001% more power than the next largest miner. 

The other incredible advantage of Memorylessness is that a miner can be turned off, put in a container, shipped elsewhere and plugged back in. The only loss the miner incurs is the Bitcoin that could have been mined in that interim time when the machine was turned off. Most physical objects being built, or even computations that are being performed on computers rely on previous data or “progress” that has been done, stored and retrieved, so that we can continue the process further. Shutting down something abruptly, without needing to store any state of progress, and starting elsewhere without any extraneous loss is _not that common_. This allows Bitcoin miners to be incredibly mobile and seek out the cheapest electricity wherever it exists. They are, in the true sense, plug-and-play.

**Hard to compute, but easy to verify** : To get the double-hash value which is under the target needs millions of trials of the function. But once someone finds it, the rest of us can verify it immediately with just a single iteration of the function. This, again, makes decentralization possible – where all of us can run the Bitcoin software on our computers and check that the miners are doing the right thing.

Replacing this function is not that easy. Most attempts have kept the general idea, and have tinkered with the specifics.

### **Conclusion**

A nation state the size of China attacked Bitcoin where it’s supposed to hurt: Bitcoin Mining and all they managed to get in return was a giant shrug of indifference by the protocol. Yet another instance of Bitcoin living up to its promise of being designed to last forever. This self-adjusting nature of Bitcoin – that makes it change itself based on market conditions, with no one central entity being in charge – separates it from all other forms of money. Fiat money always has a central planner. Bitcoin has a protocol.
