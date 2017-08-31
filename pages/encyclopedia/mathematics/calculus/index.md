---
layout: default
---

# calculus

* [sensitivity analysis](sensitivity_analysis)

## rules

### chain rule

$$
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
$$

### product rule

$$
\frac{d}{dx} (f(x) g(x)) = f(x) g'(x) + g(x) f'(x)
$$

### derivative with respect to a function

$$
\frac{d}{df} y
$$

I am not clear on how to handle this situation.

I hypothesize that the result depends on whether or not $$f$$ is a function of $$y$$.
And that if $$f$$ is a function of $$y$$, it implies that $$y$$ is a function of $$f$$.

We know that if $$f$$ is not a function of $$y$$

$$
\frac{df}{dy} = 0
$$

It may be helpful to stop thinking about variables as being different that functions of variables.

I can show for some examples that 

$$
\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}
$$

where

$$
y = f(x)
$$

Here are the examples

$$
y = ax
$$

$$
\frac{dy}{dx} = a
$$

$$
x = \frac{1}{a} y
$$

$$
\frac{dx}{dy} = \frac{1}{a}
$$

And another

$$
y = e^x
$$

$$
\frac{dy}{dx} = e^x
$$

$$
x = \ln(y)
$$

$$
\frac{dx}{dy} = \frac{1}{y} = \frac{1}{e^x}
$$

What if $$x$$ and $$y$$ are inseparable?

$$
y = x + e^x
$$

$$
dy = dx + e^x dx
$$

$$
\frac{dy}{dx} = 1 + e^x
$$

$$
\frac{dx}{dy} = \frac{1}{1 + e^x}
$$











