---
layout: default
title: complex
---

# complex

## complex power

consider

$$
c_{\mathrm{r}} + i c_{\mathrm{i}} = (a_{\mathrm{r}} + i a_{\mathrm{i}})^{(b_{\mathrm{r}} + i b_{\mathrm{i}})}
$$

$$
c_{\mathrm{r}} + i c_{\mathrm{i}} = e^{\ln{(a_{\mathrm{r}} + i a_{\mathrm{i}})^{(b_{\mathrm{r}} + i b_{\mathrm{i}})}}}
$$

$$
c_{\mathrm{r}} + i c_{\mathrm{i}} = e^{(b_{\mathrm{r}} + i b_{\mathrm{i}}) \ln(a_{\mathrm{r}} + i a_{\mathrm{i}})}
$$

$$
c_{\mathrm{r}} + i c_{\mathrm{i}} = e^{(b_{\mathrm{r}} + i b_{\mathrm{i}}) (\ln a + i \theta_a)}
$$

in terms of transformations: perform natural log transform, rotate by $$b$$, and perform exponential transform.

## natural logarithm of a complex number

first, recall euler's formula

$$
e^{ix} = \cos(x) + i \sin(x)
$$

so

$$
a_{\mathrm{r}} + i a_{\mathrm{i}} 
= 
\sqrt{a_{\mathrm{r}}^2 + a_{\mathrm{i}}^2} e^{i\tan^{-1}{\frac{a_{\mathrm{i}}}{a_{\mathrm{r}}}}} 
= 
a e^{i \theta_a}
$$

so

$$
\ln(a_{\mathrm{r}} + i a_{\mathrm{i}}) = \ln(a e^{i \theta_a})
$$

finally

$$
\ln(a_{\mathrm{r}} + i a_{\mathrm{i}}) = \ln a + i \theta_a
$$

this final form can be thought of as a transformation of the complex plane, just 
as addition and multiplication of complex numbers can be thought of as translation and rotation of
the complex place.

## exponential

$$
e^{(a_{\mathrm{r}} + i a_{\mathrm{i}})}
$$

$$
e^{a_{\mathrm{r}}} e^{i a_{\mathrm{i}}}
$$

$$
e^{a_{\mathrm{r}}} (\cos(a_{\mathrm{i}}) + i \sin(a_{\mathrm{i}}))
$$

$$
e^{a_{\mathrm{r}}} \cos(a_{\mathrm{i}}) + i e^{a_{\mathrm{r}}} \sin(a_{\mathrm{i}})
$$

this too can be thought of as a transformation of the complex plane

## multiplication

$$
(a_{\mathrm{r}} + i a_{\mathrm{i}})(b_{\mathrm{r}} + i b_{\mathrm{i}})
$$

$$
a_{\mathrm{r}} b_{\mathrm{r}} + i a_{\mathrm{i}} b_{\mathrm{r}} + i a_{\mathrm{r}} b_{\mathrm{i}} + i i a_{\mathrm{i}} b_{\mathrm{i}}
$$

$$
a_{\mathrm{r}} b_{\mathrm{r}} - a_{\mathrm{i}} b_{\mathrm{i}} + i (a_{\mathrm{i}} b_{\mathrm{r}} + a_{\mathrm{r}} b_{\mathrm{i}})
$$













