---
layout: default
title: Voronoi Clip
---

# Collision Detection

Use an n-dimensional V-Clip algorithm.

For generalization of the VClip algorithm, we must generalize some of the algorithms for all orders of feature.
However, there are always exceptions.
One exception is that there is no face-face state in the original algorithm, faces are unique in 
that they are the only feature that IS the same order as the hyperplanes that bound VR regions.
So it is the only feature that is one of its own VR bounding hyperplanes.
0-order features (vertices) are also unique in higher-dimensions in that their parameterization is trivial.
All other features (features with order between 0 and M-1 (1 to M-2 inclusive)) must be treated the
same regardless of order.

We are left with interactions shown in the figure.
V represents vertices, F represents faces, and K represents all other features.
As in the original VClip algorithm, the only type of interaction missing is face-face.

    graph SomeGraph {
      v [label="V\nk=0"]
      k [label="K\n0<k<(N-1)"]
      f [label="F\nk=N-1"]
      v -- { k f v }
      k -- {f k}
    }
    
## Generalized Parts

* Determine if feature X is completely excluded by the VR planes of feature Y
  * if order of X is 0
  * if order of X is between 0 and \\(N-1\\)
    * requires parameterization of X
      * The original does this for edges but not for faces because there is no F-F algorithm
      * See math section for parameterization of k-subspace 
   * Parameterization will yield intersection of X with VR planes of Y
   * Derivative of distance: see below

## Definition of Voronoi Regions

Since Voronoi regions are regions of n-space, they must be defined by bounding hyperplanes.

For any n-dimensional [convex polytope](http://en.wikipedia.org/wiki/Convex_polytope#Properties), 
we can construct a [Hasse diagram](http://en.wikipedia.org/wiki/Hasse_diagram) that represents the topology.
This diagram is a graph in which each vertex is a feature of the shape.
The graph is organized into rows of vertices where each row contains the feature of dimension k and k goes from -1 to n.
Edges in the graph represent composition; if a k-dim and a (k-1)-dim feature are connected, then the (k-1)-dim feature is part of the definition of the k-dim feature.
Since each k-dim feature can be defined just by a set of (k-1)-dim features, only adjacent rows are connected.

For the purposes of the V-Clip algorithm, we need only the 0-dim through (n-1)-dim rows of the graph.
Each graph edge represents a boundary hyperplane between Voronoi regions.

### Theory for the Definition of Region Boundaries Based on the Face Lattice

Consider adjacent layers k and k-1.
The (k-1)-subspace __will__ be on the boundary hyperplane.
The k-subspace __will not__ be on it.

The (k-1)-subspace __will__ be on the k-subspace.
Therefore we can extract the k-1 basis vectors that are common to both subspaces from the k-subspace, leaving a single vector that is orthogonal to the (k-1)-hyperplane.
The hyperplane boundary has this vector as its normal.

Since a k-subspace can be defined by equations of the form

$$
\mathbf{a}_i \cdot \mathbf{x} = b_i : 1 \le i \le (n-k)
$$

or

$$
Ax = B
$$

## Clipping

In the original VClip algorithm, we calculate the intersection of edges with boundary hyperplanes. The result is the value of the parameterization variable of the edge at the point of intersection.

The general algorithm will be as follows

    E is an empty set of inequalities of the parameters of subplace X
    for each hyperplane P in S
      calculate the intersection for X and P and represent with linear inequality: e = (A s < B)
      if e is less restrictive than the combined inequalities of E
        continue
      if the combination of e and any subset of elements of E are more restrictive than other elements of E
        remove those elements of e
        add e to E

How do we make the comparisons described in the code above?
Below is one such method

### Row Reduction

In general, if the have a k-dimensional subspace, you will have k parameters.
You will need k linearly independent inequalities to compare to one inequality.
By combining these k inequalities into a matrix and reducing the rows, we get inequalities of the individual parameters.
These can be subtracted from the inequality in question until a single parameter inequality remains.
This inequality can be compared with the unused inequailty form the row reduction.
If these are exclusive, then the feature in question is excluded from the Voronoi region.
If they are compatible, then one must make the other irrelevant (unless they are equal but we will ignore that possibility).
If the inequality in question is redundant, then it should be ignored.
If the inequality form the row reduction is redundant, then one of (but which we do not know) the inequalities in the set should be dropped.

## Distance from Voronoi Plane to Feature

In the original clipping algorithm, we determine whether or not an edge is fully included, clipped, or fully excluded by checking the signed distance from the end-points of the edge to the Voronoi hyperplane.
We can do a similar check for a K-order feature in M-space.
For a K-order feature, we can follow the topology graph down to the 0-order features (vertices) that lie on the feature.
Since space and all features are linear, we know that the points on the k-feature with minimum and maximum distance from the hyperplane will be one of these vertices.

### Derivative of Distance

Given the feature subspace


$$
\mathbf{x}=\mathbf{p} + \mathbf{A}\mathbf{s}
$$


and the hyperplane


$$
\mathbf{x} \cdot \mathbf{\hat{n}} = d
$$


The distance from any point on the subspace \\(\mathbf{x}\\) to the hyperplane is


$$
D = \mathbf{x} \cdot \mathbf{\hat{n}} - d
$$



$$
D = (\mathbf{p} + \mathbf{A}\mathbf{s}) \cdot \mathbf{\hat{n}} - d
$$



$$
D = \mathbf{p} \cdot \mathbf{\hat{n}} + (\mathbf{A}\mathbf{s}) \cdot \mathbf{\hat{n}} - d
$$



$$
D = \mathbf{p} \cdot \mathbf{\hat{n}} + (\mathbf{A}^T \mathbf{\hat{n}}) \cdot \mathbf{s} - d
$$



$$
D = \mathbf{p} \cdot \mathbf{\hat{n}} + (\mathbf{A}^T \mathbf{\hat{n}}) \cdot \mathbf{s} - d
$$



$$
\frac{d}{d\mathbf{s}}D = \frac{d}{d\mathbf{s}}(\mathbf{p} \cdot \mathbf{\hat{n}} + (\mathbf{A}^T \mathbf{\hat{n}}) \cdot \mathbf{s} - d)
$$



$$
\frac{d}{d\mathbf{s}}D = \frac{d}{d\mathbf{s}}((\mathbf{A}^T \mathbf{\hat{n}}) \cdot \mathbf{s})
$$



$$
\frac{d}{d\mathbf{s}}D = \mathbf{A}^T \mathbf{\hat{n}}
$$



