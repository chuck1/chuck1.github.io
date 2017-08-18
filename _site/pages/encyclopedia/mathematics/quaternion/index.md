= Quaternion =

Multiplication of two quaterions

{{{#!html
$$
ab = (a_s b_s - a_v \cdot b_v) + (a_s b_v + a_v b_s + a_v \times b_v)
$$
}}}

{{{#!html
\begin{align}
ab = &(a_1 b_1 - a_2 b_2 - a_3 b_3 - a_4 b_4) \\
+ &(a_1 b_2 + a_2 b_1 + a_3 b_4 - a_4 b_3)i \\
+ &(a_1 b_3 - a_2 b_4 + a_3 b_1 + a_4 b_2)j \\
+ &(a_1 b_4 + a_2 b_3 - a_3 b_2 + a_4 b_1)k
\end{align}
}}}


== Matrix Representaion ==

Define

{{{#!html
$$
A(a) =
\begin{bmatrix}
a_1 & -a_2 & -a_3 & -a_4 \\
a_2 &  a_1 & -a_4 &  a_3 \\
a_3 &  a_4 &  a_1 & -a_2 \\
a_4 & -a_3 &  a_2 &  a_1
\end{bmatrix}
$$
}}}

where $a$, $b$, $c$, and $d$ are the components of a quaterion.

{{{#!html
$$
A =
\begin{bmatrix}
a_1 & -a_2 & -a_3 & -a_4 \\
a_2 &  a_1 & -a_4 &  a_3 \\
a_3 &  a_4 &  a_1 & -a_2 \\
a_4 & -a_3 &  a_2 &  a_1
\end{bmatrix}
\begin{bmatrix}
b_1 \\
b_2 \\
b_3 \\
b_4
\end{bmatrix}
$$
}}}

=== Multiplication ===

If we have quaternion multiplication

{{{#!html
$$
ab = c
$$
}}}

this can be written as matrix-vector multiplication

{{{#!html
$$
A b = c
$$
}}}
