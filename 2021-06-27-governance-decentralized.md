---
title: "Governance, Decentralized"
date: 2021-06-27
source: https://tejaswin.com/2021/06/27/governance-decentralized/
---

Define  _Governance_ : the act or process of governing or overseeing the control and direction of something (such as a country or an organization).

In this article, I will focus on whether any organization can have decentralized governance, and what does that even mean? And how is this related to cryptocurrencies. Let’s start with a very basic organization, and see whether it can be governed in a decentralized way.

### What is an organization anyway?

Say some people want to pool their money and use it for charity. We have ourselves a rudimentary organization. During the organization’s inception, the founders make some bylaws – for example: for any charitable donation to happen, say 2/3rd of the remaining capital in the pool has to approve it. These bylaws are written down formally in a “human language” (the language being a “human language” is important). The organization will register itself with the government of that geographical area (let’s say, a country). In case disputes arise in the future, the courts of that country will interpret the bylaws of the organization, apply the relevant common laws of that country, and with the threat of force, ask the members of the organization to abide by the court’s judgment. We kind of get how this works.

I will call this “centralized governance”, because the dispute resolution is adjudicated by a centralized authority. In an ideal world, this centralized authority is fairly appointed by representatives of the people who were fairly elected by the people to carry out such appointments.

### Enter Smart Contracts

If the bylaws were precisely written down in an unambiguous computer language, and deployed on a distributed computer that could not be stopped, or taken over by any single authority – we have a decentralized organization. Its governance is encoded in the program that was deployed on the distributed computer. Ideally, once deployed, the program cannot be changed, and can be arbitrarily run by anyone forever. Who are the members of this organization? Let’s say the program has a function that accepts money as input, and gives out an equivalent valued token – anyone who makes such a function call is a member of this organization, as they have a stake in the program. Do disputes arise in such an organization? No. To see why the answer is “no”, we have to understand that this system adheres to the maxim: “Code is Law”. The program does exactly what it was programmed to do – there is no randomness or discretion or uncertainty in the execution. This faithful execution of the program obsoletes the idea of dispute resolution.

Ethereum smart contracts are such programs. They are deployed and run on Ethereum, which is a distributed network of computers that ideally cannot be censored or stopped. Ethereum has a richer programming language, along with the notion of a smart contract having monetary deposits, and other arbitrary data. Using this setup, one can write a smart contract that represents the charitable organization that we saw earlier. In fact, back in 2016, when Ethereum was still in its infancy, exactly such an organization was deployed as a smart contract on it. It was called The DAO, or the decentralized autonomous organization. It could accept funds from anyone, and with token holders voting for projects, would fund these projects from the collective pool of funds. Venture capitalists thought that the DAO would disrupt the VC industry itself, and added their own funds into the pool. At its peak, the DAO had 14% of all of ETH pooled inside it (ETH is the native currency of the Ethereum system). I didn’t read the code of the DAO, and am not sure how a project got actual funding – was some ETH moved to the recipient’s address? How would the DAO verify that the recipient actually produced something of value, if that artifact was not native to the blockchain itself? In the cryptocurrency space, it’s important to ask these questions – as the answers are not obvious, and often times hide red flags that indicate possible scams.

But as it turned out, this DAO program itself had a software bug, and that allowed a clever hacker to drain the uninvested funds into their own control. To “fix” this “hack”, people who had enough social clout in the Ethereum ecosystem managed to undo history, and start an alternate timeline where this hack never happened.

What?!?!

How does one undo history and make alternate timelines?

### It’s the settlement assurances, stupid[1]Read more here: https://medium.com/@nic__carter/its-the-settlement-assurances-stupid-5dcd1c3f4e41

Let’s start with an example. Let’s say your credit card is stolen, and is used to buy strange things in strange lands. You call your credit card issuer and ask them to undo history, and start an alternate timeline where the theft never happened, and you have a clean slate of your own previous transactions and new transactions. Where did the thief’s transactions go? Turns out that they were never “settled”. In the traditional finance world, very very few transactions are actually “fully settled”. Transactions between countries, or between large banks, or those that are brokered by central banks are considered settled for good, and are truly irreversible. The rest of the world’s transactions can be reversed, if the right people are convinced.

