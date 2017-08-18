= Rotation =

{{{#!html
$$
\tau = I \dot{\omega} + \omega \times ( I \omega ) 
$$
}}}

{{{#!html
$$
I \dot{\omega} = \tau - \omega \times ( I \omega )
$$
}}}

{{{#!html
$$
\dot{\omega} = I^{-1} ( \tau - \omega \times ( I \omega ) )
$$
}}}

{{{#!html
$$
I =
\begin{bmatrix}
I_xx & 0 & 0 \\
0 & I_yy & 0 \\
0 & 0 & I_zz
\end{bmatrix}
$$
}}}

== Quaternion ==

{{{#!html
$$
\dot{\mathbf{q}} = \frac{1}{2} \mathbf{A}_3 \boldsymbol\omega
$$
}}}

{{{#!html
$$
\ddot{\mathbf{q}} = \frac{1}{2} (\dot{\mathbf{A}}_3 \boldsymbol\omega + \mathbf{A}_3 \dot{\boldsymbol\omega})
$$
}}}

{{{#!html
$$
\ddot{\mathbf{q}} = 
\frac{1}{2} ( \dot{\mathbf{A}}_3 \boldsymbol\omega
+ \mathbf{A}_3 \mathbf{I}^{-1} \left( \boldsymbol\tau - \boldsymbol\omega \times \left( \mathbf{I} \boldsymbol\omega \right) \right) )
$$
}}}

=== Time Derivative ===

{{{#!html
$$
\dot{q} = \omega q
$$
}}}

{{{#!html
$$
\dot{q}^* = q^* \omega^*
$$
}}}

where

{{{#!html
$$
\omega = \frac{1}{2}
\begin{bmatrix}
0 \\
\omega_x \\
\omega_y \\
\omega_z
\end{bmatrix}
$$
}}}

matrix representation

{{{#!html
$$
\dot{q} =
\begin{bmatrix}
q_0 & -q_1 & -q_2 & -q_3 \\
q_1 & +q_0 & +q_3 & -q_2 \\
q_2 & -q_3 & +q_0 & +q_1 \\
q_3 & +q_2 & -q_1 & +q_0
\end{bmatrix}
\begin{bmatrix}
0 \\
\frac{1}{2} w_0 \\
\frac{1}{2} w_1 \\
\frac{1}{2} w_2
\end{bmatrix}
$$
}}}

{{{#!html
$$
\dot{q} =
\frac{1}{2}
\begin{bmatrix}
-q_1 & -q_2 & -q_3 \\
+q_0 & +q_3 & -q_2 \\
-q_3 & +q_0 & +q_1 \\
+q_2 & -q_1 & +q_0
\end{bmatrix}
\begin{bmatrix}
w_0 \\
w_1 \\
w_2
\end{bmatrix}
$$
}}}

we define matrix construction

{{{#!html
$$
B(q) =
\begin{bmatrix}
-q_1 & -q_2 & -q_3 \\
+q_0 & -q_3 & +q_2 \\
+q_3 & +q_0 & -q_1 \\
-q_2 & +q_1 & +q_0
\end{bmatrix}
$$
}}}

== Euler ==

{{{#!html
$$
\boldsymbol\omega
=
\begin{bmatrix}
1 & 0		& -s_{\boldsymbol\theta} \\
0 & c_{\phi}	& c_{\boldsymbol\theta} s_{\phi} \\
0 & -s_{\phi}	& c_{\boldsymbol\theta} s_{\phi}
\end{bmatrix}
\dot{\boldsymbol\theta} 
= \mathbf{A}_5^{-1} \dot{\boldsymbol\theta}
$$
}}}

{{{#!html
$$
\dot{\boldsymbol\theta} = \mathbf{A}_5 \boldsymbol\omega
$$
}}}

{{{#!html
$$
\ddot{\boldsymbol\theta} = \dot{\mathbf{A}}_5 \boldsymbol\omega + \mathbf{A}_5 \dot{\boldsymbol\omega}
$$
}}}

{{{#!html
$$
\ddot{\boldsymbol\theta}
= \dot{\mathbf{A}}_5 \boldsymbol\omega
+ \mathbf{A}_5 \left(
	\mathbf{I}^{-1} \left( \boldsymbol\tau - \boldsymbol\omega \times \left( \mathbf{I} \boldsymbol\omega \right) \right)
\right)
$$
}}}

{{{#!html
\begin{equation}
\ddot{\boldsymbol\theta} =
\mathbf{S}^{-1} \left(
	\mathbf{I}^{-1} \left( \boldsymbol\tau - \boldsymbol\omega \times \left( I \boldsymbol\omega \right) \right)
	- \dot{\mathbf{S}} \dot{\boldsymbol\theta}
\right)
\label{eq:eom_theta}
\end{equation}
}}}
