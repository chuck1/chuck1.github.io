
I hypothesize that the mathematics of solid body collisions could be translated to N-dimensional.
Another question is that of player input.
In a 3-DOF game, the player requires 3 axes or 6 discrete inputs to apply force or rotation in 3-dimensions.
Adding more controls to be able to simultaneously apply force and torque in all directions would be overwhelming beyond perhaps 4 dimensions.
It may be best to give the player 3-DOF but allow him/her to quickly remap which directions are controlled which which control axes.

= Rigid Body Kinetics =

From my old quadrotor docs:

{{{#!html
$$
\dot{\mathbf{q}} = \mathbf{A}_3 \boldsymbol\omega
$$
}}}

{{{#!html
$$
\ddot{\mathbf{q}} = \dot{\mathbf{A}}_3 \boldsymbol\omega + \mathbf{A}_3 \dot{\boldsymbol\omega}
$$
}}}

{{{#!html
$$
\ddot{\mathbf{q}}
= \dot{\mathbf{A}}_3 \boldsymbol\omega
+ \mathbf{A}_3 \mathbf{I}^{-1} \left( \boldsymbol\tau - \boldsymbol\omega \times \left( \mathbf{I} \boldsymbol\omega \right) \right)
$$
}}}


== Player Input ==

Another question is that of player input.
In a 3-DOF game, the player requires 3 axes or 6 discrete inputs to apply force or rotation in 3-dimensions.
Adding more controls to be able to simultaneously apply force and torque in all directions would be overwhelming beyond perhaps 4 dimensions.
It may be best to give the player 3-DOF but allow him/her to quickly remap which directions are controlled which which control axes.
