---
title: "Traveling Salesman"
date: 2005-04-02
source: https://tejaswin.com/2005/04/02/traveling-salesman/
---

The traveling salesman problem (TSP) is a very simple combinatorial optimization problem. Given a set of cities and distances between each pair, the problem is to find the tour of least distance that travels each city exactly once. Simple – as in simple to state. But from what I have seen this seems to be the hardest of the hard problems to solve.

To give some background, there are these famous hard problems in Computer Science that do not have “efficient” solutions. Brute force solutions work very easily on them, but take an eternity to run. In spite of 40 years of extensive research by some very smart people, brute force seems to be the only solution. For example, the TSP can be solved by listing all possible tours covering the cities once, and picking the one with the least length. This takes an eternity as there are an exponential number of such tours (n!). These problems are the (in)famous NP-Hard problems. Stephen Cook at the University of Toronto proved that if one of them can be solved efficiently, all of them can be!!! A very intuitively pleasing fact.

Tragically, most combinatorial optimization problems in nature turn out to be NP-hard. As 40 years of research hasn’t found a good solution to these problems, people have begun to approximate the solutions. Say, for TSP, if the least length best tour is around 100 KM, a procedure that finds a tour of 150 KMS would be considered good. Of course, if the length of the best tour is around 5000 KM, the same procedure should return a tour of length 7500 KM. This means that the approximate procedure for TSP should return a solution that is always some fixed fraction times more than the best solution. Most of the NP-hard problems have reasonable approximation algorithms; the TSP does not!!

It is proven that you cannot invent a procedure that can take a set of cities and give a tour that will always be some fraction times more than the optimal solution. TSP seems to be very very very very hard. But of course, most of this theory would collapse if someone comes up with a good way to solve one NP-hard problem.

In spite of my being really really really bad at this academically, I am completely enamored by the theory of NP-completeness. Somehow this notion of possible but not-feasible seems to make it intriguing. It is incredibly fascinating to see how all NP-hard problems are closely related to each other, and solving one solves them all, but approximating one, doesn’t approximate them all. Seductive!!

Reminds me of Dijkstra’s famous quote – “Computer Science is as much about Computers as Astronomy is about Telescopes.”
