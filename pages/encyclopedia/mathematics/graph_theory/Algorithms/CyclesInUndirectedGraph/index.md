---
layout: page
---

== Theorems ==

=== number of edges in a complete graph ===

$$
\frac{n(n-1)}{2}
$$

=== number of cycles in a complete graph ===

hypothesis: the number of unique length $k$ cycles in a complete graph with $n$ vertices is

$$
\frac{n!}{(n-k)!k}
$$

start with the number of permutations of $k$ vertices

$$
\frac{n!}{(n-k)!}
$$

Each permutation is a valid cycle.
We can divide these permutations into non-intersecting subsets of permutations in which any permutation in a subset can be made equal to any other permutation in that subset by simple shifting.
It is clear that each of these subsets will contain $k$ permutations.
And since shifting does not create a unique cycle, they are all equivalent cycles.
So to get the number of unique cycles, we divide by $k$.

Fun fact, for any odd numbered fully connected graph of size $n$, you can write $(n-1)/2$ cycles that share no edges and each touch each vertex exactly once.
These cycles will list each edge in the graph exactly once.
This of course, will only work for odd graphs.

graph SomeGraph {
0--1--2--3--4--0
0--2--4--1--3--0
}

=== length of cycles in fully connected graph ===

I hypothesis that for graphs with an odd number of vertices, it is possible to create a cycle that includes all edges.
And that for graphs with an even number of vertices, this is not possible.

It is easy to prove that this is impossible for graphs with even number of vertices, because the number of edges connected to each vertex is $n-1$ where $n$ is the number of vertices.
So the number of edges connected to each vertex will be odd.

The longest path possible in an even numbered graph is

$$
n\left(\frac{n-2}{2}\right)+1
$$

== Algorithm ==

This algorithm uses temporary orienting of edges.
The stack is a ordered list of edges to which one can add and remove edges from either end.

{{{
function cycles(v0)
    for each edge e connected to v0 and not in the stack
        v1 is the other vertex of e
        orient e and put in on the bottom of the stack

        if v1 has not been used as the starting vertex yet
            if the first and last vertices in e are equal
                save the stack as a cycle
            else
                call cycles(v1)

        pop e from the bottom of the stack

for each vertex v
    begin with an empty stack
    call cycles(v)
}}}

I believe this will identify all cycles of a particular definition but I do not have a proof.
Calling {{{cycles(v)}}} can find all cycles containing the vertex {{{v}}}.
So from the outer iteration, where we call {{{cycles}}} for each vertex in the graph, we can ignore cycles in subsequent calls
that would contain any vertex that has already been used as the starting vertex of {{{cycles}}}.
