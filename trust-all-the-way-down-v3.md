# 357 Bytes of Certainty: Bitcoin's Quiet Revolution in Software Integrity

When a sovereign wealth fund buys gold, it assays the bars. No serious institution would skip this step. The gold might look right, weigh right, and come from a reputable dealer. But trust is not verification, and the difference matters when billions are at stake. Assaying is not simple. There are destructive and non-destructive ways of assaying gold. X-Ray Fluorescence (XRF) and ultrasonic testing do it quickly to see if there are other heavy metals like tungsten inside. But the gold standard of testing gold is the "Fire Assay", a destructive 3,000-year-old process where a small sample of the gold is melted with lead and silver to chemically separate every trace of impurity, leaving only a pure bead of gold. 

An unasked question is - do we trust the assaying machines? Where do they come from? Most institutions and central banks do not disclose their assaying "supply-chain", given the high stakes involved. 

When a nation adds Bitcoin to its reserves, what is it assaying?

Not the blockchain. The blockchain is just raw data, inert without software to interpret it. Digitally signed transactions are the same, just blobs of data. What the nation is actually trusting is the software they run. In technical terms, they are trusting the *binary*: the compiled software running on its servers (or its custodian's servers). And the integrity of that binary depends on the integrity of every tool that participated in producing it, starting all the way from the human-readable source code. Unlike gold, Bitcoin's "assaying machine" is open source software, where the software supply chain is impossible to hide. Therefore, possible to compromise.

---

## The Rules Everyone Thinks They Can Verify

Bitcoin's source code is public. Anyone can read it. They can look for the 21M supply-cap, the four-year halving, cryptographic verification of signatures, and proof of work. They all do exist. This software is run by everyone who participates in the network: exchanges and custodians on their servers, miners in their data centers, self-custodial users on their own laptops. Each of them independently enforces the same rules.

But source code is not what these participants run. A set of tools (compilers, linkers, libraries, collectively called the "build toolchain") converts source code into an executable binary. The binary is what actually runs. And here is the uncomfortable question: if you verified the source code, can you trust the binary?

Not reliably. The toolchain that compiled your binary could change it in subtle ways. Even if every line of source code is clean, the binary on your machine might do something the source code doesn't say.

For most software, this doesn't matter. But Bitcoin is not most software. A compromised binary doesn't just steal one person's coins. It can redefine the rules themselves: alter the supply cap, change the halving schedule, weaken signature verification, accept transactions that should be invalid. And if enough nodes run that binary, the altered rules don't produce an error. They *become Bitcoin*. The software is the spec. There is no court of appeal.

---

## The Attacks Are Real and Accelerating

This is not a theoretical concern. Software supply chain attacks have been around and increasing in complexity and scope: each new attack bypasses the defenses that the previous one prompted.

**2018: The Copay Wallet Attack.** A developer [handed over maintenance](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) of a popular JavaScript package called `event-stream` to a "volunteer". The "volunteer" earned trust through a few benign contributions. Later, they injected a malicious dependency into this generic library. The payload was encrypted and selective: it activated only when it detected it was being used by BitPay's Copay wallet. It checked Bitcoin and Bitcoin Cash balances, and if the wallet held more than 100 BTC or 1,000 BCH, it harvested the private keys and sent them to a remote server. The attack went undetected for two months. The general response was to audit your dependencies a bit more thoroughly. 

**2023: The Ledger Connect Kit Attack.** A former Ledger employee's developer account was [compromised via phishing](https://www.ledger.com/blog/security-incident-report), bypassing two-factor authentication. The attacker pushed malicious versions of Ledger's wallet connection library. Because over a hundred decentralized applications loaded this library at runtime without pinning a specific version, the malicious code was automatically served to every user who clicked "Connect Wallet" on affected sites, including SushiSwap. Roughly $600,000 was [drained](https://www.ledger.com/blog/security-incident-report) in under five hours. People knew that the dependency was good, but the *latest version* of the same dependency was compromised. The industry's response: pin your dependency versions to those you know are good.

**2026: The LiteLLM Attack.** A few weeks ago, a threat group called TeamPCP [executed a cascading attack](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign) that went one level deeper. They first compromised Trivy, a widely-used security scanner. When LiteLLM's build pipeline ran the compromised Trivy (the tool that was supposed to *protect* the build), it [exfiltrated LiteLLM's publishing credentials](https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer). The attackers then pushed malicious versions of `litellm`, a package with roughly three million daily downloads that is [present in 36% of cloud environments](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign). The payload harvested API keys, SSH keys, cloud credentials, and cryptocurrency wallets, and installed a persistent backdoor. The packages were live for about three hours before being quarantined. The industry's emerging response is to treat supply chain attacks as the default threat model and not an edge case.

**2026: The Axios Attack.** A few days ago, suspected North Korean state hackers [compromised the NPM account](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) of a maintainer of Axios, the most popular JavaScript HTTP library with over [100 million weekly downloads](https://www.helpnetsecurity.com/2026/03/31/axios-npm-backdoored-supply-chain-attack/). They changed the account's email to an attacker-controlled address, then injected a malicious dependency that silently deploys a dropper targeting cryptocurrency wallets. Google [attributed](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html) the attack to UNC1069, a North Korean group that funds the regime's nuclear and missile programs with stolen crypto. Axios is used by virtually every JavaScript project on the internet. The industry's response is still unfolding.

Notice the progression. In 2018, a library was compromised by an opportunistic individual. In 2023, an employee account was hijacked through phishing. In early 2026, the security scanner itself was the attack vector. In late March 2026, a nation-state compromised the single most widely used JavaScript library on earth. Each time, the industry adds another layer of checking. Each time, attackers find a way to compromise the checker.

In 1984, Ken Thompson explained why this regression has no bottom.

---

## The Deepest Version of This Problem

Thompson received the Turing Award, computing's highest honor, for co-creating Unix. His [acceptance lecture](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf) described an attack that, four decades later, we still have no complete defense against: a compiler that inserts a backdoor into the software it compiles, and also inserts the backdoor-insertion code into any new compiler compiled from clean source code. A "corruption-inserter" is inserted into the binary and can perpetuate forever. You can audit every line of your source code, your supply chain, and the tools used to build your supply chain and still find nothing. 

Thompson's conclusion: "You can't trust code that you did not totally create yourself." He meant it all the way down the toolchain.

What makes this attack devastating is its invisibility. The corruption lives in the compiled binary, not in any source code. Every future version of the compiler, built from perfectly clean source, inherits the corruption from the binary that compiled it. The "corruption-inserter" reproduces itself through the act of compilation, living in the space between what humans write and what machines execute. 

The Copay, Ledger, LiteLLM, and Axios attacks are crude by comparison: they compromise libraries and accounts, not the compiler itself. But they demonstrate the principle at progressively deeper levels. And the industry's standard defenses (dependency auditing, version pinning, credential rotation, security scanning) are all variations of adding another tool to check the previous tool. Thompson showed that this chain of checkers has no natural terminus. Who checks the checker that checks the checker?

Bitcoin Core's answer: you build the checker from scratch, starting from something small enough for a human to verify by hand.

---

## From 550 Megabytes to 357 Bytes

For years, Bitcoin Core used a system called Gitian to produce release binaries. Multiple developers compiled the same source code inside identical virtual machines and compared results. If everyone got the same binary, no single developer had tampered with the output. This is called a *reproducible build*, and it is genuinely better than how most software ships.

But Gitian relied on Ubuntu Linux's compiler, linker, and standard libraries. The total set of binaries that everyone simply assumed was honest: approximately 550 megabytes of machine code that nobody had audited from scratch.

550 megabytes of "just trust us." For a system whose entire reason for existing is to not trust.

In 2019, a Bitcoin Core developer named Carl Dong opened [Pull Request #15277](https://github.com/bitcoin/bitcoin/pull/15277) on GitHub. One line in the description stood out:

> "..., we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler)."

Guix (pronounced "geeks") is a package manager that, unlike conventional ones, can build every package from source, starting from a defined set of bootstrap binaries. The move from Gitian to Guix took years. In Gitian, if you needed a compiler, you downloaded a 200MB binary of GCC from Ubuntu. In Guix, pre-compiled binaries are forbidden. Developers had to map out the ancestry of every single tool. If you wanted a C++ compiler, you had to define how a small seed builds an assembler, which builds a C compiler, which eventually builds the C++ compiler. If you didn't explicitly declare a dependency, the build fails. For years, the Bitcoin Core team hunted down "leaks" where the software was accidentally relying on the host operating system.

Bitcoin Core [v22.0](https://bitcoincore.org/en/releases/22.0/), released in September 2021, was the first version built with Guix. The trusted binary surface dropped from 550 MB to approximately 120 MB: a 78% reduction in unaudited attack surface.

But 120 MB was still 120 MB. Carl Dong's PR pointed toward something more radical.

The [bootstrappable builds project](https://bootstrappable.org) starts from a simple premise: compilers written in their own language create an infinite regression of trust. Their goal is to break the regression by starting from something small enough to audit completely by hand. Their answer is [hex0](https://bootstrappable.org/projects/mes.html): a program just 357 bytes long, written in raw hexadecimal. Each pair of hex characters maps directly to a single processor instruction. No compiler. No abstraction. A human can sit down, read the hex, look up each instruction in the manual, and verify that it does one thing: read hex-encoded text and output the corresponding binary.

From hex0, the chain proceeds through twenty-eight stages. Each stage builds a slightly more capable tool using only the tools from previous stages:

| Stage | What it builds | Significance |
|---|---|---|
| 0 | hex0 rebuilds itself | Verifies the 357-byte seed |
| 1-3 | Assemblers with labels, jumps, addresses | Basic machine code tools |
| 4-5 | M2-Planet (a C compiler) | From raw hex to a working C compiler |
| 6-10 | Earlier tools rebuilt in C | Cross-platform support |
| 11-28 | Shell, utilities, GNU Mes | Full build environment |
| Final | TinyCC, then vintage GCC, then modern GCC | Can compile Bitcoin Core |

The progression is worth pausing on. Stage 0 starts with 357 bytes that a human verified by hand. By stage 5, those bytes have bootstrapped a working C compiler. By stage 28, you have a complete build environment. From there, TinyCC (a small C compiler) builds a vintage version of GCC from 2001. That vintage GCC builds a modern GCC. And modern GCC builds Bitcoin Core. Every link in the chain is open, deterministic, and reproducible. No binary is taken on faith.

| Era | Trusted binary surface |
|---|---|
| Gitian (pre-2021) | ~550 MB |
| Guix (Bitcoin Core v22.0, 2021) | ~120 MB |
| Full bootstrap from hex0 (target) | 357 bytes |

That last row represents a [99.999935% reduction](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) in unaudited code. From half a gigabyte to something shorter than a tweet.

The honest caveat: as of early 2026, the full bootstrap from hex0 is merged into Guix itself, but Guile (the Scheme interpreter orchestrating the Guix build process) is still about 25 megabytes of trusted binary. Bitcoin Core's current Guix builds start from Guix's present bootstrap set, not directly from hex0. The 357-byte target is not yet reached.

The remaining hurdles are real. Guile requires a C compiler that supports C99, which means bootstrapping through several intermediate compiler versions. GCC post-4.8 requires C++, and glibc (the core C library) post-2.28 requires Python, each creating new bootstrapping dependencies that must themselves be bootstrapped. These are engineering challenges, not theoretical ones, and the bootstrappable builds community is actively working through them. A reasonable estimate is that the full hex0-to-Bitcoin-Core chain could be complete within a few years. The path is mapped and the hardest parts are done.

---

## Who else is doing this?

How does Bitcoin's approach compare to the rest of the industry?

| Project | Reproducible Builds | Bootstrappable Builds | Status |
|---|---|---|---|
| **Bitcoin Core** | Yes (since 2021) | In progress (Guix + hex0 path) | Most advanced of any comparable project |
| **Ethereum (Geth)** | No | No | [Open issue since 2018](https://github.com/ethereum/go-ethereum/issues/18292), unresolved |
| **Solana** | No (validator) | No | Single client until [late 2024](https://www.theblock.co/post/382411/jump-cryptos-firedancer-hits-solana-mainnet-as-the-network-aims-to-unlock-1-million-tps); no reproducible builds for validators |
| **Traditional Finance** | Unknown | Unknown | Entirely closed-source; the question is not asked |

Ethereum took a different approach: client diversity. Multiple independent implementations (Geth, Nethermind, Besu, Lighthouse, Prysm) ensure that a bug in one client doesn't bring down the whole network. This is valuable, but it solves a different problem. Client diversity protects against implementation bugs. It does not address whether any given binary matches its source code. Geth, which runs on roughly half of all Ethereum execution-layer nodes, has had an open issue requesting reproducible builds since 2018.

Solana's second client still uses the first client's core engine. And the first client does not have reproducible builds, as far as we know.

The LiteLLM attack is instructive here, when you look at other software. LiteLLM's developers presumably audited their dependencies. They ran a security scanner. The scanner was the attack vector. Every defense the industry considers best practice was in place and was bypassed. The standard response (pin versions, scan dependencies, rotate credentials) is necessary but insufficient. It is the equivalent of adding more locks to a door while the attacker is coming through the wall.

Bitcoin Core's Guix builds don't just add more locks. They rebuild the wall from raw materials, starting from 357 bytes that a human can verify by hand.

---

## What This Means for Institutions

"Digital Money" is not an ethereal thing that exists in a vacuum. Everything digital is eventually data and software to read and interpret the data. With a "Digital Bearer Asset" like Bitcoin, where transaction finality is established only by software and there is no other legal recourse, the integrity of that software is not a nice-to-have; it is the foundation. Even if the source code is 100% correct, its compiled version is always opaque. 

As we said in the introduction, a sovereign wealth fund accepting Bitcoin using "standard software" without understanding its software supply chain is like a central bank assaying gold using a machine that was ordered online with a credit card. They cannot be sure where that machine was made, what components were used, how it was shipped to their warehouse, and such. The supply chain can be compromised, and it often is. For gold, banks rely on secrecy and the justice system. Bitcoin doesn't have that. But it has its own armour against supply chain attacks. The "assaying guarantees" are given by the Bitcoin binary, and the binary is guaranteed by the source code and the toolchain that built it in the most transparent way possible, thereby reducing software supply chain attack risks to the minimum. And hopefully, zero in the near future. 

---

## What Can We Learn from Bitcoin?

Bitcoin's approach to software integrity is not just relevant to Bitcoin. The LiteLLM attack hit cloud infrastructure. The Copay attack hit financial software. The Ledger attack hit hardware wallet interfaces. The Axios attack's blast radius is too huge to write a flippant quip about it. Software supply chain compromises are not a crypto problem; they are a software problem. Any organization running mission-critical software should be asking the same questions Bitcoin Core asked a decade ago.

Three takeaways:

**1. Reproducible builds should be the minimum standard for critical software.** If two people cannot compile the same source code and get the identical binary, there is no way to verify that the binary matches the source. Most financial, healthcare, and government software does not meet this bar. Bitcoin Core has met it since 2021.

**2. Dependency supply chains are attack surfaces, not just convenience.** Every library, every build tool, every update mechanism is a potential vector. The progression from Copay to LiteLLM shows that attackers are moving deeper into the toolchain with each generation. Pinning versions and auditing dependencies is necessary but not sufficient. Organizations should ask: how many layers of unaudited software sit between our source code and our running binary?

**3. The question "who built this binary?" should be part of institutional due diligence.** For any software that handles money, personal data, or critical infrastructure, the provenance of the binary is as important as the quality of the source code. Bitcoin Core is the only major project that has taken this question to its logical conclusion. The rest of the industry has barely started asking it. Understandably so; it is the hardest of the three questions. 

While the digital sovereignty debate is omnipresent, a more fundamental question goes unasked: have you verified the integrity of the mission-critical software running in your organization?

357 bytes. That's where it starts.
