---
layout: default
---

## Conductor

### Bottlenecks

When you have a block, the maximum throughput of that block is equal to the throughput
of a straight rail.
So if you have a simple crossing, the total throughput of the lines goings into the crossing
is now limited to the throughout of a single rail!
This will require more parallel lines.
But keep in mind that we cannot have lines that divrege and converge, a line must have a single viable
path in order for Conductor to work.

Large merge junctions make things even more complicated.
Tests have shown that when merging two groups of N parallel tracks into N output tracks.
If you allow for a complex array of crossings, the throughput is limited only by the number of output tracks.
This will be very useful for converging and diverging lines at subfactories.


## Factory

![](factory_rail.svg)

### Downstream Train Departing The Subfactory

A train at a subfactory stop that is scheduled to head downstream will depart when

* it has unloaded all of the items it intended to unload
* OR the chests to which it is unloading are full (circuit condition)

It will then head to the downstream waiting area.
Here it will wait to be scheduled on the main line.

At its destination, it will wait in the upstream waiting area.
It will wait here until it is requested by a subfactory stop.
A stop will request trains carrying specific items based on what items the stop needs.
So if the recipe is A and B make C, there could be one route delivering A and another delivering B.
If the stop is low on A and not B, it will request a train carrying A.

We must also consider the case in which a train is unloading item A and loading item C.
Lets say for some reason the factory has an excess of item A.
So no trains carrying A will be requested.
But the route that takes C downstream also delivers A.
So we need to make room on a train carrying A so that it can load C and take it downstream.
To know if this is necessary, we must look at the factories that need C.
We can look at each of those factories and see if the total C in their chests is below a set point.
If their demand cannot be filled by trains that are waiting to go directly to those factories, they can request a train like this one.

Maybe the method described in the paragraph above is too complicated.
Perhaps with our conductor mod, the throughput of rails, even when they have many crossings, will be high enough
that it is better to just have trains with two destinations and a single item.
Simpler is almost always better afterall.


