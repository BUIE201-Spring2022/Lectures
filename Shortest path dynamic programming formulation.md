# Shortest path: dynamic programming formulation

## Bellman's principle of optimality

Suppose s > --- > u > --- > v is a shortest path from s to v. This implies that s > --- > u is a shortest path from s to u.

### Proof

This can be proven by contradiction. If there is a shorter path between s and u, we can replace s > --- > u with the shorter path in s > --- > u > --- > v, and this would yield a better path between s and v. But we assumed that
s > --- > u > --- > v is a shortest path between s and v, so have a contradiction.

## Formulation

Let G = (N, A) be a graph with node set N and arc set A. Let d(u, v) > 0 be the length of the arc (u, v) in A.

Define SP(s, v) as the length of the shorthest path between nodes s and v for and s and v in N:

SP(s, v) = min { SP(s, u) + d(u, v) | (u, v) in A }

SP(s, s) = 0

## Discussion point

Discuss the need for a stopping condition for the recursive formula.
