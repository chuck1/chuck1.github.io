---
layout: default
---

## Using graph theory

A system of equations can be represented by a graph.
In such a graph, there are two types of vertices: variable-vertex and equation-vertex.
Edges connect variable vertices to the equation vertices in which they appear.

This model helps us identify simplifications to the set of equations.

For these simplification to be valid, we must assume that all equations represented in the graph
are independent.

### Leaf variable vertices

If a variable-vertex is a leaf, then the equation-vertex to which it is connected can be removed from the graph.

### Leaf equation vertex

If an EV is a leaf, this means that it is an equation of only one variable, implying that we can solve for the value of
the variable and remove this EV and the connected VV from the graph.

### Unconnected vertices

Unconnected vertices, which can only be variables-verties, can be removed.

### Bridges

Find a bridge edge.
Try removing the equation-vertex connected to that edge.
If the resulting component that contains the variable(s) of interest still has Ve >= Vv, then the edge can be removed.

### Cycles

If a graph is equal to a simple cycle, then the system is simplified as much as possible and is solvable.
The number of variable-vertices and equation-vertices are equal.

Imagine a graph constructed by starting with a simple cycle as described above and adding a path between two vertices in the cycle.
If the path connects an existing VV and EV or two existing VVs, then the system is still solvable.
However, if the path connects two existing EVs, then the system is now un-solvable.



