---
layout: default
title: triangle of power
---
# triangle of power

See [this math.stackexchange.com question](https://math.stackexchange.com/questions/30046/alternative-notation-for-exponents-logs-and-roots/) and [this youtube video](https://youtu.be/sULa9Lc4pck).

Assuming $$x>0$$ and $$z>0$$

## definition

The triangle

$$
_x\stackrel{y}{\triangle}_z
$$

represents the relationship

$$
x^y = z
$$

## basic equations

power

$$
x^y = {}\stackrel{y}{_x\triangle_{\phantom{z}}}
$$

logarithm

$$
\log_x(z) = {}\stackrel{}{_x\triangle_{z}}
$$

root

$$
\sqrt[y]{z} = \stackrel{y}{_\phantom{x}\triangle_{z}}
$$

## equivalent relations

$$
\begin{array}{rr}

\sqrt[y]{x^y} = x && 
\stackrel{y}{\triangle}_{\stackrel{y}{_x\triangle_{\phantom{z}}}} = x && 
_x\stackrel{y}{\triangle}_{\stackrel{y}{_x\triangle_{\phantom{z}}}}
\\\\

\sqrt[\log_x(z)]{z}=x && 
\stackrel{\stackrel{}{_x\triangle_{z}}}{_\phantom{x}\triangle_{z}} = x &&
\stackrel{\stackrel{}{_x\triangle_{z}}}{_x\triangle_{z}}
\\\\

\log_x(x^y) = y && 
\stackrel{}{_x\triangle_{\stackrel{y}{_x\triangle_{\phantom{z}}}}} = y &&
_x\stackrel{y}{\triangle}_{\stackrel{y}{_x\triangle_{\phantom{z}}}}
\\\\

\log_{\sqrt[y]{z}}(z) = y && 
_{\stackrel{y}{_\phantom{x}\triangle_{z}}}\hspace{-.25pc}\stackrel{}{\triangle_z} = y &&
_{\stackrel{y}{_\phantom{x}\triangle_{z}}}\hspace{-.25pc}\stackrel{y}{\triangle}_z
\\\\

x^{\log_x(z)} = z && 
\stackrel{\stackrel{}{_x\triangle_{z}}}{_x\triangle_{\phantom{z}}} = z &&
\stackrel{\stackrel{}{_x\triangle_{z}}}{_x\triangle_{z}}
\\\\

(\sqrt[y]{z})^y = z && 
_{\stackrel{y}{_\phantom{x}\triangle_{z}}}\hspace{-.25pc}\stackrel{y}{\triangle}=z &&
_{\stackrel{y}{_\phantom{x}\triangle_{z}}}\hspace{-.25pc}\stackrel{y}{\triangle}_z 

\end{array}
$$ 

From the relations above we see that the following rule applies:

> **RULE:** A triangle with **a** in one position and in another position a triangle with **a** in 
> the same position as in the outer triangle and **b** in the position that is empty in the outer 
> triangle is equal to **b**.

Turns out this is true for *any* binary (closed) operator.
Try it out for addition and mulitplication to see for yourself.
We can do a very similar thing for unary operators, but its a bit less interesting.
It is also less interesting for multiplication and addition since those
are commutative.
I think its more interesting for power/logarithm/root because those operations are
non-commutative (though I think it is also interesting here because we have such
poor notation for these things to begin with).
So perhaps this type of notation would also be interesting for other non-commutative
operations like subtraction, division, matrix multiplication, etc.
I should play around with those.
And while we're here are there any trinary operators (we could represent them with a square. surely
we could invent one out of binary operations)?

This rule represents all six of the relations in the center column above.
I will attempt to prove why it is true.

The position of **a** in the outer triangle is the same as the position of **a** in the inner
triangle.
The position of **b** in the inner triangle is the same as the position of the missing element
in the outer triangle.
The position of the inner triangle in the outer triangle is the same as the position of the 
missing element in the inner triangle.
Let **c** be the missing element of the inner triangle. **c** will go into the same position in
the outer triangle as it does in the inner triangle.
So we have two triangles in whose matching position we have **a** and **a**, **c** and **c**, and **b** and blank.
It is obvious that the missing element in the outer triangle, and therefore the value of the whole
expression, is **b**.

