---
layout: default
---

# snap

Rotate a vector from body to global frame

$$
\mathbf{y} = \mathbf{q}^* \left( \mathbf{x} \right) \mathbf{q}
$$

$$
\dot{\mathbf{y}} = \mathbf{q}^* \left( \dot{\mathbf{x}} + \mathbf{x} \times \boldsymbol{\omega} \right) \mathbf{q}
$$

$$
\ddot{\mathbf{y}} = 
\mathbf{q}^* 
\left( \frac{d}{dt} \left( \dot{\mathbf{x}} + \mathbf{x} \times \boldsymbol{\omega} \right) + \left(\dot{\mathbf{x}} + \mathbf{x} \times \boldsymbol{\omega} \right) \times \boldsymbol{\omega} \right) 
\mathbf{q}
$$

$$
\ddot{\mathbf{y}} = \mathbf{q}^* \left(
\frac{d}{dt} \left( \dot{\mathbf{x}} \right) +
\frac{d}{dt} \left( \mathbf{x} \times \boldsymbol{\omega} \right) +
\dot{\mathbf{x}} \times \boldsymbol{\omega} +
\left(\mathbf{x} \times \boldsymbol{\omega} \right) \times \boldsymbol{\omega}
\right) \mathbf{q}
$$

$$
\ddot{\mathbf{y}} = \mathbf{q}^* \left(
\ddot{\mathbf{x}} +
\dot{\mathbf{x}} \times \boldsymbol{\omega} +
\mathbf{x} \times \dot{\boldsymbol{\omega}} +
\dot{\mathbf{x}} \times \boldsymbol{\omega} +
\left(\mathbf{x} \times \boldsymbol{\omega} \right) \times \boldsymbol{\omega}
\right) \mathbf{q}
$$

$$
\ddot{\mathbf{y}} = \mathbf{q}^* \left(
\ddot{\mathbf{x}} +
2 \left( \dot{\mathbf{x}} \times \boldsymbol{\omega} \right) +
\mathbf{x} \times \dot{\boldsymbol{\omega}} +
\left(\mathbf{x} \times \boldsymbol{\omega} \right) \times \boldsymbol{\omega}
\right) \mathbf{q}
$$

### State Space

No integral control

$$
x =
\begin{bmatrix}
\dddot{x} \\
\ddot{x} \\
\dot{x} \\
x
\end{bmatrix}
$$

$$
A =
\begin{bmatrix}
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

$$
E =
\begin{bmatrix}
c_4 & c_3 & c_2 & c_1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\dot{x} = (A-E)x +
\begin{bmatrix}
c_1 \\
0 \\
0 \\
0
\end{bmatrix}
$$





