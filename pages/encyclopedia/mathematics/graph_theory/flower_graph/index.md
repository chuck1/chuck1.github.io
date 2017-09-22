---
layout: default
---

# flower graph

Let $$G = (V,E)$$ be an undirected graph composed of $$n$$ simple cycles in which each pair of
cycles has exactly one vertex in common, the root vertex.

For example here is a flower graph with $$n = 3$$.

![](flower3.svg)

The number of [cycles][cycles] in a flower graph of size $$n$$ is

$$
\sum_{k=1}^n \left( \begin{array}{c} n \\ k \end{array} \right) 2^k (k-1)!
$$


[cycles]: /pages/encyclopedia/mathematics/graph_theory/cycles