In Ethereum, where code is supposed to be law – alternate timelines should not have been possible. The hacker took out the pooled funds from the DAO because the smart contract allowed that to happen. That’s the bylaws of the contract, and the hacker is playing by the rules. There shouldn’t be a discretionary voice that says “But that’s not the spirit of the law”. Smart contracts are only supposed to respect the word of the law, and not the spirit of the law. Ethereum, in its early days at least, believed that the spirit of the law mattered more than the word of the law, and allowed the DAO hack to be “bailed out”.

Ethereum is just one such “network computer” (blockchain, to keep up with the times) that runs such code-is-law smart contracts. There are other blockchains that claim to do the same, and have varying degrees of centralization that allows the powers-that-be to “bail out” certain contracts if shit his the fan. On the other hand, Bitcoin doesn’t even allow such powerful smart contracts, and the rudimentary smart contracts that it does allow, have never been reversed because some people lost their money. I think it’s an important distinction that makes Bitcoin the most (if not the only) credible blockchain in existence, but that’s just me.

### Governance, through code

Coming back to Ethereum smart contracts which act as decentralized autonomous organizations, how can governance rules be changed if all token holders agree to it? We now get into some of the more sophisticated governance models for smart contracts, which can all be coded into the initial smart contract itself. Here’s one popular model:

In our original charity smart contract, we had the initial bylaw that 2/3rds of the total pool had to approve every new donation. Let’s say we want to change this rule to have 3/4 instead of 2/3. While writing the initial smart contract, this particular constant (2/3) is delegated to a different smart contract that is deployed first, and the main smart contract calls this other smart contract to perform it’s actions. In software programming, this is either called “delegation” or “forwarding” or “a pimpl – pointer to an implementation”. The difference between a classic software program that does this, vs. a smart contract that does the same thing – is that in a smart contract with decentralized governance, the change in implementation of a functionality has to be voted by token holders. This is how it looks:

  1. The initial smart contract is written in such a way that the following steps are supported.
  2. Someone (doesn’t matter who) codes a new piece of functionality and deploys it on the blockchain. For now, this is dead code, as no one is executing it. But everyone can see what it does.
  3. Someone (again, doesn’t matter who) makes a proposal in the original contract that they would want to call a vote for this new functionality from step (2) to replace the equivalent step in the original code.
  4. There is a timeline for token holders of the smart contract to vote for this proposal. Votes are tallied. The result is known.
  5. If the governance change is approved, there is an additional time window before it comes into effect. Token holders who are unhappy with this change can withdraw their capital from the pool by returning or burning the tokens.
  6. The governance change is affected by changing the smart contract implementation of this functionality from the original to the new.



Many smart contracts on Ethereum have the so called “governance token” that allows token holders to change the rules of the smart contract if enough such token holders vote for it.

  1. Uniswap, the popular decentralized exchange on Ethereum, has its own governance token UNI, which allows UNI holders to vote for governance changes like increasing or decreasing the fee taken by the protocol per exchange trade.
  2. Compound, a smart contract for credit issuance on Ethereum, has its own governance token COMP, which allows COMP holders to affect governance changes – like how they recently voted to change their price oracle.
  3. MakerDAO, the smart contract behind the stable coin DAI, has its own governance token MKR, which allows MKR holders to change the parameters of the DAI stablecoin, and how it maintains its 1:1 peg against the USD.



In my naïve unqualified opinion, these kinds of governance tokens can sometimes pass the Howey test, and could qualify as securities under some regulatory regime.

### What’s in it for me?

Many tokens/coins are available to buy on many cryptocurrency exchanges.

  1. Some are native coins of their own blockchains – like BTC/ETH. Many of these native coins are centralized, issued to investors first, and dumped on the general public later.
  2. Some are ERC-20 tokens on the Ethereum blockchain. They represent governance rights on protocols, and thereby generate cash flow.
  3. Some are tokens on other blockchains. Most blockchains’ native currencies themselves are worth nothing. Tokens that are launched on these blockchains are even trickier.
  4. Some are even more complex tokens issued by smart contracts that govern other smart contracts.
  5. Some tokens are blatantly pointless, and are valuable just as collectibles: remember NFTs?



Some tokens have a point, but are still worth nothing.

Some tokens have a point, and might be worth something.

To keep life simple, one can just buy Bitcoin. If that’s too conservative (it’s not), maybe add ETH to the mix (don’t).

References[+]

References ↑1 | Read more here: https://medium.com/@nic__carter/its-the-settlement-assurances-stupid-5dcd1c3f4e41  
---|---
