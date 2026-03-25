# Trust All the Way Down

Let's start with a simple question: How do you install software? When you install an app from Apple's App Store, Apple has reviewed the source code written by someone else, compiled the source code into a binary (the machine-readable instructions your device actually runs), cryptographically signed it, and shipped it to your phone. Your phone is configured to run only such software. 

You trust Apple. This works. Apple has the incentive and the resources to keep the pipeline clean. Google does the same. So does Microsoft. Your trust model is simple: delegate verification to a gatekeeper you trust.

Bitcoin, naturally, has no such gatekeeper. The software is run by everyone who participates in the network: exchanges and custodians on their servers, miners in their data centers, self-custodial users on their own laptops. Each of them independently enforces the same rules. The source code behind that software is public. You can read it yourself. Is the 21 million cap actually there? Does the four-year halving logic exist where you think it should? Does the cryptographic verification of signatures follow the standards? What about Proof of Work? All of these are in human-readable source code that anyone can inspect. But source code is not what these myriad participants run. A set of tools (compilers, linkers, libraries, collectively called the "build toolchain") converts source code into an executable binary. The binary is what actually runs on mobile phones, laptops, mining-pools, exchanges and custodians, etc. 

And here is the uncomfortable question: if you verified the source code, can you trust the binary? Does the binary do what the source says it does?

Not really. The toolchain that compiled your binary could change it in subtle ways. Even if every line of source code is clean, the binary on your machine might do something the source code doesn't say. A compromised binary doesn't just steal one person's coins. It can redefine the rules themselves. Alter the supply cap. Change the halving schedule. Weaken signature verification. Accept transactions that should be invalid. And if enough nodes in the Bitcoin network run that binary, the altered rules don't produce an error. They *become Bitcoin*. 

So: when you download and run a Bitcoin node, how do you know it does what the source code says? Do you trust the toolchain? Even if you didn't build the binary, do you trust the toolchain of the person who built it? Even Bitcoin.org - has anyone audited their toolchain?

For most of computing's history, the honest answer has been: No, you don't know if the software you run is what you think you are running. And yes, you trust the toolchain. And for most software, that's rational. For Bitcoin, it's a contradiction. A system built to eliminate trust, running on a foundation of trust.

This is the story of how a small group of engineers decided to fix that contradiction, how far they've gotten, and why almost nobody else is trying.

---

# The Problem Is Forty Years Old

