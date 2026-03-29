---
title: "Defi for the rest of us"
date: 2021-06-07
slug: "defi-for-the-rest-of-us"
source: https://tejaswin.com/2021/06/07/defi-for-the-rest-of-us/
categories:
  - "cryptocurrencies"
---

DeFi stands for Decentralized Finance. 

Decentralized: Ideally, any single entity should not be able to stop the process or program or system in question. It’s running on some unstoppable system where anyone can execute operations.

Finance: Savings, Loans, Exchanges, Margin Trading, Synthetic Assets (Equities, for example), Lotteries, Insurance, Collateralized Debt Obligations (why not?), and such.

Before the advent of Bitcoin/Ethereum, financial products were run on a computer that some entity controlled. This entity had a physical address, and could be visited by law enforcement or regulators or more generally, whom I call “men with guns”. Bitcoin/Ethereum run on so many computers that it’s not possible for men with guns to stop it. Smart contracts running on Ethereum are hard to take physical control of – and stop, or modify unilaterally by men with guns. This is the decentralization that we are interested in. Because of this, we have “unstoppable programs”, at least in theory.

First, a simple example of where these “unstoppable programs” come in. Let’s say you want to buy some Ether. You could submit your KYC details to a centralized exchange like Coinbase or Kraken and get an account. You then wire-transfer some dollars to their bank account, with some routing instructions so that the money goes to your account. You wait for the dollars to show up in your dashboard, and then buy some Ether with it. You could let the Ether stay there (like how you let your money stay in a real world bank) or you could self-custody by transferring the Ether out to your own hardware wallet. Like you withdraw cash from a bank and self-custody under a mattress, for example. 

#### Decentralized Exchanges

Given that you could be an “under-the-mattress” type of person, Coinbase could block your account. What then? Enter DEX’es, or decentralized exchanges. Uniswap is one such DEX. It’s a set of smart contracts that run on the Ethereum network. The specific Uniswap smart contract that accepts USD and gives back Ether is located at the address 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc on the Ethereum blockchain’s “main-net”. Think of it as the unchanging IP address of the smart contract on the Internet. If you make a request to this smart contract with some USD, and it returns some Ether to your address. Think of it as making a web-search request to Google.com with a query and getting back 10 blue links as the result. But to start this process, you need to have USD in a form that the smart contract can accept. Enter Stablecoins.

#### Stablecoins

Stablecoins are tokens that 1:1-track external fiat currencies like the US Dollar or Euro, external (to the system in question) cryptocurrencies like Bitcoin. This token system is implemented as an ERC-20 token (which I explained in [my post on NFT’](<https://tejaswin.com/2021/03/28/on-nfts/>)s). Take USDC for example, which is a stablecoin that tracks the US Dollar. Every token minted by the USDC smart contract can be redeemed for $1. How do you mint a USDC token? You create an account on Coinbase, you transfer USD to it, and you buy 1 USDC for 1 USD. This 1 USDC is an ERC-20 token that can be transferred from your Coinbase account to your computer, or some other contract, or exchanged on Uniswap for something else. The 1 USD you owned earlier is now on the Ethereum blockchain in the form of 1 USDC. To redeem this 1 USDC back to 1 USD, you transfer this USDC back to your Coinbase account, and sell if for 1 USD. Note again, that there is no USD, ever, on the Ethereum blockchain. Ethereum does not know about USD at all. All it knows is USDC. Coinbase is your bridge from the real world to the ethereal world.

Coinbase is able to redeem USDC to USD because they have a traditional bank account somewhere that stores the USD that backs the USDC.

Coming back to our earlier use case: now that you have USDC on Ethereum, you can use the Uniswap contract to buy Ether with it, without going through Coinbase. But hey, we had to go to Coinbase to buy USDC. So, didn’t we just move the trusted third party from the exchange to the stablecoin issuer? We did. But do note that you can get USDC without going to Coinbase as well – it’s just an ERC-20 token that anyone can transfer to you on the Ethereum blockchain without permission from anyone else. And you can use this to exchange to any other token without anyone’s permission as well. If more and more of the economy “moves on chain”, the on and off ramps to fiat currencies like USD will become less important. But for now, someone, somewhere has to store 1 USD in a bank account to be able to generate the equivalent stablecoin “on chain”.

#### Automated Market Makers

So, how does Uniswap know the exchange rates for every token pair that it allows us to trade with? Each token-pair is run as a smart contract, where you can make function calls to swap one token for another. The smart contract also has a liquidity pool under its control which stores both the tokens in some ratio, and this ratio is used to infer the market price. The assumption is that if this ratio goes out of sync with the external market price, arbitrageurs will trade in the other direction to take tiny profits and revert the pool ratio back to reflect external market price. Users with excess liquidity in any token can fund these liquidity pools and take a small cut of each trade that hits their liquidity pool. We now have a liquidity provider who can get some yield on their capital. Notice that this system of smart contracts is not relying on any external data to be ingested into the system. The exchange rate between token is entirely set by market dynamics.

Let’s say you wanted to provide liquidity to the token pair ABC-XYZ on Uniswap, but you have neither token with you. On the other hand, you have more than enough Bitcoin that you want to HODL and not want to sell. Can we use this Bitcoin as collateral to get a loan of some ABC tokens that you can then use to fund the ABC-XYZ Uniswap pool? Enter DeFi loans.

#### Loans

In the traditional world of finance, Loans are given out to parties with good credit rating, and defaults are prevented/mitigated by a combination of social pressure of reputational damage, law enforcement, liquidation of other assets, or such. In the world of cryptocurrencies, the users have just one identity – a public key, which looks like this: 12cbQLTFMXRnSzktFkuoG3eHoMeFtpTu3S. How do you cause reputational damage to this public key? Traditional default protection ideas fail here. Most crypto-loans are, for that reason, over-collateralized. You want to borrow 100 tokens of ABC? You put up 150 ABC worth of Bitcoin as collateral, and then you take 100 ABC. As long as the smart contract can convince itself that the loan remains over-collateralized, you are good. If the value of Bitcoin goes down, you are expected to put up more collateral – or risk being liquidated. 

Why would someone borrow an amount of X by pledging a collateral of 1.5X? Well, one obvious reason is that the borrowed token is more useful than the collateral token. It could be that the borrowed token is undervalued by the market vis-à-vis the collateral token. It could be that the borrower knows that the collateral token will tank in value the next day, and wants to willfully default on the loan. It’s all possible. 

#### Hmm

What next? “TradFi” could get disrupted by “DeFi” because of how automated these smart contracts are, and how they can easily build on top of each other. Everything is an API, and API’s are open. On the other hand, men with guns could mess with the trusted third parties that, say, back stablecoins – and take down the whole system. Also, they could just run in this little corner of the general financial ecosystem, and everyone wins.

PS: Overheard on Twitter: Fish are swimming to DeFi in droves, and that’s attracting the sharks 🙂
