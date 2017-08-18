---
layout: default
---


$$
\lim_{x\to\infty} \left( \frac{x+a}{2} - \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} \right)
$$


Rearrange the function


$$
\frac{x+a}{2} - \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} 
\left(\frac{\frac{x+a}{2} + \sqrt{\left(\frac{x+a}{2}\right)^2 - abx}}{\frac{x+a}{2} + \sqrt{\left(\frac{x+a}{2}\right)^2 - abx}}\right)
$$



$$
\frac
{ \left(\frac{x+a}{2}\right)^2 - \left(\frac{x+a}{2}\right)^2 + abx }
{ \frac{x+a}{2} + \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} }
$$




$$
\frac
{ abx }
{ \frac{x+a}{2} + \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} }
$$


Back to taking the limit


$$
\lim_{x\to\infty} \left(
\frac
{ abx }
{ \frac{x+a}{2} + \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} }
\right)
$$


LHopitals Rule


$$
\lim_{x\to\infty} \left(
\frac
{ \frac{d}{dx} abx }
{ \frac{d}{dx} \frac{x+a}{2} + \frac{d}{dx} \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} }
\right)
$$



$$
\lim_{x\to\infty} \left(
\frac
{ ab }
{ \frac{1}{2} 
+ \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} }
\right)
$$


Moving the limit inside


$$
\frac
{ ab }
{ 
\frac{1}{2} 
+ \lim \left( \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} \right) 
}
$$


Lets look at the limit in the denominator


$$
\lim \left( \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} \right) 
$$


Again apply LHopitals Rule


$$
\lim \left( 
\frac{ \frac{1}{2} }
{2 \frac{d}{dx} \sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} 
\right) 
$$


Move the limit inside


$$
\frac{ \frac{1}{2} }
{
2 \lim \left( \frac{d}{dx} \sqrt{\left(\frac{x+a}{2}\right)^2 - abx} \right) 
} 
$$



$$
\frac{ \frac{1}{2} }
{
2 \lim \left( \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} \right) 
} 
$$


Notice that we now have a repeating fraction


$$
\lim \left( \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} \right) =
\frac{ \frac{1}{2} }
{
2 \lim \left( \frac{\frac{x+a}{2} - ab}{2\sqrt{\left(\frac{x+a}{2}\right)^2 - abx}} \right) 
} 
$$



$$
y =
\frac{ \frac{1}{2} }
{2 y } 
$$



$$
y = \frac{1}{2} 
$$


Apply this to the original limit


$$
\frac
{ ab }
{ 
\frac{1}{2} 
+ \frac{1}{2} } = ab
$$

