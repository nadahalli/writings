# Trust All the Way Down

Most software reaches you through a chain of trust you never inspect. When you install an app from Apple's App Store, Apple has reviewed the source code, compiled it into a binary (the machine-readable instructions your device actually runs), signed it, and shipped it to your phone. You trust Apple. This works. Apple has the incentive, the resources, and the legal liability to keep the pipeline clean. Google does the same. So does Microsoft. The model is simple: delegate verification to a gatekeeper you trust.

Bitcoin, naturally, has no such gatekeeper. Bitcoin's source code is public, available in many places. You can read it yourself. Is the 21 million cap actually there? Does the four-year halving logic exist where you think it should? Does the cryptographic verification of signatures follow the standards? What about Proof of Work? All of these are in human-readable source code that anyone can inspect.

But source code is not what your machine runs. A set of tools (compilers, linkers, libraries, collectively called the "build toolchain") converts source code into an executable binary. The binary is what actually runs. And here is the uncomfortable question: if you verified the source code, can you trust the binary?

No. The toolchain that compiled your binary could alter the output. Even if every line of source code is clean, the binary on your machine might do something the source code doesn't say. For most software, this doesn't matter. The cost of compromising Chrome to steal your vacation photos exceeds the value of your vacation photos. The economics of trust work when the stakes are low. But Bitcoin is not most software. It is crucial: it guards something valuable enough that the economics of attack flip. It is distributed: it runs on thousands of machines across dozens of jurisdictions, far too many to physically inspect. And it is synchronized: every instance must agree on the same rules, because the rules are the product. If two instances of your spreadsheet disagree on how to format a column, that's a bug. If two instances of Bitcoin software disagree on whether a transaction is valid, that's a fork in a financial system securing over a trillion dollars. Bitcoin's consensus *is* whatever the software agrees on. There is no spec that exists independently of the running code. There is no court of appeal, no central authority, no "but the whitepaper says otherwise."

This is worth sitting with. A compromised binary doesn't just steal one person's coins. It can redefine the rules themselves. Alter the supply cap. Change the halving schedule. Weaken signature verification. Accept transactions that should be invalid. And if enough nodes run that binary, the altered rules don't produce an error. They *become Bitcoin*. No one notices, because there is nothing to notice against. The software is the spec.

So: when you download and run a Bitcoin node, how do you know it does what the source code says? Do you trust the toolchain?

For most of computing's history, the honest answer has been: No, you don't know if the software you run is what you think you are running. And yes, you trust the toolchain. And for most software, that's rational. For Bitcoin, it's a contradiction. A system built to eliminate trust, running on a foundation of trust.

This is the story of how a small group of engineers decided to fix that contradiction, how far they've gotten, and why almost nobody else is trying.

---

# The Problem Is Forty Years Old

