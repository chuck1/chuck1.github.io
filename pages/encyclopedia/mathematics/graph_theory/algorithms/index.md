---
layout: default
---

 * [cycles in undirected graph](cycles_in_undirected_graph)

## method for finding interesting edge subsets

Here we develop general methods for finding all subsets in a family of subsets of graph elements.
For example, these families could be simple cycles, cycles, simple paths, or paths.

Define a function $$f$$ of element (vertex or edge) $$x$$ such that we can prove that $$f$$ will return all 
solutions that contain $$x$$ and no solutions that contain $$y | y < x$$.
You can easily see that evaluating $$f$$ for each $$x$$ in the graph, we will obtain all solutions 
with no repeated solutions.

The challenge now is to find $$f$$ that satisfies the above.

Here is an attempt to write out these ideas using mathematical notation:

**THEOREM**

If $$f(x) = \{ s | x \in s, y \notin s, y < x \}$$ where $$s \in S$$ and $$S$$ is the set of
all solutions, then $$\bigcup \textrm{F}(x) = S$$ and 
$$\textrm{F}(x) \cap \textrm{F}(y) = \emptyset, x \neq y$$.

**PROOF**

$$
\bigcup_{y < x} f(y) \cup f(x) = 
\{ s | y \in s, y \lt x \} \cup
\{ s | x \in s, y \notin s, y < x \} =
\{ s | y \in s, y \le x \}
$$

$$
\bigcup_{y < x} f(y) \cap f(x) = 
\{ s | y \in s, y \lt x \} \cap
\{ s | x \in s, y \notin s, y < x \} =
\emptyset
$$

**END**

### Depth First Search

Here we define a function that will serve as a recursive component of $$f$$ using a depth-first-search algorithm.

**ALGORITHM**

    function g(e0, e, Q, f1, f2)
        e is an edge that temporarily points from v0 to v1
        Q is a sequence of edges. Q contains e.
        
        for each edge e1 adjacent to v1
            if Q contains e1 then continue
            
            add e1 to the end of Q
            
            orient e1 such that its tail is at v1

            add f1(e0, e1, Q) to S

            if f2(e0, e1, Q) evaluates true then
                g(e0, e1, Q, f1, f2)
        
            remove e from the end of Q
       
### cycles

We define the functions $$f_1$$ and $$f_2$$ for finding cycles using the above DFS algorithm

    function f1(e0, e1, Q)

        if e1 < e0 then return

        if tail(e0) == head(e1) then
            Q is a cycle, add it to the return set

and

    function f2(e0, e1, Q)
        if(e1 < e0) then
            return false
        else
            return true



 
