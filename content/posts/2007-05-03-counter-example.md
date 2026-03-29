---
title: "Counter Example"
date: 2007-05-03
slug: "counter-example"
source: https://tejaswin.com/2007/05/03/counter-example/
categories:
  - "computer science"
  - "research"
---

Finding counter examples to conjectures can be notoriously hard (pun? I think not). This is an area of creativity that mostly goes unappreciated.

Here’s a personal anecdote: my father once came up with an algorithm to solve a hugely constrained version of the [traveling salesman problem](<http://167.172.176.209/2005/04/02/traveling-salesman/>). The greedy proof was slightly hand-wavy, and I felt it would be an easier thing to find a counter example where his algorithm wouldn’t find the optimal tour. Of course, I was just trying to tell him that he couldn’t have solved TSP (or even approximated it). I learnt two lessons that day.

Lesson One: One must always speak sweet, because one underestimates the number of times one has to eat his own words.

Lesson Two: Finding counter examples can get quite tricky – and if I may, I would admit that it’s not just tricky, it’s quite hard – requires tons of patience, and a deep understanding of the problem and the algorithm we are out to disprove. I had learnt a similar lesson earlier in Sundar’s Approximation Algorithms class. Sundar let us spend one hour counter-exampling that a minimum spanning tree over the vertex set wouldn’t give us a minimum Steiner tree. The counter example used a ‘construct’ that was quite simple, and took a few minutes of dedicated thought to find. But what amazed me today was this fact about [Tait’s conjecture](<http://en.wikipedia.org/wiki/Tait%27s_conjecture>):

> Tait’s conjecture states that “Every [polyhedron](<http://en.wikipedia.org/wiki/Polyhedron> "Polyhedron") has a [Hamiltonian cycle](<http://en.wikipedia.org/wiki/Hamiltonian_cycle> "Hamiltonian cycle") (along the edges) through all its [vertices](<http://en.wikipedia.org/wiki/Vertex> "Vertex")“. It was proposed in 1886 by [P. G. Tait](<http://en.wikipedia.org/wiki/P._G._Tait> "P. G. Tait") and disproved in 1946, when [W. T. Tutte](<http://en.wikipedia.org/wiki/W._T._Tutte> "W. T. Tutte") constructed a counterexample with 25 faces, 69 edges and 46 vertices.

Imagine the patience, creativity, deep understanding of the problem, and the [least appreciated of them all] ability to borrow from related problems and areas – it takes to come up with such a counter example. And I keep wondering: _why research?_

---

<details>
<summary><strong>Archived Comments (9)</strong></summary>

**Tejaswi** — 2007-10-23 10:08:21

@Deeps: I had forgotten to add that the graphs are constrained by the triangular inequality.

---

**Deepak** — 2007-10-23 08:59:11

>> a minimum spanning tree over the vertex set wouldn't give us a minimum Steiner tree<br/><br/>why one hour? take a triangle ABC with edge weights AB=1, BC=1, AC=3. min spanning tree of {A,C} is of cost 3 where as min steiner tree over {A,C} is of cost 2.<br/><br/>Did I understand the question wrong?

---

**Samba** — 2007-10-05 08:02:49

The bigger question is, don't examples suffice? Why do we need counter-examples? Examples show us that we can get some wok done. So "let's get it done", with apologies to Citigroup. If our algorithm cannot get something done, let's try a trick older than mathematics - money! If we cannot solve the traveling salesperson problem, let's ask him not to travel - we can establish retail outlets, start selling online or organize a customer event where potential customers travel, wine, dine and hopefully write a check.<br/><br/>Pragmatism aside, I do realize that the traveling salesperson problem is an important problem that's better solved than unsolved. So let me make an effort propose a solution. Since the traveling salesperson problem is NP hard (I got to know what it means, courtesy you), can we not make the hardware that executes the NP hard algorithm scale up as the number of nodes scales up?

---

**Saket Sathe** — 2007-06-26 05:07:36

There is an extremely celebrated book devoted to <a href="http://en.wikipedia.org/wiki/Counterexamples_in_Topology" rel="nofollow ugc">counter examples in topology</a> by Steen and Seebach. Although I don't think it relates to graph theory (or TSP, for that matter) in any sense, but it deals with a more general subject -- topology.

---

**Asterix** — 2007-05-22 12:06:35

There is an urban legend about a professor (some say he is none other than Prof Diwan). An undergraduate was giving a seminar and the prof was in the audience. The student made a cavalier claim of some sort which the prof was not comfortable with. After about 30 seconds, the prof stood up and drew a 17-node weighted graph to disprove the claim. <br/><br/>Not as good as Tutte's polyhedron, but impressive none the same.<br/><br/>Rahul

---

**test123** — 2007-05-05 17:57:49

Similar experience with reductions. Coming up with the widget for the hamiltonian or from 3-SAT to vertex cover. <br/><br/>Non-Euclidean geometry anybody :).

---

**Meghana Kshirsagar** — 2007-05-05 10:11:28

Your post reminded me of something I read elsewhere. Someone recently <a href="http://arxiv.org/abs/math.NT/0703367" rel="nofollow ugc">disproved </a> the <a href="http://en.wikipedia.org/wiki/Riemann_Hypothesis" rel="nofollow ugc"> Riemann hypothesis</a>. So he wasn't that great a mathematician huh?

---

**Anonymous** — 2007-05-04 13:26:22

Then there are <a href="http://www.amazon.com/Counterexamples-Topology-Lynn-Arthur-Steen/dp/048668735X" rel="nofollow ugc"> these </a>   <a href="http://www.amazon.com/Counterexamples-Analysis-Dover-Books-Mathematics/dp/0486428753/ref=pd_bxgy_b_text_b/102-2951266-9709754" rel="nofollow ugc"> two </a> books.

---

**sudeep** — 2007-05-04 01:47:02

<i>Imagine the patience, creativity, deep understanding of the problem, and the [least appreciated of them all] ability to borrow from related problems and areas - it takes to come up with such a counter example. And I keep wondering:  why research?</i><br/><br/>More than the patience it is about a "gut feel" and a motivation which comes with a familiarity (which can be experienced at the beginning or somewhere down the lane) while studying a problem which makes a mathematician/scientist set to disprove something. Exceptions to rules are not a good thing....There are more like Kabaab mein haddi...But if there are too many exceptions, the rule itself may be screwed up.<br/><br/>The bottomline is if you try to "generalize" a counter-example, there could be a counter-example to a counter-example (which can be called a counter-counter example??).<br/><br/><i>PS:- I am not drunk.Sumne timepass ge barde.....</i>

---

</details>
