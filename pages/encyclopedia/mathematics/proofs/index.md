---
layout: default
---

## algorithm for finding proofs

Lets consider the example of the pythagorean theorem.
We are working with two-dimensional geometry and equations concerning the angles between and
length of line segments.
So we will formalize the geometry and constructions that add elements to that geometry.

The geometry is defined by points and line segments between points.
Line segments have length and line segments with common points have angles between them.
These lengths and angles are the variables of our system.
Triangles, rectangles, and other polygons will have area equations.

We end up with a set of variables and equations.
By performing the proper constructions we should have enough equations to prove the theorem.

The idea for creating an algoithm to find the proof is that we can put our variables and equations
into a graph and we can search the graph for the evidence for a proof.

The algoithm starts with an initial geometry and associated variables and equations and some known variables.
The initial geometry will be a triangle ABC.
The initial variables will be the lengths of the three sides and six angles (interior and exterior at each point).
We will set one of the angles of the triangle to 90 degrees.
We will give the goal in the form of an equation to prove: $$(AC)^2 + (BC)^2 = (AB)^2$$.

We define possible constructions that can be made one the geometry.
For example. We can take a line segment and construct a square with the line segment as one of its sides.
This will create two points, three lines, and several equations for angles and lengths.
The new equations will be added to the graph of existing equations.

The details of how the algoirthm would search the graph for proof of the theorem is not yet known in detail.

For this idea to be extended to other areas, we need concrete definitions of the mathematics involved and operations we can perform on it.

This idea may only apply to a relatively small set of problems whose theorem takes the form of an algebraic equations.

