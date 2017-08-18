---
layout: default
title: Haskell
---

# Haskell


{% highlight haskell %}
foldl' :: (a -> b -> b) -> b -> [a] -> b
foldl' f b []     = b
foldl' f b (a:as) = f a (foldl' f b as)
{% endhighlight %}

{% highlight haskell %}
> foldl' (+) 0 [1,2,3,4]
10
{% endhighlight %}

{% highlight haskell %}
foldl' (+) 0 [1,2,3,4]
(+) 1 (foldl' (+) 0 [2,3,4])
(+) 1 ((+) 2 (foldl' (+) 0 [3,4]))
(+) 1 ((+) 2 ((+) 3 (foldl' (+) 0 [4])))
(+) 1 ((+) 2 ((+) 3 ((+) 4 (foldl' (+) 0 []))))
(+) 1 ((+) 2 ((+) 3 ((+) 4 (0))))
{% endhighlight %}

