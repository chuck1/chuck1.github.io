---
layout: default
title: six arm platform
---
# six arm platform

The goal is to design and build a machine consisting of a base, a tool platform, and six arms.
The arms connect the base and the tool.
At each arm's connection to the base and to the tool is a joint with zero DOF for linear 
motion but three DOF for rotation.

The base is considered fixed.
The arms fix the position and orientation of the tool.
The length of each arm is adjustable.
By changing the length of each arm, the position and orientation of the tool changes.

Let $$o_i$$ be the point where arm $$i$$ connects to the base.
Let $$p_i$$ be the point where arm $$i$$ connects to the tool.

## controlling tool position and orientation

If the base position of each arm and the starting position of the tool are known, control
of the position and orientation of the tool is simple.
For each arm, calculate the distance between points $$o$$ and $$p$$.
This is the new length of the arm, simply adjust the length of the arm to match.

## adjusting arm length

Many mechanisms could be used for adjusting the length of the arms.

The method of choice for my build will be lead screws.
At each joint, there will be only two rotational DOF.
At the tool end, a stepper motor will be mounted to a pivot.
The motor will be connected directly to the screw.
At the base end, the nut will be fixed to a pivot.
As the motor turns, the screw will rotate relative to the nut (this is why the pivots must only have
two rotational DOF) changing the length of the arm.

## description of operation

The platform will be controlled by an arduino. The arduino will receive gcode commands from a computer by serial communication.


