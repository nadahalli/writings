# 357 Bytes

There is a piece of software that is 357 bytes long. That's shorter than this paragraph. It's written in raw hexadecimal, each pair of characters encoding a single machine instruction, with nothing in between. No compiler was used to produce it. A competent programmer can read the whole thing in an afternoon, look up each instruction in the processor manual, and verify, by hand, that it does exactly what it claims: take hex-encoded text in, produce a binary out. Nothing else. No network calls, no hidden logic, no surprises.

From this seed, through a chain of twenty-eight carefully orchestrated stages, you can build a complete compiler toolchain. That toolchain can then compile the entire Bitcoin Core software from source. Every intermediate step is open, deterministic, and reproducible. Anyone on earth can start from those same 357 bytes and arrive at the same result.

Why does this exist? Why would anyone build a twenty-eight-stage chain from a seed smaller than a tweet to a full-blown compiler?

To answer a question most people have never thought to ask: when you run software, how do you know it does what the source code says?

For most software, the honest answer is: you don't. You trust. You trust the developer, the build server, the compiler, the operating system, the hardware. Each layer assumes the one below it is honest. This is fine for a weather app (probably). It is less fine for a system that, as of early 2026, secures over two trillion dollars in value and is increasingly held by sovereign nations as a reserve asset.

Bitcoin's engineering culture decided, years ago, that trust is not fine. What follows is the story of what they're doing about it, why it's harder than you think, and why almost nobody else is even trying.

---

# The Problem Is Forty Years Old

In 1984, Ken Thompson received the Turing Award, computing's highest honor (the Nobel Prize of computer science, roughly), for his work co-creating the Unix operating system. His acceptance lecture was three pages long. Three. It described an attack so elegant that four decades later, the computing world still has no complete defense against it.

Thompson built his argument in stages. I'll try to do the same.

**Stage 1:** A program can contain a complete copy of itself. This is a well-known curiosity in computer science, called a quine. Write a program, run it, and it prints out its own source code. The important property isn't the self-reproduction itself, but that such a program can carry extra payload along for the ride. Think of it as a document that contains its own printing instructions, plus a hidden appendix that gets faithfully reproduced every time someone prints it. The appendix can say anything.

**Stage 2:** Compilers have a strange property. A compiler is a program that translates human-readable source code into machine-executable binaries. Most compilers are written in their own language: the C compiler is written in C, the Rust compiler is written in Rust. This creates a dependency loop. To compile the C compiler, you need... a C compiler. How does this actually work? The compiler binary "knows" things that aren't present in the current source code. It learned them from the previous version of itself, which learned them from the version before that, going back to the very first version someone compiled by hand, decades ago.

This is a deep concept, and Thompson recognized it as such. He called it "as close to a 'learning' program as I have seen." The binary carries knowledge that is invisible in the source. You simply teach the compiler once, and it remembers. Forever. Through every future generation.

Can you see where this is going?

**Stage 3:** Thompson combined stages 1 and 2. He modified the C compiler to recognize when it was compiling the Unix login program. When it detected the login source code, it inserted a backdoor: the compiled login would accept a secret password known only to Thompson, regardless of what the source code said. Anyone could log in as any user. But this alone would be easy to catch. Anyone reading the compiler's source code would see the malicious addition.

So Thompson added a second modification. The compiler now also recognized when it was compiling *a new version of itself*. When it detected its own source code, it inserted both modifications into the new compiler binary: the login backdoor, and the self-reproducing payload that re-inserts both modifications.

Then he deleted both modifications from the compiler's source code.

The source was now perfectly clean. You could read it, audit it, have it reviewed by the world's best security experts. They'd find nothing wrong. But the compiler binary, built from that clean source by the previously compromised binary, still carried both payloads. And every future compiler built from clean source would carry them too, because the compromised binary would re-insert them during compilation.

Thompson's conclusion was blunt: "You can't trust code that you did not totally create yourself. No amount of source-level verification or scrutiny will protect you from using untrusted code."

He then noted, almost casually, that the same attack works at any level: assemblers, loaders, even hardware microcode. The deeper you go, the harder the detection.

The audience applauded. Then, largely, the world moved on.

---

# The ASML Problem

I first read Thompson's paper while writing a blog post about trust in Bitcoin. The argument is airtight, but it can feel abstract. Source code, compilers, binaries, quines. These aren't things most people have intuitions about.

