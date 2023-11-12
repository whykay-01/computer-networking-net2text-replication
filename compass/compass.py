"""
ComPass "Computing Path Specifications" (R, q1,...,ql, k, t)

INPUT: 
R: a set of routing paths.
q1,...,ql: a set of feature functions.
k: maximal number of specifications.
t: maximal size of each specification.

OUTPUT:
A set of specifications S.
"""

def argmax(): # greedy, maximal increase in score
    return None, None

def ComPass(R, q, k, t):
    S = set() # The specifications set, set of solutions
    L = set() # The last computed specification
    Q = q # The set of candidate features
    while len(S) < k:
        # Compute the candidate features
        q, v = argmax(R, q, t) # compute_candidate_features(R, q, t) #TODO: Fix this
        # Compute the specifications
        L = L.union(set(v))
        Q = Q.difference(q)
        R = R.difference(v) # Eliminate routing path that won't satisfy feature values
        # Add the specifications to the specifications set
        if len(L) == t:
            S = S.union(L)
            break

        while len(L) > 0: # Add specification for a higher score even though same path
            L = L.union(set(v)) # Add the specification with the highest score to the specifications set
            if len(L) == t:
                S.add(set(L))
                break
            Q = Q.difference(set(q))
            # Remove all specifications that are subsumed by f
        S = S.union(L)
    return S


