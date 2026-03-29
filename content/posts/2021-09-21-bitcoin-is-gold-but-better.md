---
title: "Bitcoin is Gold, but better."
date: 2021-09-21
slug: "bitcoin-is-gold-but-better"
source: https://tejaswin.com/2021/09/21/bitcoin-is-gold-but-better/
categories:
  - "bitcoin"
---

![](/images/01-36140-goldatom01.jpg)

_The more I learn about Bitcoin, the more I respect gold. The more I learn about gold, the more I appreciate**** Bitcoin_ – [Nic Carter](<https://twitter.com/nic__carter/status/1438298080848265217>)

_One thing Bitcoin taught me is that goldbugs don’t truly understand why gold is valuable_ – [Vijay Boyapati](<https://twitter.com/real_vijay/status/1440153757233266692>)

Bitcoin as Gold 2.0 is a great analogy. Both Bitcoin and gold are mined. In both, the miner spends an excessive amount of time and energy going through a large haystack looking for a shiny needle. With gold, the haystack is the entire Earth, and the needle is around 3,300 metric tons of gold per year (to put that in context, we extract around 2,500,000,000 metric tons of iron per year).

Other than having to be mined, natural laws of physics and geology have given gold many different properties:

  * Inertness: Gold doesn’t rust, corrode, or evaporate. It just stays as is.
  * Density: Gold is among the densest metals known to us. It’s one notch below the legendary tungsten (used to make fake gold, typically) and almost twice as dense as lead.
  * Mouldable: Gold can be broken down into small pieces and reassembled back without losing any other properties.
  * Scarcity: As we saw earlier, gold is not that readily available. But interestingly enough, it is not incredibly rare either and is distributed relatively evenly on Earth, albeit in small quantities – unlike say, platinum, which is rarer and heavier than gold but also concentrated in just South Africa. Gold has what appears to be “optimal scarcity.”



What appears as boring chemical and physical properties of a shiny metal, is in fact, a remarkable set of properties that is not common to physical things. We will soon find out – why these properties enable gold to solve a significant problem entirely unrelated to gold itself. First, a slight detour.

## Capital and Labor

There have been libraries worth of books written about capital and labor, but I want to talk about just one thing: how do I save the fruits of my labor. If someone performs a task and wants to be compensated for it, what is the best means of payment? Curiously, this means of payment needs properties quite similar to gold.

  * Inertness: their compensations shouldn’t rust, corrode, or evaporate.
  * Density: their compensations should be economical to save, store, and carry. It shouldn’t need a container ship to carry the amount of labor I have expended to – say – buy a house.
  * Mouldable: Labor spent on one task should be compensated such that the person can utilize this for many tasks later. Or the compensation for the labor of many tasks should be aggregatable into one spendable unit later.
  * Scarcity: If whatever is being used for saving the fruits of my labor is available freely everywhere to everyone, **my** part of that compensation “pool” becomes infinitesimally small and meaningless.



Many units of such compensation accumulate capital. This capital is then spent on other labor. And so forth. This conversion of energy from labor to capital and then back to labor again allows humans to specialize and flourish. Peoples of past millennia figured out that to achieve this state, the means of payment had to be gold. I am simplifying the enormously profound topic of the emergence of money. Read Nick Szabo’s [classic essay](<https://nakamotoinstitute.org/shelling-out/>) on the origins of money for more details.

## Is Gold Good Enough?

Unfortunately for gold, physics also prevents it from being teleported across space. That’s a bug in gold’s very nature. If labor wants to be paid across timezones instantly, gold just doesn’t cut it. We have to introduce a trusted third party whose IOU serves this purpose. If we are the type who doesn’t trust third parties and want to use something natural, or something not controlled by anyone, we were out of luck. Till Bitcoin, which can be teleported.

Unfortunately for gold, it’s not possible for any individual to know how much gold exists on Earth. Above or below ground. There is some talk about gold being found on asteroids. What is the total supply of gold? We are out of luck. Till Bitcoin, whose supply is capped.

Unfortunately for gold, it’s hard to judge whether a piece of metal I have in my hand is gold or not. It could be gold-coated tungsten, for instance. We need specialized equipment to assay gold, and if an average person wants to make sure that what he received as payment is actually gold, he is out of luck. Till Bitcoin, which can be verified trivially.

All these gold-bugs are fixed with Bitcoin. Bitcoin also carries gold’s features of inertness, density, mouldability, and scarcity. How does it all work? It’s not hard to design a centralized digital system that has all these properties. Designing a decentralized system with these properties, and making sure that it doesn’t change at all – is the hard part. I wrote about this part in an earlier post: [Bitcoin is Forever](<https://tejaswin.com/2021/03/22/bitcoin-is-forever/>). This social barrier that lets Bitcoin have gold’s properties, and not its bugs – has to hold forever – for Bitcoin to succeed in replacing gold as a way to store the fruits of one’s labor. I have high hopes for this, but by no means am I certain.

## Needles in the Haystack

Gold mining is expensive, time-consuming, and energy-intensive. Again, thanks to physics and geology. Also, gold mining has been going on for millennia and has been somewhat commoditized. We find parts of Earth with gold and deploy a somewhat well-understood piece of technology on it. On the other hand, Bitcoin mining is a bit trickier – but in my opinion, more elegant. Let’s see why Bitcoin mining is expensive and consumes energy. Rewinding ourselves all the way back to the idea of mining as finding a needle in a haystack, Bitcoin’s haystack is of the size 2^256, which is this astronomical number: 115792089237316195423570985008687907853269984665640564039457584007913129639936

The proverbial needles in this haystack are currently of the size 2^180, which is a much smaller number than the size of the haystack: 1464008529111715998423770879212294388201901757724360704

Any number smaller than this number is a needle for us, and if we find it – we hit gold, so to speak. As it turns out, the only way to mine Bitcoin is to randomly go through the entire range of numbers from 0 to 2^256 and hope to get lucky with a number that is lower than 2^180. Well, hang on a second!! If I start with 1, 2, 3, and so forth – it seems like it should work. They are all lesser than 2^180. Unfortunately, it’s not that easy. Bitcoin’s protocol forces randomness on us as we go through the range of numbers from 0 to 2^256. Randomness ensures that if we pick any random number from this range, we have very high odds of picking something much larger than 2^180. So, we trudge along randomly sampling numbers, looking for gold, thereby proving to the protocol that we are doing work. With enough proof-of-work, we eventually hit gold.

Can I do this on my desktop? What are my odds of striking gold? I wrote a quick program on my desktop that could make around 1,000,000 random guesses per second. That’s 10^6 or 2^20. Bitcoin sets its mining window to 10 minutes, and in that time, my desktop can run through 2^29 random numbers. My target, though, as set by the Bitcoin protocol, is around 2^(256-180), or 2^76 numbers, before I hit gold (metaphorically). Even if my desktop has eight cores, I can get to 2^32 numbers. That’s still quite far away from 2^76. How do I achieve 44 orders of magnitude in performance improvement? Are there special tools for this? There are!!

The thing is – general-purpose computers are like human hands, good at many tasks, but not fast or efficient at any specific task. One can instead design tools to solve specific problems – like how we use a hammer to put a nail in the wall and not use our hands for that job. But these tools are pretty useless at solving other problems. A hammer is no good for cutting paper, for example. Human hands can do both, but not as efficiently. Let’s say we designed a hammer to do the Bitcoin mining function and make it as streamlined as can be designed. Can we get 44 orders of magnitude improvement over the equivalent of human hands? Somewhat.

ASICs, or Application Specific Integrated Circuits, are the best type of computers for Bitcoin mining. Among these, the very best can do 110 terra-guesses per second, or around 2^56 random guesses every 10 minutes. That’s 27 orders of magnitude improvement over my desktop. One such ASIC costs around $15,000 and is hyper-optimized just to run the Bitcoin random number generator and nothing else. If we assume the lifespan of hardware to be around two years, the amortized cost of this ASIC is $0.14 for 10 minutes of use. Before we forget, this ASIC has to be connected to a source of power, the cheapest of which costs around $0.06 per kilowatt-hour (kWh). The ASIC has a power rating of about 3.2 kWh, making it cost $0.03 for 10 minutes of use. Going from 2^56 to the required rate of 2^76 is still around 2^20, or just more than a million such ASICs spread over a few datacenters, making the cost around $225,000 for 10 minutes of mining. The gold strike at the end of the 10 minutes is worth 6.25 Bitcoin, which translates to around $260,000 in today’s USD price, netting a profit of $35,000 dollars every 10 minutes to the whole mining industry.

This is just a back-of-the-envelope estimation with more assumptions than I can list: transaction fee variance, location rent, software and hardware labor cost, hardware age/lifespan/generation, electricity price variance, regulatory uncertainty, etc. Bitcoin mining is almost as geographically distributed as gold mining, and it’s hard to get exact numbers.

On a side note, this entire mining process is random, which ensures that the mining reward at the end of each 10 minute period goes to a random miner, where the randomness is proportional to their share of the entire network’s computing power. This delicate dance of the 10-minute timespan, the proportionate randomness-based distribution of rewards, and other such details were covered in my previous post on [Bitcoin’s secret sauce](<https://tejaswin.com/2021/07/30/bitcoins-secret-sauce/>).

There are a few interesting consequences of this particular setup:

  * When Bitcoin is more valuable, older and less efficient hardware becomes viable. On the flip side, when Bitcoin’s value goes down, it’s no longer profitable for miners to run old hardware. Bitcoin’s value, as we know, is highly volatile – which makes old mining hardware almost impossible to throw out as e-waste, as we never know when they will become more profitable to run again. Mining hardware, which guesses random numbers, is not the same as my mobile phone, which does become e-waste as application demands on older phone hardware get overwhelming over time.
  * The random number guessing program these hyper-specialized ASICs run is an open standard from before Bitcoin’s genesis – called the SHA2 standard. The actual program specification of this program is well known, and long before Bitcoin was born, people have been optimizing its execution in both software and hardware. After Bitcoin got popular, another wave of optimizations happened, and some optimizations are happening even now. But there is a limit to these optimizations – both from software and hardware angles.
    * Software: the functional specification is well known, and we have only so many things we can do with for-loops, additions, and multiplication. The low-hanging fruits are all long gone.
    * Hardware: Hardware optimization will eventually hit physical limits. Transistors placed close enough to each other will start doing unexpected things that only quantum physicists can understand.
  * As optimizations end, mines will seek electricity at lower prices. There are many more ways of optimizing electricity production than optimizing the SHA256 function. Finding cheap sources of power or even creating new sources of cheap power is where the next optimization is. Note that cheap is not always green.



Some have argued that miners in Bitcoin serve the same purpose as gold miners. I think it’s not the same. Gold miners can all go away tomorrow, and gold will continue to be what it is. If all Bitcoin miners are gone tomorrow, transactions will stop. Bitcoin’s protocol pays its miners because they have to exist – forever. As we saw earlier, it’s a thin-margin business, where technology will almost certainly be commoditized – as the specifications are set in stone. At this thin margin, cheap electricity is their only competitive advantage. As their margins drop, hopefully 51% or more miners will function honestly, and transactions will keep flowing.

Will Bitcoin deprecate gold? I hope the answer is a no, but I am afraid the answer will be a yes.