So let me map it onto something concrete. A supply chain that's been in the news for years, one that most readers will already have a mental model of: the semiconductor supply chain.

It has three links.

**ASML**, a Dutch company, builds the extreme ultraviolet lithography machines that print circuits onto silicon wafers. They're the only company on earth that makes these machines at the cutting edge. There is no alternative supplier. If you've read anything about "chip wars" or export controls, ASML is at the center of it.

**TSMC**, a Taiwanese company, operates the fabrication plants that use ASML's machines to actually manufacture chips. They take a chip design, feed it into ASML's lithography equipment, and produce physical silicon.

**NVIDIA** designs the chips. The blueprints. But NVIDIA doesn't manufacture anything. They hand their designs to TSMC, whose factories (equipped with ASML's machines) produce the physical GPUs that end up in data centers worldwide, running the AI workloads everyone is talking about.

ASML builds the machines. TSMC uses the machines. NVIDIA designs what the machines make. Three layers.

Now, suppose (purely as a thought experiment, I don't want ASML's lawyers calling) that ASML decided to compromise this chain.

They wouldn't do something crude like making all their machines malfunction. That'd be detected in hours. Instead, they'd make a *targeted* modification. ASML's lithography machines would be rigged to detect when TSMC is fabricating a chip from one of NVIDIA's specific GPU designs. For every other customer's designs (AMD, Apple, Qualcomm, everyone), the machines work flawlessly. Every diagnostic passes. Every quality check comes back clean.

But when the machines recognize NVIDIA's specific design patterns, they introduce a subtle alteration in the silicon.

How subtle? The resulting GPU performs perfectly on every benchmark. Renders every game without a glitch. Passes every validation test. Except when running one specific application, say, ChatGPT. Only then does it produce subtly wrong outputs. Every other workload: perfect. The corruption activates only for the one target that matters.

Three layers deep. The problem is in ASML's machines, but it only manifests in NVIDIA's GPU, and only when running a specific program. You could stare at NVIDIA's blueprints all day. You'd find nothing.

Now here's the self-reproducing part, the bit that makes it truly Thompsonian.

ASML also rigs its machines to recognize when TSMC is building *new lithography equipment*. Manufacturing equipment is itself manufactured. If TSMC decides to build the next generation of lithography machines using designs published by ASML (suppose ASML open-sourced their blueprints tomorrow), the existing compromised machines would insert the same targeted modifications into the new machines. Clean blueprints in, compromised machines out.

You could audit ASML's published designs line by line. You could walk the floor of TSMC's fabrication plants with a team of physicists. You could inspect every NVIDIA chip blueprint with a magnifying glass. You'd find nothing. The corruption exists only in the physical machines, not in any document. And it propagates through every generation of equipment built by the compromised generation before it.

This is precisely the structure of Thompson's attack.

TSMC's fabrication plant is the compiler. ASML's lithography equipment is the compiler's compiler. NVIDIA's chip design is the source code. The login backdoor is the ChatGPT-only corruption. The self-reproducing payload is the part where building new machines from clean blueprints still produces compromised machines.

Everything else compiles clean. Everything else fabricates clean. You'd never know.

How do you break out of this chain?

---

# Bitcoin Lived With This Problem for a Decade

When you "run a Bitcoin node," what you're actually doing is downloading a compiled binary (or compiling one yourself from source), and trusting that binary to enforce the rules of the network. The binary validates every transaction, rejects invalid blocks, determines what is and isn't a legitimate Bitcoin. If the binary is compromised, your node is compromised. Doesn't matter how many copies of the blockchain you have, or how many peers you connect to.

The binary is the law.

For years, Bitcoin Core used a system called Gitian to produce its release binaries. Gitian was clever: multiple developers would compile the same source code inside identical virtual machines and compare results. If everyone got the same binary, you could be confident that no single developer had tampered with the output. This is called a *reproducible build*, and it was a genuine advance over the way most software ships, which is: a developer compiles a binary on their laptop, uploads it, and you just... trust them.

But Gitian had a problem Thompson would have recognized immediately.

The virtual machines ran Ubuntu Linux. They relied on Ubuntu's compiler, Ubuntu's linker, Ubuntu's standard libraries. The total set of trusted binaries (software that everyone simply assumed was honest) was approximately 550 megabytes. Half a gigabyte of machine code that nobody had audited from scratch, supplied by Canonical (Ubuntu's parent company), who received it from upstream GNU and Linux projects, who compiled it using previous versions of their own tools, who received those from...

