= Geometry =

== Requirement for Valid Lower-Dimensional Features in Higher Dimensions ==

There is a requirement that all of the lines that form a face are co-planar. Is there a higher-dimensional generalization of this requirement? I believe it requires considering the next highest dimension: a face is 2D but this requirement is only relevant if we are in working in 3D (being non-co-planar means that a vertex has a component outside the 2D subspace of the face). So this is difficult to grasp for higher dimensional because to have this requirement for a polyhedron, a vertex must be capable of having a component outside or perpendicular to the 3D subspace of the polyhedron, which would be the 4th dimension.

So here is an attempt at generalizing this requirement. in N dimensions, an K dimensional polytope, where K is less than N, must meet the following requirement. We can create a subspace basis for our polytope with K basis vectors. We shall then find the remaining (N-K) vectors perpendicular to our subspace basis and each other. Together these N vectors form a new coordinate system for N space. We can transform each vertex of our polytope to these new coordinates. For each vertex, the components in the last (N-K) directions corresponding to the space perpendicular to our polytope subspace must be zero.

= Geometric Algebra =

== Rotations ==

Rotate a vector <math>\mathbf{v}$$ by rotor <math>\mathbf{r}</math>. A rotor is an arbitrary sum of even-grade terms.


$$
\mathbf{v}' = \mathbf{\tilde{r}}\mathbf{v}\mathbf{r}
$$


Example in three dimensions


$$
\mathbf{v}' = (r_0 - r_{1,2} \mathbf{e}_1 \mathbf{e}_2 - r_{1,3} \mathbf{e}_1 \mathbf{e}_3 - r_{2,3} \mathbf{e}_2 \mathbf{e}_3)(v_1 \mathbf{e}_1 + v_2 \mathbf{e}_2 + v_3 \mathbf{e}_3)
(r_0 + r_{1,2} \mathbf{e}_1 \mathbf{e}_2 + r_{1,3} \mathbf{e}_1 \mathbf{e}_3 + r_{2,3} \mathbf{e}_2 \mathbf{e}_3)
$$


If you distribute the above, the trivector terms cancel, leaving only the vector terms. If you collect the vectors terms, you can construct a rotation matrix and see that it is identical to construction using quaternions.

The only requirement for <math>r$$ is


$$
\mathrm{gorm}(\mathbf{r})=1
$$


where


$$
\mathrm{gorm}(\mathbf{r}) \equiv \langle \mathbf{\tilde{r}}\mathbf{r} \rangle_0
$$


Note that the number of terms in the rotation equation before simplification is <math>n^2 2^{(n-1)}$$. So the computational cost increases quickly with <math>n</math>.

= Linear Algebra =

== Definition of a Subspace ==

A k-dimensional subspace will at first be defined by the intersection of (n-k) hyperplanes.

<math>\mathbf{n}_i \cdot \mathbf{x} = d_i$$

or

<math>\mathbf{B} \mathbf{x} = \mathbf{d}$$

We want to convert this to the form

$$
\mathbf{x} = \mathbf{p} + \mathbf{A} \mathbf{s} $$

The columns of <math>\mathbf{A}$$ are orthogonal basis vectors for the subspace.
I do not yet know how to determine <math>\mathbf{A}$$.
Keywords to research are

* Nullspace
* Matrix Kernel
* Vector space basis
* Gram-Schmidt Process

== Intersection of a Ray and a Hyperplane ==

The ray is defined by

<math>\mathbf{x} = \mathbf{p}_0 + k \mathbf{v}$$

The plane is defined by

<math>\mathbf{n} \cdot \mathbf{x} = d$$.

Combining these gives

$$
\mathbf{n} \cdot (\mathbf{p}_0 + k \mathbf{v}) = d
$$

$$
\mathbf{n} \cdot \mathbf{p}_0 + \mathbf{n} \cdot (k \mathbf{v}) = d
$$

$$
k = \frac{d - \mathbf{n} \cdot \mathbf{p}_0}{\mathbf{n} \cdot \mathbf{v}}
$$

Note that if <math>\mathbf{n} \cdot \mathbf{v}=0$$, the ray is parallel to the plane and there is not point of intersection.

== Intersection of Subspace and Hyperplane ==

A subspace can be parameterized as

$$
\mathbf{x} = \mathbf{p} + \mathbf{A} \mathbf{s} $$

A sided hyperplane inequality is given by

$$
\mathbf{n} \cdot \mathbf{x} < \mathbf{d} $$

Combine to get

$$
\mathbf{n} \cdot (\mathbf{p} + \mathbf{A} \mathbf{s}) < d
$$

$$
\mathbf{n} \cdot \mathbf{p} + \mathbf{n} \cdot (\mathbf{A} \mathbf{s}) < d
$$

$$
\mathbf{n} \cdot (\mathbf{A} \mathbf{s}) < d - \mathbf{n} \cdot \mathbf{p}
$$

$$
(\mathbf{A}^T \mathbf{n}) \cdot \mathbf{s} < d - \mathbf{n} \cdot \mathbf{p}
$$

This is a single linear inequality of $$\mathbf{s}$$.

== Convert from Position Vector to Parameter Vector on Subspace ==

Given the k-dimensional subspace defined by

$$
\mathbf{x} = \mathbf{p} + \mathbf{A} \mathbf{s}
$$

and a known point <math>\mathbf{x}$$ on that subspace. Find the value of the parameter vector <math>\mathbf{s}</math>.

$$
\mathbf{A} \mathbf{s} = \mathbf{x} - \mathbf{p}
$$

If we guarantee that the basis vectors of the subspace (the column vectors of <math>\mathbf{A}$$) are orthogonal, we can simply project <math>\mathbf{x} - \mathbf{p}</math> individually onto each of these basis vectors.

$$
s_i = (\mathbf{x} - \mathbf{p}) \cdot \mathbf{\hat{v}}_i
$$

<math>\mathbf{s} = \mathbf{A}^T (\mathbf{x} - \mathbf{p})$$

'''Hypothesis''' If x is not on the subspace, s will be the parameter for the projection of x onto the subspace.

# N-Space Cross Product

We start with the following formula for the determinant of an NxN matrix.

$$
\mathrm{det}(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma_i}
$$

$$
\mathrm{det}(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) a_{1,\sigma_1} \prod_{i=2}^n a_{i,\sigma_i}
$$

If the first row of the matrix is composed of the unit vectors of N-Space

$$
a_{1,i} = \mathbf{e}_i
$$

then we can write

$$
\mathrm{det}(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \mathbf{e}_{\sigma_1} \prod_{i=2}^n a_{i,\sigma_i}
$$

the question is, if A is constructed with the unit vectors forming the first row and n-1 row n-vectors forming the remaining rows, does the determinant and the formula above give the cross product of the n-1 n-vectors.
Where the cross product is a vector that is linearly independent of all n-1 of the input vectors if the input vectors themselves are all linearly independent?



