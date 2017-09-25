---
layout:default
---

Rotate a vector from body to global frame

\[
\V{y} = \V{q}^* \left( \V{x} \right) \V{q}
\]

\[
\Vd{y} = \V{q}^* \left( \Vd{x} + \V{x} \times \G{\omega} \right) \V{q}
\]

\[
\Vdd{y} = \V{q}^* \left( \frac{d}{dt} \left( \Vd{x} + \V{x} \times \G{\omega} \right) + \left(\Vd{x} + \V{x} \times \G{\omega} \right) \times \G{\omega} \right) \V{q}
\]

\[
\Vdd{y} = \V{q}^* \left(
\frac{d}{dt} \left( \Vd{x} \right) +
\frac{d}{dt} \left( \V{x} \times \G{\omega} \right) +
\Vd{x} \times \G{\omega} +
\left(\V{x} \times \G{\omega} \right) \times \G{\omega}
\right) \V{q}
\]

\[
\Vdd{y} = \V{q}^* \left(
\Vdd{x} +
\Vd{x} \times \G{\omega} +
\V{x} \times \Gd{\omega} +
\Vd{x} \times \G{\omega} +
\left(\V{x} \times \G{\omega} \right) \times \G{\omega}
\right) \V{q}
\]

\[
\Vdd{y} = \V{q}^* \left(
\Vdd{x} +
2 \left( \Vd{x} \times \G{\omega} \right) +
\V{x} \times \Gd{\omega} +
\left(\V{x} \times \G{\omega} \right) \times \G{\omega}
\right) \V{q}
\]

\paragraph{State Space}

No integral control

\[
x =
\begin{bmatrix}
\dddot{x} \\
\ddot{x} \\
\dot{x} \\
x
\end{bmatrix}
\]

\[
A =
\begin{bmatrix}
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\]

\[
E =
\begin{bmatrix}
c_4 & c_3 & c_2 & c_1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\]

\[
\dot{x} = (A-E)x +
\begin{bmatrix}
c_1 \\
0 \\
0 \\
0
\end{bmatrix}
\]