In 1984, Ken Thompson received the Turing Award (computing's Nobel Prize, roughly) for co-creating Unix and the language Unix was written in: C. In his acceptance speech, after all the customary thank-yous were done with, he went on to describe a possible attack that he could have engineered into the C compiler that possibly could never have any defense. See this [Numberphile Video](https://www.youtube.com/watch?v=SJ7lOus1FzQ) for an animated discussion. The attack is subtle. It took me a while to understand it. I recommend reading his [original paper](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf) that accompanied the lecture. I will attempt a crude explanation anyway.

A compiler is a program that translates human-readable source code into machine-executable binaries. Most compilers are programs themselves and have their own source code, which itself needs to be compiled. The C compiler itself is written in C. To compile, say, the 2026 version of the C compiler source code, you use the 2024 C binary. The 2024 binary was compiled from the 2024 source code using some earlier binary from the 2010s. And so on, all the way back to Ken Thompson himself, who compiled the original C binary using a binary of another primitive language called B. If you go even more into history, you will eventually get a hand-assembled proto compiler-compiler called TMG whose binary code was hand-built by Doug McIlroy. 

Thompson's proposed attack is devious. He says his original C binary was mostly normal, except for one malicious addition. This addition had two jobs. First, it waits for anyone compiling the Unix operating system and compromises the Unix operating system to accept a secret password, letting Thompson log in as any user. So, Unix, if built by this particular C binary, is compromised. Second, Thompson's C binary waited for anyone compiling a new version of the C compiler itself and injected a copy of the entire malicious package into the resulting binary. A self-perpetuating virus: one part does the damage, the other part ensures its own survival by propagating itself. As Thompson built the first binary, everyone who built the C Binary ever again has to have used his binary to start with. And of course, all major programming languages eventually can trace their way back to the original C binary that Thompson created. 

Here is the problem. The source code of your own C compiler never contains this malicious addition. You take clean 2026 source code, compile it with the 2024 binary, and the 2024 binary injects this malicious payload (and the payload injector) into your fresh 2026 binary. You cannot escape it because every C Binary you use to build your own C binary, or any other software for that matter - could be compromised. You compile Bitcoin's source code with this 2026 binary and the Bitcoin binary could come out compromised. You compile other programs and they're fine. The compromised compiler is selective: it targets only Bitcoin and future versions of itself. Everything else compiles clean.

You could audit every line of compiler source code. You'd find nothing. The corruption lives in the binary, not the source, and it has lived there since Thompson's original compilation, propagating silently through every generation.

Thompson's conclusion was blunt: "You can't trust code that you did not totally create yourself (by hand)." He meant it all the way down the toolchain.

---

# If Ken Thompson Ran ASML

Thompson's argument can feel abstract. Source code, compilers, binaries. Let me map it onto something concrete: the semiconductor supply chain.

ASML, a Dutch company, builds the extreme lithography machines used by TSMC to make GPU's for NVIDIA. Suppose ASML decided to compromise this chain. Say ASML's lithography machines detect when TSMC is specifically fabricating an NVIDIA GPU. For every other customer's designs, the machines work flawlessly. But when they recognize NVIDIA's patterns, they introduce a subtle alteration in the silicon. The resulting GPU performs perfectly on every benchmark, except when running one specific application (say, ChatGPT). Every other workload: perfect. Every other customer's chips - even more perfect. This is the attack part of the attack.

Now the self-reproducing part. Suppose ASML's machines could also be used to build new ASML lithography machines (not true in real life, but go with it). ASML rigs its machines to recognize when someone is building *new lithography equipment* and compromises those too, along with the targeted NVIDIA alteration as well. It's a recursive attack, in a sense.

---

# This Is Not Theoretical

Thompson's attack was a thought experiment. He never actually deployed it. But the JavaScript ecosystem, which powers most cryptocurrency wallets and web interfaces, has been a live testing ground for exactly this kind of supply chain compromise.

In 2018, a developer named Dominic Tarr handed over maintenance of a popular NPM package called `event-stream` to a volunteer. The volunteer made a few benign commits over five days to build trust, then injected a malicious dependency called `flatmap-stream`. The payload was encrypted and selective: it activated only when it detected it was being built inside BitPay's Copay wallet. It checked Bitcoin and Bitcoin Cash balances, and if the wallet held more than 100 BTC or 1,000 BCH, it harvested the private keys and sent them to a remote server. The attack shipped to end users in Copay versions 5.0.2 through 5.1.0. It went undetected for two months.

In December 2023, a former Ledger employee's NPM account was compromised via a phishing attack that captured their session token, bypassing two-factor authentication. The attacker pushed malicious versions of Ledger's `connect-kit` library. Because wallet frontends loaded this library at runtime from a CDN without pinning a specific version, the malicious code was automatically served to over a hundred decentralized applications, including SushiSwap. For about five hours, anyone clicking "Connect Wallet" on an affected site was shown a fake overlay that, if interacted with, drained their wallet. Roughly $600,000 was stolen before Ledger deployed a fix.

Neither of these was a Thompson-style compiler attack. They were simpler: one exploited trust in a maintainer, the other exploited a stale employee account. But they demonstrate the principle. The code you audit is not always the code that runs. And in crypto, the consequences are immediate and irreversible.

Bitcoin Core's engineering culture watches these incidents carefully. They are, in a sense, the reason the Guix effort exists.

---

# Bitcoin Lived With This Problem for a Decade

How does Bitcoin.org compile its binaries? For years, Bitcoin Core used a system called Gitian to produce release binaries. Multiple developers compiled the same source code inside identical virtual machines and compared results. If everyone got the same binary, no single developer had tampered with the output. This is called a *reproducible build*, and it was genuinely better than how most normal software ships (a developer compiles on their laptop, uploads, and you trust them). In this case, we trust the toolchain - but we make sure that a quorum of developers ran the said toolchain on different machines in different physical locations. 

But Gitian relied on Ubuntu Linux: Ubuntu's compiler, linker, and standard libraries. The untrustworthy toolchain, so so speak. The total set of trusted binaries, software that everyone simply assumed was honest, was approximately 550 megabytes. Half a gigabyte of machine code that nobody had audited from scratch, supplied by Canonical, who received it from upstream GNU and Linux projects, who compiled it using previous versions of their own tools, who received those from...

550 megabytes of "just trust us." For a system whose entire reason for existing is to not trust.

---

# From 550 Megabytes to 357 Bytes

In 2019, a Bitcoin Core developer named Carl Dong opened Pull Request #15277 on GitHub. Unassuming title: "contrib: Enable building in Guix containers." But one line in the description stood out:

> "If OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler)."

Someone was claiming, in a pull request for a trillion-dollar financial system, that someday the entire trust surface could be reduced to 500 hand-assembled bytes.

Guix (pronounced "geeks") is a package manager that, unlike conventional ones, can build every package from source, starting from a defined set of bootstrap binaries. The move from Gitian to Guix took years. Cross-compilation for five architectures plus macOS and Windows, all from a sealed environment with no network access, every dependency explicitly declared. No sneaking in a package at build time.

The conceptual shift mattered more than the technical one. Gitian asked: "Did multiple people get the same result?" Guix asks: "Can we account for every binary in the build chain as well?" It's the difference between checking that five people agree on the answer, and checking that the textbook they all read wasn't wrong.

Bitcoin Core v22.0, released in September 2021, was the first version built with Guix. The trusted binary surface dropped from 550 MB to approximately 120 MB. A 78% reduction in code you have to take on faith. Nobody outside of Bitcoin Core's development community really noticed.

But 120 MB was still 120 MB. Carl Dong's PR pointed toward something more radical.

The bootstrappable builds project (bootstrappable.org) starts from a simple premise: compilers written in their own language create an infinite regression of trust. Their goal is to break the regression by starting from something small enough to audit completely by hand.

They have a nice domestic analogy. To make yogurt, the first step is to add yogurt to milk. Where does the first yogurt come from?

Their answer is hex0. A program, 357 bytes long, written in raw hexadecimal. Each pair of hex characters maps directly to a single processor instruction. No compiler. No abstraction. A human can sit down, read the hex, look up each instruction in the manual, and verify, by hand, that it does one thing: read hex-encoded text and output the corresponding binary.

The yogurt that doesn't require yogurt.

From hex0, the chain proceeds through twenty-eight stages. Each builds a slightly more capable tool using only the tools from previous stages:

**Stages 0-5: From nothing to C.** hex0 rebuilds itself from its own source (verifying the seed). Labels and jumps. Addresses. A minimal assembler. A rudimentary C compiler. Then M2-Planet, a more capable one. We just went from 357 bytes of hand-verified hex to a working C compiler.

**Stages 6-10: Bootstrapping the bootstrapper.** Earlier tools rebuilt with improved compilers, gaining cross-platform support. The hex assembler from stage 1 gets rebuilt in C. Each stage replaces trust with verification.

**Stages 11-28: The scaffolding.** A shell, a hash function, basic utilities. Everything needed for a real build environment. At the end: GNU Mes, a mutually self-hosting Scheme interpreter and C compiler. Mes builds TinyCC. TinyCC builds vintage GCC. Vintage GCC builds modern GCC. Modern GCC builds Bitcoin Core.

| Era | Trusted binary surface |
|---|---|
| Gitian (pre-2021) | ~550 MB |
| Guix (Bitcoin Core v22.0, 2021) | ~120 MB |
| Full bootstrap from hex0 (target) | 357 bytes |

That last row represents a 99.999935% reduction in code taken on faith. From half a gigabyte to something shorter than a tweet.

The honest caveat: as of early 2026, the full bootstrap from hex0 is merged into Guix itself, but Guile (the Scheme interpreter orchestrating the build) is still about 25 megabytes of trusted binary. Work to bootstrap Guile is ongoing. Bitcoin Core's current Guix builds start from Guix's present bootstrap set, not directly from hex0. Hardware (Intel ME, AMD PSP, RNG) remains a separate trust surface entirely.

But the path is mapped. The hardest parts are done. And no other software project of comparable importance is further along this road. Ethereum's most popular client, Geth, has had open issues requesting reproducible builds since 2018. Unresolved. Solana ran a single client implementation with no reproducible builds until late 2025. Traditional finance is entirely closed-source. The question isn't even asked.

Most haven't set foot on this road. Most haven't found the trailhead.

---

# 357

The engineers doing this work will never be publicly recognized. They're not building features that make headlines. Not launching tokens. Not raising venture capital. They're arguing about linker flags and debating whether 25 megabytes of trusted binary is 25 megabytes too many.

When a nation adds Bitcoin to its reserves, it's trusting the binary. When an institution evaluates Bitcoin's monetary policy (fixed supply, halving schedule, 21 million cap), it's evaluating properties described in the source code. Whether the running software faithfully implements that source code is a separate question. It's the question Guix answers.

A sovereign wealth fund holding Bitcoin without understanding its software supply chain is like a central bank storing gold without assaying it. You might have what you think you have.

Twenty-eight stages. From a seed smaller than a tweet to a financial system for billions. This is what it looks like when the people building a system actually believe it matters.

357 bytes. That's where it starts.
