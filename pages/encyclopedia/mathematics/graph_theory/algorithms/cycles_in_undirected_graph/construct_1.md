---
layout: default
---

**goal**

Given a graph with at least one cycle, draw the graph by first finding one cycle and drawing just that cycle.
Then find another cycle that is not equal to the first but has at least one edge in common with the first.
Part of the second cycle is already drawn, draw the rest of it by connecting with a path two vertices that are already drawn.
Continue this process until no more cycles are found in this manner.

**algorithm**

First we need to find the first cycle.
This can be done any number of ways.

The next step is a bit trickier.
We will generalize for any point in the process.
So we have drawn a graph composed entirely of cycles.
Make a spanning tree of this graph and to it add all of the undrawn edges.
For each edge in the spanning tree, look for any cycle that contains this edge.
By creating a spanning tree, we have guaranteed that none of the already drawn cycles
will be found in this step.
Having a spanning tree also guarantees that if there is another cycle to be found, it can be found in this manner.
This is because every new cycle found in this way can be thought of as a path connecting drawn vertices.
In a spanning tree there is a path between any pair of vertices.
These two paths togehter will form a cycle.



