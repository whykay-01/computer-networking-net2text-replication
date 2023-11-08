"""
ComPass "Computing Path Specifications" (R, q1,...,ql, k, t)

INPUT: 
R: a set of routing paths.
q1,...,ql: a set of feature functions.
k: limit on the number of specifications.
t: limit on the size of specifications.

OUTPUT:
A set of specifications S.
"""

def compute_candidate_features(R, q, t):
    Q = set()
    for r in R:
        for i in range(len(r)):
            for j in range(i+1, len(r)):
                if len(r[i:j]) <= t:
                    Q.add(q(r[i:j]))
    return Q


def compute_specifications(Q, S):
    L = set()
    for f in Q:
        if all([not (f <= s) for s in S]):
            L.add(f)
    return L

def ComPass(R, q, k, t):
    S = set() # The specifications set
    while len(S) < k:
        # Compute the candidate features
        q, v = compute_candidate_features(R, q, t) #TODO: Fix this
        # Compute the specifications
        L = L.union(v)
        Q = Q.difference(q)
        R = R.difference(v) #TODO: Fix this
        # Add the specifications to the specifications set
        if len(L) == t:
            S = S.union(L)
            break
        while len(L) > 0:
            # Add the specification with the highest score to the specifications set
            f = max(L, key=lambda f: f.score())
            S.add(f)
            # Remove all specifications that are subsumed by f
            L = set([f for f in L if not (f <= s)])
        S = S.union(L)
    return S


