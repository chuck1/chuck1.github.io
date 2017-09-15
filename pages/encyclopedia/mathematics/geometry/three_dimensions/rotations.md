
thinking about rotation are circles drawn on the inside of a sphere
-------------------------------------------------------------------

Image our object is centered inside a sphere.
Our object has a local coordinate system so we can think of the object as
having a direction it is facing.
We can create a facing vector.
This vector points to a point on the sphere.
As the object rotates about a fixed axis, this point traces a circle on the inside surface
or our sphere.
Depending on the angle between our facing vector and the rotation axis,
the diameter of that circle changes.

We can think of orientation as a combination of a facing vector (or a point on the sphere)
and an additional rotation about the facing vector (roll).

If we are trying to rotate our object from one orientation to another,
we can think about all the possible circles we could trace
between the two points on the sphere.

Since we can think of a circle drawn on the surface of a sphere as
the intersection of a sphere and a plane, we generate all possible
circles by creating a plane that lies on the straight like between 
the two points on the sphere and rotating the plane one complete revolution
around that straight line.

If we could visualize the circle that this intersection makes as
we rotate the plane, we would see that near either point, the circle
looks like a line going through the point in a specific direction and that that
direction goes through a complete revolution around the point.

The angle that the circle makes with the point is related to the additional rotation about the facing
vector that we mentioned above.
This should be sufficient proof that rotation about a fixed axis can transform any orientation into any other
orientation.


