---
layout: default
---

# N-Dimensional Game

 * [voronoi clip](voronoi_clip)
 * [physics](physics)

# N-Dimensional Visualization

## Outline

The general process of visualization is as follows

* define model space geometry
* define and apply model-view-projection matrix
* drop higher dimensions
* render resulting 3D geometry directly

### Define Model Space Geometry

Start with a unit shape.
An N-dimensional shape can be defined as a collection of (N-1)-dimensional shapes.
This can be broken down into a collection of N-dimensional vertices that are connected to form N-dimensional triangles.
To render these triangles, we will rotate the vertices to be aligned with the view-space and then disregard the higher dimensions.

Define a model transformation which includes rotation, translation, and scaling.
Apply this transformation to get the model-space geometry.

### Define Model-View Matrix

The model-view matrix is constructed from N linearly independent vectors that form the view-space coordinates.
The first of these vectors is always the view-vector, which is the vector from the eye point to the center point.
The other N-2 vectors define the orientation, and the last vector is simply the cross product of the other N-1 vectors.

### Define Projection Matrix 

A higher-dimensional counterpart to the projection can be constructed and applied. This projection can be either parallel or perspective.

### Render the 3-Dimensional Scene 

After applying the model-view and projection matrix to the higher-dimensional shape, we are left with a 3-dimensional shape that is ready to be rendered directly.
Since the higher-dimensional model-view-projection matrix is already applied, we do not need the usual MVP matrix in the vertex shader.

### Lighting 

Lighting will be applied in higher dimensions using ray-tracing. For The N-dimensional rays will be cast from the eye point or the screen point depending on the type of projection.
The mathematics for detecting intersection and reflection and refraction angles should translate nicely to N-dimensions, I hope.

## 4D transformation matrix

A 4D rotation matrix is similar to its 3D counterpart. It is a 4-matrix and can be used to rotate vectors.
A vector $$\mathbf{v}$$ can be rotated to a new vector $$\mathbf{v'}$$ by

$$\mathbf{v'} = \mathbf{M} \mathbf{v} $$

where $$\mathbf{M}$$ is the rotation matrix.

== 4D model space to 4D eye space ==

Before projecting from 4D to 3D, we will transform the 4D scene to be oriented relative to the eye coordinates.
Later, this will allow use to simplify the projection from 4D to 3D.

The transformation is accomplished by constructing a transformation matrix using the four linearly-independent 4-vectors that define the eye-coordinates.

The transformation matrix is composed of the column vectors $$\mathbf{A}$$, $$\mathbf{B}$$, $$\mathbf{C}$$ and $$\mathbf{D}$$.

$$\mathbf{D} = \wedge (\mathbf{c}-\mathbf{e}) $$

where we define $$\wedge$$ as the normalization operator.

$$\mathbf{A} = \wedge ( \otimes ( \mathbf{u}, \mathbf{o}, \mathbf{D} ) ) $$

$$\mathbf{B} = \wedge ( \otimes ( \mathbf{o}, \mathbf{D}, \mathbf{A} ) ) $$

$$\mathbf{C} = \wedge ( \otimes ( \mathbf{D}, \mathbf{A}, \mathbf{B} ) ) $$

where $$\mathbf{c}$$ is the center point, $$\mathbf{e}$$ is the eye point, $$\mathbf{u}$$ is the up vector and $$\mathbf{o}$$ is the over vector.
The constructed rotation matrix is applied by

$$\mathbf{v'} = \mathbf{M} (\mathbf{v} - \mathbf{c})$$

## 4D to 3D Projection 

The projecting from 4D to 3D is analogous to that from 3D to 2D.
For 3D to 2D, we define a 2-space in 3D on which to project the 3D verticies.
So for 4D to 3D, we define a 3-space in 4D on which to project 4D verticies.
In general, we can define this surface by

$$\mathbf{n} \cdot \mathbf{p} = d$$

where $$\mathbf{n}$$ is the 4D normal vector of the 3-space and $$\mathbf{p}$$ is a point on the 3-space.
As with 3D to 2D, the projection can be parallel or perspective.

### Parallel Projection 

To project to a 4-vertex $$\mathbf{p}$$, we calculate the intersection of a ray with origin $$\mathbf{p}$$ and direction $$-\mathbf{n}$$ with the 3-space defined above.

$$\mathbf{n} \cdot \mathbf{p^*} = \mathbf{n} \cdot (\mathbf{p} + k \mathbf{n}) = d$$

$$ \mathbf{n} \cdot \mathbf{p} + \mathbf{n} \cdot (k \mathbf{n}) = d $$

$$ \mathbf{n} \cdot (k \mathbf{n}) = d - \mathbf{n} \cdot \mathbf{p} $$

$$ k = \frac{d - \mathbf{n} \cdot \mathbf{p}}{\mathbf{n} \cdot \mathbf{n}} $$

If $$k$$ is positive, the vertex is behind the viewing 3-space.

### Perspective 

For perspective, the projected point is the intersection of the viewing 3-space with a ray from the eye point to the vertex.

$$\mathbf{n} \cdot \mathbf{p^*} = \mathbf{n} \cdot (\mathbf{p} + k (\mathbf{p} - \mathbf{e})) = d$$

$$\mathbf{n} \cdot \mathbf{p} + \mathbf{n} \cdot k (\mathbf{p} - \mathbf{e}) = d$$

$$ \mathbf{n} \cdot k (\mathbf{p} - \mathbf{e}) = d - \mathbf{n} \cdot \mathbf{p}$$

$$ k = \frac{d - \mathbf{n} \cdot \mathbf{p}}{\mathbf{n} \cdot (\mathbf{p} - \mathbf{e})}$$