You see the regression.

550 megabytes of "just trust us." For a system whose entire reason for existing is to not trust.

And there were practical problems too. Gitian pinned builds to a specific Ubuntu version, which meant you inherited whatever toolchain decisions Ubuntu's package maintainers made. At one point, a mingw-w64 linker option was patched in Ubuntu Bionic, then *unpatched* in Ubuntu Focal, breaking Bitcoin's security checks. You're building the world's most security-sensitive software, and your linker flags depend on which Ubuntu release happened to be current? (This actually happened.)

For most software projects, 550 MB of trusted binaries is normal. Nobody thinks twice about it. But for a system securing trillions of dollars, a system whose core value proposition is the elimination of trust, it was an uncomfortable dependency. The builders of Bitcoin were doing something no previous financial system had attempted: making the rules of money verifiable by anyone. But "anyone" still had to trust half a gigabyte of opaque binary code just to get started.

This tension sat unresolved for years. Not because nobody noticed. Because the solution was extraordinarily hard.

---

# The Long March to Guix

In 2019, a Bitcoin Core developer named Carl Dong opened Pull Request #15277 on GitHub. The title was unassuming: "contrib: Enable building in Guix containers." Technical description, routine formatting, the kind of PR that most people scroll past. But one line in the description stood out:

> "If OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler)."

What an extraordinary sentence. Someone was claiming, in a pull request for a trillion-dollar financial system, that someday the entire trust surface could be reduced to 500 bytes.

Guix (pronounced "geeks") is a package manager created by the GNU project. Unlike conventional package managers that download pre-built binaries from a repository, Guix can build every package from source, starting from a defined set of bootstrap binaries. More importantly, Guix was designed from the ground up with a focus on *bootstrappability*: the ability to trace the entire build chain back to its origins. Not just "did we get the same output?" but "can we account for every binary that participated in producing this output?"

The move from Gitian to Guix was not a weekend project. It took years. The PR was updated, debated, tested, and refined across multiple Bitcoin Core release cycles. The technical challenges were real: cross-compilation for five architectures (x86_64, i686, ARM, AArch64, RISC-V) plus macOS and Windows, all from a controlled environment with no network access, using only explicitly declared dependencies. No sneaking in a package at build time. No phone-home to Ubuntu's servers. Everything declared, everything auditable.

But the conceptual shift mattered more than the technical one.

Gitian asked: "Did multiple people get the same result?" That's a good question. It detects tampering by individual developers. But Guix asks a deeper one: "Can we account for every binary in the build chain?" It's the difference between checking that five people agree on the answer, and checking that the textbook they all read wasn't wrong.

With Gitian, you trusted 550 MB and then verified that everyone agreed on the output. With Guix, you start dismantling the 550 MB itself. Replace opaque Ubuntu packages with source-built equivalents. Pin the exact version of every tool, every library, every compiler. Build in a sealed container. The build becomes a pure function: source code and bootstrap binaries in, deterministic binary out. Nothing else.

Bitcoin Core v22.0, released in September 2021, was the first version built with Guix instead of Gitian. The trusted binary surface dropped from 550 MB to approximately 120 MB.

That's a 78% reduction in code you have to take on faith.

This was not a marketing milestone. It was an engineering one. In a single release, Bitcoin's build process became more auditable than virtually any other piece of software in production anywhere. And nobody outside of Bitcoin Core's development community really noticed.

But 120 MB was still 120 MB. Carl Dong's PR had pointed toward something more radical: a chain starting from a few hundred bytes. To get there, Bitcoin needed help from a separate community that had been working on the problem from the opposite direction.

---

# From 550 Megabytes to 357 Bytes

The bootstrappable builds project (bootstrappable.org) starts from a simple premise: compilers written in their own language depend on previous versions of themselves, creating an infinite regression of trust. Their goal is to break the regression by starting from something small enough to audit completely, and building upward.

They have a nice domestic analogy for this. To make yogurt, the first step is to add yogurt to milk. Where does the first yogurt come from?

Their answer is hex0. A program, 357 bytes long on x86 Linux, written in raw hexadecimal. Each pair of hex characters maps directly to a single processor instruction. No compiler. No abstraction. A human can sit down, read the hex, look up each instruction in the manual, and verify that it does one thing: read hex-encoded text and output the corresponding binary. A hex assembler that can assemble its own source code.

