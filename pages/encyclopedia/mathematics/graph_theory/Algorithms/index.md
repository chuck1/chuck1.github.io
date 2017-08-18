---
layout: page
---

 * [[/CyclesInUndirectedGraph]]

== Method For Finding Edge Subsets ==

This method should be applicable to four types of edge subsets:
 * cycles with repeated vertices
 * cycles without repeated vertices
 * paths with repeated vertices
 * paths without repeated vertices

The goal is to develop a method that we can prove finds all solutions and does so relatively efficiently.

Define a function $F$ of vertex or edge $x$ such that we can prove that $F$ will return all solutions (with no repeated solutions) that contain $x$ and no solutions that contain $y|y<x$.
You can easily see that evaluating $F$ for each $x$ in the graph, we will obtain all solutions with no repeated solutions.

Clearly the challenge now is to find $F$ that satisfies the above.

Here is an attempt to write out these ideas using mathematical notation:

$$
y \notin s, \forall s \in \textrm{F}(x), \forall y | y < x
$$

$$
\textrm{F}(x) \cap \textrm{F}(y) = \emptyset, x \neq y
$$

$$
\bigcup_x \textrm{F}(x) = S
$$

$$
\textrm{F}(x) = \{ s | x \in s, y \notin s, y < x \}       
$$

There is the question, should $F$ be a function of a vertex or an edge. I think that this does not matter. We must be able to say

$$
S_{x <= a} \cup S_{x > a} = S, S_{x <= a} \cap S_{x > a} = \emptyset
$$

$$
S_{x <= a} = \{ s | x \in s, x <= a \}
$$

$$
S_{x > a} = \{ s | x \in s, x > a, y \notin s, y <= a \}
$$

now consider $a = x_0$

$$
S_{x <= x_0} = \{ s | x \in s, x <= x_0 \} = \{ s | x_0 \in s\}
$$

compare to

$$
\textrm{F}(x_0) = \{ s | x_0 \in s, y \notin s, y < x_0 \} = \{ s | x_0 \in s \}
$$

so

$$
S_{x <= x_0} = \textrm{F}(x_0)
$$

If we combine

$$
\textrm{F}(x_0) \cup \textrm{F}(x_1) = \{ s | x_0 \in s \} \cup \{ s | x_1 \in s, y \notin s, y < x_1 \} = \{ s | x_0 \in s \} \cup \{ s | x_1 \in s, x_0 \notin s \} = \{ s | x \in s, x <= x_1 \} = S_{x <= x_1}
$$

The only requirement for using vertices or edges is that we can define the operators $\in$ and $\notin$ such that

$$
\begin{align}
\{s|x \in s\} \cup \{s|x \notin s\} = S\\\{s|x \in s\} \cap \{s|x \notin s\} = \emptyset
\end{align}
$$

And I see no reason that we cannot do this for both vertices and edges, even though the solutions are fundamentally subsets of edges.

=== Depth First Search ===

Here we define a function that will serve as a recursive component of $F$ using a depth-first-search algorithm.

{{{

function g(v)
  for each edge e adjacent to v
    if the stack contains e then continue
    push e onto to stack

    if the stack is a valid solution
      save the stack as a solution

    if we should descend
      g(vertex opposite v in e)

    pop e from the stack

}}}
