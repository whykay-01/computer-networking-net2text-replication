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

def argmax(Q, L, R, t):
    max_score = -float('inf')
    best_feature = None
    best_value = None
    for q in Q:
        if len(L) == t:
            break
        S = L.union({q})
        score = 0
        for r in R:
            if set(r).issuperset(S):
                score += 1
        if score > max_score:
            max_score = score
            best_feature = q
            best_value = S.intersection(set(r))
        # Compute the score of the candidate feature and update the best feature and value
        # if the score is higher than the current maximum
    return best_feature, best_value

def ComPass(R, q, k, t):
    S = set() # The specifications set, set of solutions
    L = set() # The last computed specification
    Q = q # The set of candidate features
    while len(S) < k:
        # Compute the candidate features
        q, v = argmax(Q, L, R, t)
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