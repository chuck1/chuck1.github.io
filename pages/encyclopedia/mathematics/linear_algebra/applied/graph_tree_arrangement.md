---
layout: default
---

arranging the nodes of a tree graph
===================================

For every branch node (including the root) there is a set of variables representing the angle 
allocated to each of its child nodes. The sum of these angles is equal to the angle that was
allocated to this branch node by its parent. If this branch node is the root nodes, the angles
sum to 360 degrees instead.

We will define linear program

$$
\mathrm{maximize} ( \mathbf{c}^{\mathbf{T}} \mathbf{x} )
$$

$$
\mathbf{A} \mathbf{x} \le \mathbf{b}
$$

where $$\mathbf{x}$$ is a vector of all the angles described above and $$\mathbf{A}$$ and 
$$\mathbf{b}$$ define the relationships between angles described above.

Let the angle $$x_i$$ be the angle allocated to the children of a given node.
Lets say this node has $$n_i$$ children and the children will lie on radius $$r_i$$.
The arc length between adjecent children will be 

$$
l_i = \frac{x_i r_i}{n_i}
$$

We will say

$$
\mathbf{c}^{\mathbf{T}} \mathbf{x} = \mathbf{l}
$$

so

$$
c_i = \frac{r_i}{n_i}
$$

We are therefore trying to maximum the sum of the arc lengths between child nodes of each branch node.


