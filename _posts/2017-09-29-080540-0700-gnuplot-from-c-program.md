---
layout: default
date: 2017-09-29 08:05:40 -0700
title: gnuplot from c program
---

How to call gnuplot from a c program

{% highlight c %}
FILE * fp = popen("gnuplot", "w");

fprintf(fp, "plot [0:3.14] sin(x)\n");

// fflush causes gnuplot to read commands
fflush(fp);

// you can continue to write commands and the plot will be updated
fprintf(fp, "plot [0:6.28] sin(x)\n");
fflush(fp);

pclose(fp);
{% endhighlight %}

