---
layout: default
---

# Spaces

To help up keep track of spaces, we will denote them by $$S_i$$ where $$i$$ is the number of dimensions in the space.

An $$(i,i-1)$$-subspace can be parameterized as

$$
\mathbf{s_i} = \mathbf{p} + \mathbf{A} \mathbf{s_{i-1}} 
$$

You can see that this acts as a transformation from $$S_{i-1}$$ to $$S_i$$.

A hyperplane in $$S_i$$ is given by

$$
\mathbf{n} \cdot \mathbf{s_i} = d
$$

Combine to get

$$
\mathbf{n} \cdot (\mathbf{p} + \mathbf{A} \mathbf{s_{i-1}}) = d
$$

$$
\mathbf{n} \cdot \mathbf{p} + \mathbf{n} \cdot (\mathbf{A} \mathbf{s_{i-1}}) = d
$$

$$
\mathbf{n} \cdot (\mathbf{A} \mathbf{s_{i-1}}) = d - \mathbf{n} \cdot \mathbf{p}
$$

$$
(\mathbf{A}^T \mathbf{n}) \cdot \mathbf{s_{i-1}} = d - \mathbf{n} \cdot \mathbf{p}
$$

This takes the form of a plane in $$S_{i-1}$$.
We can use this plane to creates a subspace that connects $$S_{i-1}$$ and $$S_{i-2}$$.

## Bounding

For practical uses, we need to bound subspaces using features from higher dimensions.
For example, we may want to bound an $$(i,i-1)$$-subspace using a plane in $$S_i$$.
Above we see that the intersection of these features creates a plane in $$S_{i-1}$$.



