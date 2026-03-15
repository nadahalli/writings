---
title: "Bitcoin’s Time"
date: 2022-02-25
source: https://tejaswin.com/2022/02/25/bitcoins-time/
---

No, this article is not about whether it’s Bitcoin’s moment to shine. It is a somewhat technical explainer on how Bitcoin implements time, or timestamps.

First, we need to understand why Bitcoin needs a notion of time at all. If you don’t care for this, you can directly jump to the “How” section of the article below. The “Why” section of this article is somewhat opinionated.

## Why?

Does money need timestamps? Bitcoin’s peers are a mixed bag when it comes to timestamping.

  * Physical cash typically has timestamps: both notes and coins. These are bookkeeping aids for the issuer – who wants to know how many old coins/notes are in circulation. Users don’t care for these timestamps.
  * Digital transactions brokered by centralized institutions have a timestamp on them, but those are also just for their users’ bookkeeping and serve no foundational purpose.
  * Gold is almost infinitely malleable and cannot have a physical timestamp, even if the initial miner/forger stamped a time on it. Gold receipts have timestamps, but those are either digital cash or some digital certificate going back to bullets 1 and 2.



On the other hand, Bitcoin relies on reliable timestamping for its very existence as decentralized digital money. Bitcoin will stop working if its timestamping mechanism fails. Bitcoin’s reliance on timestamps comes about because of how its difficulty adjustment mechanism works. We discussed this in a previous article on how difficulty adjustment is Bitcoin’s [secret sauce](<https://tejaswin.com/2021/07/30/bitcoins-secret-sauce/>). To recap briefly: Bitcoin’s blocks need to have somewhat accurate timestamps on them so that the entire network knows when it is time to adjust difficulty again. And to complete the feedback loop, difficulty adjustment is required to keep Bitcoin’s blocks coming approximately every 10 minutes. This fixed frequency of blocks is required to ensure that the blockchain grows at a “reasonable rate.” Reasonable in the sense that it satisfies two opposing requirements: to have enough transactions to satisfy users, but not enough transactions that users cannot store the said transaction data without overwhelming their storage.

So, each block needs to have a somewhat accurate timestamp on it – so that every two weeks, all nodes can check if difficulty was adjusted by the upcoming block. They do this by checking if 2016 blocks [1]There is a subtle off-by-1 bug here, but that doesn’t change our story. have elapsed since difficulty was adjusted.

## How?

In my opinion, timestamping is the “ugliest” part of Bitcoin’s otherwise elegant design. To be fair, distributed timestamping, especially in a permission-less peer-to-peer setting with no trusted third parties – where nodes can come and go as they please and have no identity at all – is a tough problem AFAIK, had never been solved before.

To recap how Bitcoin’s consensus works, miners aggregate transactions into blocks, and if those blocks do not conform to Bitcoin’s consensus rules, full nodes that make up the Bitcoin network reject these blocks. Full nodes are users, merchants, payment processors, peer-to-peer payment channel operators, exchanges, service providers, countries, commercial banks, central banks, what have you. Some full nodes might choose to accept blocks that others don’t accept, and that’s when we have hard-forks, and we have two versions of Bitcoin. As no one wants that, all full-nodes run the same consensus code. In reality, this mechanism is a lot more complicated, but that full nodes reject invalid blocks is essential to understanding how timestamping works.

There are two validity rules that a block’s timestamp has to follow:

  1. The blocks’s timestamp should be greater than the median of the last 11 blocks.
  2. The block’s timestamp should not be ahead of your own local node’s timestamp by 2 hours.



If the incoming block doesn’t conform to these rules, all conforming nodes discard the block, and the miner who mined this block doesn’t get his rewards as per these nodes. So, the miner has an incentive to use as accurate a timestamp as possible. The miner can use any means to figure out how to set their own local time. Still, it’s in their best interest to select a timestamp that everyone will agree with (with a two-hour tolerance window, which consensus rules allow).

On the other side of these rules, we have nodes accepting or rejecting blocks based on the block’s timestamp and their own local time (rule #2). What is the validating full node’s own local clock time? There is a delightful comment in the code, which I will reproduce here verbatim:
    
    
    /**
     * "Never go to sea with two chronometers; take one or three."
     * Our three time sources are:
     *  - System clock
     *  - Median of other nodes clocks
     *  - The user (asking the user to fix the system clock if the first two disagree)
     */

The user can also pick their own system clock as their timestamp (chronometer #1). Chronometer #2 needs some explanation. The “other nodes” refer to the peers connected to your Bitcoin node. Your clock’s local time is adjusted to add/subtract the median of the offset between these nodes’ times and your local clock time. [2]This is where things get murkier. The current code has a bug going back to Satoshi. Surprisingly, it took till 2014 to find this “bug.” Because of this bug, only the first 200 peers are … Continue reading. When your node starts, if your local clock and your peer’s clocks are apart by a significant value, you get a warning: chronometer #3 in the comment.

Due to the heterogeneity of Bitcoin nodes and the two-hour tolerance allowed by the consensus rules on the maximum block timestamp allowed, it seems to be working fine so far. This “hacky” design allows for quirks like Block X having a higher timestamp than Block X-1, which has happened a few minutes in the past. The median-of-the-last-11-blocks rule allows for some fringe [theoretical attacks](<https://bitcoin.stackexchange.com/questions/75831/what-is-time-warp-attack-and-how-does-it-work-in-general>) as well. Overall, it works because every participant has an incentive to keep their local clocks somewhat in sync with the accepted time. Blocks are valid only when enough people agree on the time. Both sets of participants have their incentives. Miners want to mine valid blocks – that’s their incentive. Nodes do not want to miss a valid block, and maybe lose track of payments made to them – that’s their incentive.

Individual nodes could keep their own clocks accurate by syncing with a central trusted authority using a protocol like NTP. Importantly though, Bitcoin doesn’t care about it. Its stance is: if you don’t set your time approximately correct, you pay the price. Up to you. [3]This mechanism is far from being proven to work and due to the above bug – is also needlessly complicated. But somehow, it seems to work – showing again that … Continue reading

References[+]

References ↑1 | There is a subtle off-by-1 bug here, but that doesn’t change our story.  
---|---  
↑2 | This is where things get murkier. The current code has a bug going back to Satoshi. Surprisingly, it took till 2014 to find this “[bug](<https://github.com/bitcoin/bitcoin/issues/4521>).” Because of this bug, only the first 200 peers are considered for time adjustment. At any point since your node starts, your node is connected to some peers – these peers come and go, and the 201st peer that your node sees doesn’t affect your node’s local clock anymore. The first 200 nodes you see – the median of their time’s offset to your time is considered while updating your local time. So, if your node runs forever and your local clock starts drifting, it could go out of sync with the network and might start rejecting valid blocks.  
↑3 | This mechanism is far from being proven to work and due to the above bug – is also needlessly complicated. But somehow, it seems to work – showing again that Bitcoin [exemplifies](<https://www.gwern.net/Bitcoin-is-Worse-is-Better>) the “worse is better” philosophy.
