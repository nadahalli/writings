---
title: "Heuristics vs. Provability"
date: 2006-01-04
slug: "heuristics-vs-provability"
source: https://tejaswin.com/2006/01/04/heuristics-vs-provability/
categories:
  - "computer science"
---

Given a problem, we can:

  1. Give efficient methods to find exact solutions. When this is possible, all’s well. But alas, this is not possible all the time.
  2. Give inefficient methods to find exact solutions (brute force), and bemoan that [P != NP (mostly).](<https://tejaswin.com/2005/04/02/traveling-salesman/>)
  3. Propose intuitively appealing heuristics that are quick, and give “mostly good” results in practice, and hope that the malicious worst case input which can tear the heuristic apart never comes about.
  4. Prove theoretical approximation guarantees about these heuristics so that even in the worst case, the heuristic won’t go bad beyond some known bound.



Personally, I am fascinated by #4. Most current large scale problems rely on #3, which hopefully will get elevated to #4 in a few years time, and theoreticians will tell the practitioners – “Yeah, your heuristic will never give a solution that if off the optimal by 200%.” As a budding researcher, is it better to build simulations, concrete systems, models, etc., and show empirically that certain heuristics work most of the time? Or is it better to take some small heuristic and prove without doubt its effectiveness under all circumstances?

The latter appeals to me because of its no nonsense, matter of fact, precise nature. But I can also see how we cannot do without the former. The former (heuristics) gets built to tackle real world problems. Theoreticians follow up later by giving provable approximate guarantees for these heuristics. Combinatorial optimization is rife with this pattern. What about other heuristics though?

Take the everyday example of Question Answering. Given a question, and an essay that might contain the answer to the given question, a reasonably educated person can extract an answer without much difficulty. But this simple task is extremely hard for an automated system. It can manage questions of the type: “how much,” “what,” and “when”; but will get flummoxed by questions of the type: “why” and “how”. Practioners in the area of Natural Language Processing come up with heuristics that attempt to answer these tough questions, but there is no provable guarantee that these heuristics can answer all questions correctly all the time.

Can problems from the “Human Domain” be modeled fully as combinatorial problems so that we can hopefully give some approximation guarantee? Given realistic scale and scope, how does the human brain solve such problems (like question-answering)? Does the brain map everything to combinatorial optimization? Can its modus operandi be applied to automated systems so that they solve our problems while we attack other problems that right now are complicated even for the human mind?

---

<details>
<summary><strong>Archived Comments (2)</strong></summary>

**test123** — 2006-01-07 08:29:16

I am for the latter:<br/>The token ring architecture proposed by IBM, had the advantage of the latter. Deterministic worst case guarantees were what was required. ( Sure there are other examples to the contrary, but interesting example of when mathematical proving can be useful). Same with RTOS I guess. ( I am sure Sudeep can explain it ). You need to prove hard guarantees.

---

**sudeep** — 2006-01-04 06:33:02

<i>As a budding researcher, is it better to build simulations, concrete systems, models, etc., and show empirically that certain heuristics work most of the time? Or is it better to take some small heuristic and prove without doubt its effectiveness under all circumstances?<br/></i><br/><br/>I strongly agree with the former. The latter becomes a  problem of mathematics and narrows down to only a small number of heuristics.Although "mathematical proof" is something, a simulation is what matters because it is a better approximation of reality than pure maths.Laymen will be more convinced by simulations and reports of input.

---

</details>