I find it very interesting that the proof is independent of the actual positions of **a**, **b**,
and **c**.

## other identities

$$
_x\stackrel{a}{\triangle}_r
$$

$$
_x\stackrel{b}{\triangle}_s
$$

Exponent addition

$$
\stackrel{a}{_x\triangle_{\phantom{z}}} 
\cdot 
\stackrel{b}{_x\triangle_{\phantom{z}}} 
= 
{}\stackrel{a+b}{_x\triangle_{\phantom{z}}}
$$

$$
\stackrel{}{_x\triangle_{rs}}
=
{}\stackrel{}{_x\triangle_{r}}
+
\stackrel{}{_x\triangle_{s}}
$$

For fun

$$
\stackrel{}{_x\triangle_{rs}}
=
\stackrel{}{_x\triangle_{
\stackrel{a}{_x\triangle_{\phantom{z}}} 
\cdot 
\stackrel{b}{_x\triangle_{\phantom{z}}} 
}}
=
\stackrel{}{_x\triangle_{
{}\stackrel{a+b}{_x\triangle_{\phantom{z}}}
}}
=
a + b
$$

$$
{}\stackrel{}{_x\triangle_{r}}
+
\stackrel{}{_x\triangle_{s}}
=
{}\stackrel{}{_x\triangle_{\stackrel{a}{_x\triangle_{\phantom{z}}}}}
+
\stackrel{}{_x\triangle_{\stackrel{b}{_x\triangle_{\phantom{z}}}}}
=
a + b
$$

Exponent subtraction

$$
\frac{\stackrel{a}{_x\triangle_{\phantom{z}}}}{\stackrel{b}{_x\triangle_{\phantom{z}}}}={}\stackrel{a-b}{_x\triangle_{\phantom{z}}}
$$

$$
\stackrel{}{_x\triangle_{a/b}}
=
{}\stackrel{}{_x\triangle_{a}}-\stackrel{}{_x\triangle_{b}}
$$

Untitled 1

$$
_{\stackrel{a}{_x\triangle_{\phantom{z}}}}\hspace{-.25pc}\stackrel{b}{\triangle_{\phantom{z}}} 
=
{}\stackrel{ab}{_x\triangle_{\phantom{z}}}
$$

Untitled 2

$$
\stackrel{}{_x\triangle}_{\stackrel{b}{_a\triangle_{\phantom{z}}}}=b\cdot\stackrel{}{_x\triangle}_{a}
$$

Untitled 4

$$
\stackrel{1/y}{_x\triangle_{\phantom{z}}}=\stackrel{y}{_\phantom{x}\triangle_{x}}
$$

Changing the sign of the exponent

$$
\stackrel{-a}{_x\triangle_{\phantom{z}}}=\frac{1}{\stackrel{a}{_x\triangle_{\phantom{z}}}}
$$

$$
\stackrel{}{_x\triangle_{1/r}}=-\stackrel{}{_x\triangle_{r}}
$$

Untitld 5

$$
\stackrel{}{_a\triangle_{b}}
\cdot
\stackrel{}{_b\triangle_{c}}
=
\stackrel{}{_a\triangle_{c}}
$$

$$
\stackrel{}{_a\triangle_{c}}
=
\frac
{\stackrel{}{_b\triangle_{c}}}
{\stackrel{}{_b\triangle_{a}}}
$$

Combining gives

$$
\stackrel{}{_a\triangle_{b}}
\cdot
\stackrel{}{_b\triangle_{c}}
=
\frac
{\stackrel{}{_b\triangle_{c}}}
{\stackrel{}{_b\triangle_{a}}}
$$

$$
\stackrel{}{_a\triangle_{b}}
=
\frac
{1}
{\stackrel{}{_b\triangle_{a}}}
$$

Equivalently

$$
_a\stackrel{d}{\triangle}_b \Longleftrightarrow {} _b\stackrel{1/d}{\triangle}_a
$$

This interesting looking relation is actually something we're all very familiar with

$$
\sqrt[d]{b} = b^{1/d}
$$



