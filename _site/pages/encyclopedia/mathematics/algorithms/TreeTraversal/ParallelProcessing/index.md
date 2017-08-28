== Organization of the parallel processing of a tree traversal ==

In this discussion, the tree has a finite maximum size that is predetermined, though some branches may be truncated based on the progress of the traversal.

With large trees, there may be insufficient memory to store the information for all tree nodes.
And there may be insufficient processors to compute all lowest-level nodes simultaneously.

To solve the memory issue, the tree can be divided into equally sized sections, where each section is small enough that all of its nodes can be stored in memory.
The sections can be defined by a single depth value, where each node at this depth represents the root (we'll call it subroot) of a subtree that constitutes a section.
There must be enough memory to store this section as well as each ancestor node up to the root of the tree.
In some cases, you must also store all siblings of the subroot.
This would be the case if information from all child nodes is needed in order to calculate the end state of a given node.
