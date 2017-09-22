---
layout: default
---

# finding the longest cycle using lp-relaxation

## preparing the graph

In order for this algorithm to work properly,
we must first perform some simplifying operations on the graph.
If used on just any undirected graph,
you can end up with multiple disconnected features in your solution.
These features can be cycles or paths.
They can be paths because the constraint on vertex inclusion explained below is that each vertex 
value is $$\le 2$$.
As far as I know, with the library that I am using, I cannot specify that the value be 
either 0 or 2 but not 1.
There also appears to be no way to prevent disconnected cycles, since they do not violate any of 
the constraints.

Instead, we will simplify the graph.
We can reduce the graph to the point where multiple features in the solution are not possible.
We can consider only 
[vertex identification](/pages/encyclopedia/mathematics/graph_theory/vertex_identification).
A problem arises when, after simplificiation, we have a pair of vertices with multiple edges 
connecting them.

We will illustrate with a simple example.

![](example_1.svg)

Which gets simplified to

![](example_2.svg)

Problem: a solution to the above could be any of the length-3 cycles in the original graph as
well as the true solution.
What we need to do is replace these edges with two virtual edges, each of which represents a choice 
between two of the original edges.
If we correctly choose which pairs of edge to combine, we will get the true solution.
It is clear that the pairs should be either (0--3 and 1--3) and (0--2 and 1--2) or (0--3 and 0--2) and (1--2 and 1--3).
The key here is that edges that do not share common neighbors are not in the same group.
The key may also be that edges that *do* share common neighbors *are* in the same group.
I'm not sure which it is.

An explanation of why the groupings are important is that when we identify two vertices, the edge
between them is lost.
In the new graph, two choices of solution that look the same are actually different because one
of those solutions would actually use the removed edge.
We want to make sure that our solution will use that removed edge.

It looks like this method of grouping edges only works in specific cases.
Namely it appears that we need at least four parallel edges that get grouped into two groups of two.

Another interesting example is

![](example_3.svg)

which gets simplified to

![](example_4.svg)

in this case, grouping does not help us.
The only thing to do is remove the edge (1--3) as it cannot be part of a valid solution.
So what information tells us that we should remove (1--3)?
It could be the fact that there are an odd number of edges (so we cannot evenly divide the edges into groups).
And that two of the three edges do not share neighbors, suggesting that they would be a valid solution.

## problem statement

maximize

$$
\mathbf{c} \mathbf{x}_e
$$

with constraints

$$
\mathbf{A} \mathbf{x}_e \le \mathbf{b}
$$

$$
\mathbf{x}_e \ge \mathbf{0}
$$

## details

In the integer program, the elements of the vector $$\mathbf{x}_e$$ are either $$0$$ or $$1$$ and represent inclusion in the cycle.
The relaxed constraint should be 

$$
x_e \le 1
$$

or

$$
\mathbf{I}_{e} \mathbf{x}_e \le \mathbf{1}_e
$$

where $$\mathbf{I}_{e}$$ is the identity matrix of size $$e$$ where $$e$$ is the number of edges in the graph and $$\mathbf{1}_e$$ is a column vector of ones of size $$e$$.
We can also define $$\mathbf{x}_v$$ to be a vector where each element represents a vertex and is the number of included edges connected to that vertex.

$$
\mathbf{D} \mathbf{x}_e = \mathbf{x}_v
$$

where $$\mathbf{D}$$ is the connectivity matrix for the graph.
Each included vertex should have a value of $$2$$ and every other vertex should have a value of $$0$$.
So we can write

$$
\mathbf{D}_{v,e} \mathbf{x}_e = \mathbf{x}_v \le \mathbf{2}_v
$$

and

$$
\mathbf{D} \mathbf{x}_e \le \mathbf{2}_v
$$

We can combine these two facts and write

$$
\begin{bmatrix}
\mathbf{I}_e \\
\mathbf{D}_{v,e}
\end{bmatrix}
\mathbf{x}_e \le
\begin{bmatrix}
\mathbf{1}_e \\
\mathbf{2}_v
\end{bmatrix}
$$