The yogurt that doesn't require yogurt.

From hex0, the bootstrap chain proceeds through twenty-eight stages. Each builds a slightly more capable tool using only the tools from previous stages. The progression is, I think, genuinely beautiful, so it's worth walking through:

**Stages 0-5: From nothing to C.** Stage 0 rebuilds hex0 from its own source, verifying the seed (you can already check that the 357-byte binary matches what hex0 produces from hex0's source). Stage 1 adds labels and relative jumps. Stage 2 handles absolute addresses. Stage 3 builds a minimal assembler. Stage 4 produces a rudimentary C compiler, specific to the target architecture. Stage 5 produces M2-Planet, a more capable C compiler.

We just went from 357 bytes of hand-verified hex to a working C compiler. Let that sink in.

**Stages 6-10: Bootstrapping the bootstrapper.** The chain rebuilds its earlier tools using the improved compilers, gaining cross-platform support and optimizations. The hex assembler from stage 1 gets rebuilt in C. The C compiler from stage 4 gets rebuilt with the better C compiler from stage 5. Each stage replaces trust with verification.

**Stages 11-28: The scaffolding.** A shell, a hash function, basic utilities. Everything needed for a real build environment.

At the end of stage 28, you have GNU Mes: a mutually self-hosting Scheme interpreter and C compiler in about 5,000 lines of simple C. Mes can build TinyCC (a small but real C compiler, about 25,000 lines of code). TinyCC can build an early version of GCC (2.95.3, vintage 2001). That vintage GCC can build a modern GCC. And modern GCC can build Bitcoin Core.

357 bytes to Bitcoin Core. Twenty-eight stages. Every step open, deterministic, reproducible.

Here are the numbers:

| Era | Trusted binary surface |
|---|---|
| Gitian (pre-2021) | ~550 MB |
| Guix (Bitcoin Core v22.0, 2021) | ~120 MB |
| Full bootstrap from hex0 (target) | 357 bytes |

That last row, if achieved completely, represents a 99.999935% reduction in the code you have to take on faith. From half a gigabyte to something shorter than a tweet.

Now, the honest caveat. As of early 2026, the full-source bootstrap from hex0 has been merged into the Guix project itself, but there's a gap. The bootstrap driver (Guile, the Scheme interpreter that orchestrates the whole Guix build process) is still about 25 megabytes of trusted binary. Work to bootstrap Guile itself is ongoing. It's hard (GCC post-4.8 requires C++, glibc-2.28+ requires Python, each creating new bootstrapping challenges). It may take years.

Bitcoin Core's current Guix builds start from Guix's present bootstrap set, not directly from hex0. So we're not at 357 bytes yet.

But the path is mapped. The hardest parts are done. And no other software project of comparable importance is further along this road. Most haven't set foot on it.

---

# Meanwhile, in the Rest of Crypto

Every blockchain, every cryptocurrency, every piece of financial software on earth is built with compilers that were built with compilers. The question isn't whether the trusting-trust problem applies to them. It does. The question is whether anyone is doing anything about it.

**Ethereum** took a fundamentally different approach: client diversity. Instead of one reference implementation, Ethereum supports multiple independent clients. On the execution layer: Geth (Go), Nethermind (C#), Besu (Java), Erigon (Go). On consensus: Prysm (Go), Lighthouse (Rust), Teku (Java), Nimbus (Nim), Lodestar (TypeScript), others. The theory is that a bug or backdoor in any one client affects only the fraction of the network running it.

This is legitimate. In 2016, attackers exploited a slow I/O path in Geth, but alternative clients kept the network running while Geth was patched. Client diversity works.

But it solves a different problem.

Client diversity protects against implementation bugs. It doesn't address the supply chain. Geth, which runs on roughly half of all Ethereum nodes as of late 2025, does not have reproducible builds. There are two open issues on GitHub requesting this. One filed in 2018. Another in 2023. Both unresolved. A KTH thesis examining the problem found three barriers to reproducibility in Geth alone: non-determinism from CGO, environment-specific metadata baked into binaries, and inconsistent build tooling across environments. No other Ethereum client has reproducible builds either.

So Ethereum can tell you that five different teams wrote five different implementations. It cannot tell you that any one of those binaries corresponds to its published source code. That's like having five factories building the same product from five different blueprints, and being unable to verify that any factory is actually following its blueprints.

Is that better than one factory you also can't verify? Sure. Is it a solution to the trusting-trust problem? No.

**Solana** is in a starker position. Until recently, the entire network ran a single client implementation (Agave). No reproducible builds. No bootstrappable chain. Five of Solana's seven major outages have traced to bugs in this one codebase. A second client, Firedancer (built by Jump Crypto), reached mainnet in late 2025 as a hybrid (Frankendancer), but the full independent client isn't production-ready yet. Solana does offer verified builds for smart contracts, using Docker containers for determinism. But the validator itself, the software that runs the actual network, has no such verification.

**Monero** is the sole exception. Following Bitcoin's lead, Monero has been migrating to Guix-based bootstrappable builds, with a PR closely mirroring Bitcoin Core's approach. This isn't surprising: Monero's engineering culture shares Bitcoin's emphasis on privacy, verification, and minimal trust.

**Traditional finance** doesn't enter this conversation at all. Banking software is proprietary, closed-source, and unauditable by design. When you trust a bank, you're trusting the institution, the software vendors they purchased from, the compilers those vendors used, the build infrastructure those compilers ran on. The trust surface isn't 550 MB or 120 MB. It's unknown and unknowable. Nobody even asks the question.

---

# The Frontier: Hardware

I should be honest about where this story hits a wall.

Even if the entire software toolchain is bootstrapped from 357 bytes, the resulting binary runs on hardware. And hardware has its own trust problems.

Modern processors contain management engines. Intel's Management Engine (ME) and AMD's Platform Security Processor (PSP) are autonomous subsystems embedded in the CPU. They run their own firmware, have access to system memory, and operate independently of the operating system. Their firmware is proprietary (Intel's is encrypted). You can't audit what they do. You can't fully disable them (people have tried; it bricks the machine). They are, in Thompson's framework, the deepest layer: microcode that no amount of software verification can reach.

Random number generators are another surface. Cryptographic operations depend on unpredictable randomness. If the hardware RNG is biased or backdoored, cryptographic keys can be weakened without any visible anomaly. This isn't theoretical. The Dual EC DRBG episode (a random number generator standardized by NIST, later shown to contain what appeared to be an NSA backdoor) proved it can happen. And did.

Network infrastructure (routers, switches, firmware updates delivered over the wire) adds more trust surfaces that software bootstrapping can't touch.

The bootstrappable builds community is thinking about this. Independent bootstraps on different processor architectures (x86, ARM) as a cross-check. Legacy boot processes that minimize firmware dependencies. These are research directions, not solutions. But at least they're research directions, which is more than most.

The honest picture: Bitcoin's software supply chain is, or is becoming, the most auditable in the world. Its hardware supply chain is no better or worse than anyone else's. The difference is that Bitcoin's engineers are looking at the problem instead of pretending it doesn't exist.

---

# Why You Should Care

When a nation adds Bitcoin to its reserves (and several now have), it's making an implicit statement: we trust this system. But what, precisely, is being trusted?

Not the blockchain. The blockchain is a data structure. Inert without software to interpret it. The trust is in the binary, the compiled software running on that nation's (or its custodian's) hardware. And the integrity of that binary depends on the integrity of the toolchain that produced it.

This is the due diligence question nobody is asking.

Institutions evaluate Bitcoin's monetary policy (fixed supply, halving schedule). Its network effects (hashrate, node count). Its liquidity and market structure. All important. But these are properties of the system as described in the source code. Whether the running software faithfully *implements* that source code is a separate question entirely. And it's the question that Guix and bootstrappable builds are designed to answer.

A sovereign wealth fund holding Bitcoin without understanding its software supply chain is like a central bank storing gold without assaying it. You might have what you think you have. You haven't verified it. For a system whose entire value proposition rests on verification over trust, that's a gap worth thinking about.

The work to close this gap is being done by a small number of engineers, most of whom will never be publicly recognized. They're not building features that make headlines. Not launching tokens. Not raising venture capital. They're writing twenty-eight-stage bootstrap chains and arguing about linker flags and debating whether 25 megabytes of trusted binary is 25 megabytes too many.

This is what building for the long term looks like. Not the price charts or the political endorsements or the conference keynotes. Pull requests that take years to merge. Projects named hex0 and M2-Planet and GNU Mes. People who understand that when you're building a financial system for centuries, you don't get to take shortcuts on trust.

357 bytes. That's where it starts.
