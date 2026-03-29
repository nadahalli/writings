---
title: "Anchor Text and Focused Crawling"
date: 2005-02-18
slug: "anchor-text-and-focused-crawling"
source: https://tejaswin.com/2005/02/18/anchor-text-and-focused-crawling/
categories:
  - "computer science"
---

Its been a while since I have blogged anything technical.

These days, I am working on [the open source search engine, Nutch](<http://www.nutch.org/>). Before I get into what I am doing, let me explain why, in the last sentence, I put the phrase “open source search engine” as a part of the href tag. Search engines use anchor text extensively to figure out what a page is about. For example, the [home page of Tejaswi](<http://www.it.iitb.ac.in/~tejaswi>) doesn’t have the phrase “home page” anywhere. So, by looking at the anchor text of all the in-links to a page, the search engine figures out what the content of the page might be about. This is a latent way of identifying the content of a page: by looking at what in-links call it. Now, when I say “the open source search engine Nutch” in the anchor text and link to nutch.org, that phrase gets associated with the site, and helps someone searching for an open source search engine, but has no clue about Nutch itself.

Currently, I am working on the crawler part of the search engine. The crawler/spider is an offline process that goes all over the web and gets pages for the search engine to index. The idea is to start the crawler with a set of seed pages. The crawler then starts indexing the textual content of each page, and recursively crawls each page’s out-links. This goes on ad-infinitum. This part is pretty standard, and is already implemented. My job is to ensure that the crawl is not ad-hoc, ie. not all out-links are crawled. I am trying to “focus” the crawl so that only pages pertinent to certain topics get crawled, and subsequently indexed. Topics like “cycling”, “art cinema”, “photography”, “BDSM” etc. Why do we need to focus a crawl?

Google currently claims that it indexes 8 billion webpages. According to [recent estimates](<http://citeseer.ist.psu.edu/eiron04ranking.html>), un-indexed pages outnumber indexed pages by a factor of 4-5. This means that there are at at least 33 billion pages out there that Google can index, but is not indexing. Why not? well, for one, more pages doesn’t necessarily mean better search results. Good number of pages representing a broad range of topics means better search results. This is where a focused crawl might be preferred over an ad-hoc crawl. If you are really interested, take a look at my [advisor](<http://www.cse.iitb.ac.in/~soumen>)‘s [Focused Crawling](<http://www.cse.iitb.ac.in/~soumen/focus/>) page for more information.

In other news, read [Jeremy Zawodny’s post on Mark Jen](<http://jeremy.zawodny.com/blog/archives/004157.html>) to know about the Google employee who got fired for blogging some company internals. All corporate bloggers out there….you reading this?
