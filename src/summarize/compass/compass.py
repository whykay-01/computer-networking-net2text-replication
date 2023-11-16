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

import sqlite3

# how to score the functions????????
def argmax(Q, L, R, t):
    print("inputs:", Q, L, t)
    max_score = -float('inf')
    best_feature = None
    best_value = None # what is the feature value
    for q in Q:
        if len(L) == t:
            break
        S = L.union({q})
        print("spec set:", S)
        # Feature scoring function
        score = 0
        for r in R:
            r = r.split(" -> ")
            if set(r).issuperset(S): # if the path contains the feature, but that's not what it does
                score += 1
        if score > max_score:
            max_score = score
            best_feature = q
            best_value = score
            print("best feature:", best_feature, "best value:", best_value)
        # Compute the score of the candidate feature and update the best feature and value
        # if the score is higher than the current maximum
    print(best_feature, best_value)
    return best_feature, best_value

def ComPass(R, q, k, t): # R: set of strings, q: set, k: int, t: int
    S = set() # The specifications set, set of solutions
    L = set() # The last computed specification
    Q = q # The set of candidate features
    while len(S) < k:
        # Compute the candidate features
        q, v = argmax(Q, L, R, t)
        L = L.union({v})
        Q = Q.difference(q)
        R = R.difference({v}) # Eliminate routing path that won't satisfy feature values
        # Add the specifications to the specifications set
        if len(L) == t:
            S = S.union(L)
            break
        
        while True: # TODO: Add specification for a higher score even though same path
            L = L.union({v}) # Add the specification with the highest score to the specifications set
            if len(L) == t:
                S.add(set(L))
                break
            Q = Q.difference(q) # Remove the feature from the candidate features
        S = S.union(L)
    return S

if __name__ == "__main__":
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    routing_paths = set()
    for row in cur.execute('SELECT path FROM network;'):
        routing_paths.add(row[0])
    
    ss = ComPass(routing_paths, {"egress", "ingress","shortest_path", "org"}, 3, 4)
    print(ss)
    con.close()

    # Consider R = {(Google, P_i)}^100 i=1. each with weight 1, and k=t=2.
    # E(Google, P_i) = NY_e and E(Google, P_i) = LA_e otherwise....
    # feature values should be a key value pair

    # path is a list of STRINGS (even if they look like ints)

"""
return should look something like this:
compass_result = [['60', {'egress': "NY"}], 
                  ['40', {"egress": "Washington"}], 
                  ['39.6', {"egress": "New York", "shortest_path": True, "waypoint": "Atlanta"}]]

why are the ingress and egress numbers?
"""
