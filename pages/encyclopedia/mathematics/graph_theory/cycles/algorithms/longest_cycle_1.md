---
layout: default
---

# finding the longest cycle using lp-relaxation

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








