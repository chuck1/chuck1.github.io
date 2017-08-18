== In General ==

{{{#!html
$$
M = M_0 + \frac{2 \pi}{T} t
$$
}}}

{{{#!html
$$
t = \frac{T}{2 \pi}(M - M_0)
$$
}}}

== Centered at Focal Point ==

Consider an ellipse with one focal point centered at the origin.
This focal point will be $F_1$ and the other focal point will be $F_2$.
Let $P$ be an arbitrary point on the ellipse.
Let $r$ be the distance from the origin to point $P$.

{{{#!html
$$
r = \frac{a(1-e^2)}{1+e \cos f}
$$
}}}

{{{#!html
$$
r = a(1 - e \cos E)
$$
}}}

where $a$ is the semi-major axis, $e$ is the eccentricity, $f$ is the true anomaly, and $E$ is the eccentric anomaly.
The true anomaly is the angle from the radial of the closest point to the origin to radial of $P$.
A radial is the line from the origin to an arbitrary point on the ellipse.

Let us define $\gamma$ as the angle between the lines from the focal points to point P.
These lines and the line between the two focal points forms a triangle.
Let $\zeta$ be the angle in this triangle opposite side $\overline{F_1P}$.
Note that

{{{#!html
$$
\zeta + \gamma = f
$$
}}}

because $f$ and the angle opposite $\overline{F_2P}$ are supplementary.

Using the law of sines we can write

{{{#!html
$$
\frac{\sin\zeta}{r} = \frac{\sin\gamma}{2c}
$$
}}}

{{{#!html
$$
\frac{\sin(f - \gamma)}{r} = \frac{\sin\gamma}{2c}
$$
}}}

{{{#!html
$$
\frac{\sin f \cos \gamma - \cos f \sin \gamma}{r} = \frac{\sin\gamma}{2c}
$$
}}}

{{{#!html
$$
\frac{\sin f \cos \gamma - \cos f \sin \gamma}{\sin\gamma} = \frac{r}{2c}
$$
}}}

{{{#!html
$$
\sin f \cot \gamma - \cos f = \frac{r}{2c}
$$
}}}


{{{#!html
$$
\cot \gamma = \frac{\frac{r}{2c} + \cos f}{\sin f}
$$
}}}


== Two Ellipses ==

Consider two ellipses like the one defined above, which share a focal point at the origin.
The parameters of the ellipses can differ and they can be rotated relative to one another about the origin.

Let us define a mapping from every point on ellipse A to every point on ellipse B.
Choose a point $P$ on ellipse A. Draw a ray from the origin $O$ to $P$.
Find the point on ellipse B that intersects $\overline{OP}$.
When we refer to pairs of points we are referring to two points, one on each ellipse, that satisfy this definition.

Find all pairs of points for which the tangent lines are parallel.
This will be achieved if $\gamma$ for each of the points is the same.

== Two Orbits ==

{{{#!html
$$
t = \frac{T_A}{2 \pi}(M_A - M_{A,0}) = = \frac{T_B}{2 \pi}(M_B - M_{B,0})
$$
}}}