In 1984, Ken Thompson received the Turing Award (computing's Nobel Prize, roughly) for co-creating Unix. His acceptance lecture was three pages long. It described an attack so elegant that four decades later, computing still has no complete defense against it.

A compiler is a program that translates human-readable source code into machine-executable binaries. Most compilers have their own source code, which itself needs to be compiled. The C compiler is written in C. To compile, say, the 2026 version of the C source code, you need the 2024 C binary. The 2024 binary was built from the 2024 source code using some earlier binary from the 2010s. And so on, all the way back to Ken Thompson himself, who wrote the original in a language called B and compiled it to produce the first C compiler binary.

Thompson's proposed attack is devious. He says his original C binary was mostly normal, except for one malicious addition. This addition had two jobs. First, it waited for anyone compiling the Unix operating system and compromised those binaries to accept a secret password, letting Thompson log in as any user. Second, it waited for anyone compiling a new version of the C compiler itself and injected a copy of the entire malicious package into the resulting binary. A self-perpetuating virus: one part does the damage, the other part ensures its own survival.

Here is the problem. The source code of your C compiler never contains this malicious addition. You take clean 2024 source code, compile it with the 2024 binary, and the 2024 binary injects the payload into your fresh 2026 binary. You compile Bitcoin's source code with this 2026 binary and the Bitcoin binary comes out compromised. You compile other programs and they're fine. The compromised compiler is selective: it targets only Bitcoin and future versions of itself. Everything else compiles clean.

You could audit every line of compiler source code. You'd find nothing. The corruption lives in the binary, not the source, and it has lived there since Thompson's original compilation, propagating silently through every generation.

Thompson's conclusion was blunt: "You can't trust code that you did not totally create yourself." He meant it all the way down the toolchain.

---

# The ASML Problem

Thompson's argument can feel abstract. Source code, compilers, binaries. Let me map it onto something concrete: the semiconductor supply chain.

ASML, a Dutch company, builds the extreme ultraviolet lithography machines that print circuits onto silicon. They're the only company on earth that makes these at the cutting edge. TSMC, in Taiwan, operates the fabrication plants that use ASML's machines to manufacture chips. NVIDIA designs the chips but manufactures nothing; they hand blueprints to TSMC.

Suppose ASML decided to compromise this chain. Not crudely, not by making all machines malfunction. Instead: ASML's machines detect when TSMC is specifically fabricating an NVIDIA GPU. For every other customer's designs, the machines work flawlessly. Every diagnostic passes. But when they recognize NVIDIA's patterns, they introduce a subtle alteration in the silicon. The resulting GPU performs perfectly on every benchmark, except when running one specific application (say, ChatGPT). Every other workload: perfect.

Now the self-reproducing part. Suppose ASML's machines could also be used to build new lithography machines (not true in real life, but go with it). ASML rigs its machines to recognize when TSMC is building *new lithography equipment* and compromises those too, along with the targeted NVIDIA alteration. Clean blueprints in, compromised machines out. You could audit ASML's designs line by line. You could walk TSMC's fabrication floor with physicists. You'd find nothing. The corruption exists only in the physical machines, and it propagates through every generation built by the compromised generation before it.

This is Thompson's attack, mapped onto atoms. How do you break out of this chain?

---

# Bitcoin Lived With This Problem for a Decade

When you run a Bitcoin node, you're trusting a compiled binary to enforce the rules of the network. The binary validates every transaction, rejects invalid blocks, determines what is and isn't legitimate Bitcoin. If the binary is compromised, your node is compromised. And because Bitcoin is synchronized, if enough binaries are compromised in the same way, the compromised rules become the network's rules. No appeal.

For years, Bitcoin Core used a system called Gitian to produce release binaries. Multiple developers compiled the same source code inside identical virtual machines and compared results. If everyone got the same binary, no single developer had tampered with the output. This is called a *reproducible build*, and it was genuinely better than how most software ships (a developer compiles on their laptop, uploads, and you trust them).

But Gitian relied on Ubuntu Linux: Ubuntu's compiler, linker, and standard libraries. The total set of trusted binaries, software that everyone simply assumed was honest, was approximately 550 megabytes. Half a gigabyte of machine code that nobody had audited from scratch, supplied by Canonical, who received it from upstream GNU and Linux projects, who compiled it using previous versions of their own tools, who received those from...

550 megabytes of "just trust us." For a system whose entire reason for existing is to not trust.

---

# From 550 Megabytes to 357 Bytes

In 2019, a Bitcoin Core developer named Carl Dong opened Pull Request #15277 on GitHub. Unassuming title: "contrib: Enable building in Guix containers." But one line in the description stood out:

> "If OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler)."

Someone was claiming, in a pull request for a trillion-dollar financial system, that someday the entire trust surface could be reduced to 500 bytes.

Guix (pronounced "geeks") is a package manager that, unlike conventional ones, can build every package from source, starting from a defined set of bootstrap binaries. The move from Gitian to Guix took years. Cross-compilation for five architectures plus macOS and Windows, all from a sealed environment with no network access, every dependency explicitly declared. No sneaking in a package at build time.

The conceptual shift mattered more than the technical one. Gitian asked: "Did multiple people get the same result?" Guix asks: "Can we account for every binary in the build chain?" It's the difference between checking that five people agree on the answer, and checking that the textbook they all read wasn't wrong.

Bitcoin Core v22.0, released in September 2021, was the first version built with Guix. The trusted binary surface dropped from 550 MB to approximately 120 MB. A 78% reduction in code you have to take on faith. Nobody outside of Bitcoin Core's development community really noticed.

But 120 MB was still 120 MB. Carl Dong's PR pointed toward something more radical.

The bootstrappable builds project (bootstrappable.org) starts from a simple premise: compilers written in their own language create an infinite regression of trust. Their goal is to break the regression by starting from something small enough to audit completely.

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
