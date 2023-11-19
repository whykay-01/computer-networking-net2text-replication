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

def score_feature(q, R):
    # Assuming feature function 'q' returns a boolean if a feature is present in the routing path
    return sum(1 for r in R if q(r))

def argmax(Q, R):
    max_score = -float('inf')
    best_feature = None
    for feature in Q:
        # We assume 'feature' is a callable function that can be applied to the routing paths
        score = score_feature(feature, R)
        if score > max_score:
            max_score = score
            best_feature = feature
    return best_feature, max_score

def ComPass(R, q, k, t):
    S = set()  # The specifications set, set of solutions
    L = set()  # The last computed specification
    Q = set(q)  # The set of candidate features

    while len(S) < k:
        best_feature, _ = argmax(Q, R)
        if best_feature is None:
            break  # No more features to add
        L.add(best_feature)
        if len(L) >= t:
            S.add(frozenset(L))  # Add as an immutable set
            break
        Q.remove(best_feature)
        R = {r for r in R if best_feature(r)}  # Keep only paths where the best feature is present

    return S

if __name__ == "__main__":
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    routing_paths = set()
    for row in cur.execute('SELECT path FROM network;'):
        routing_paths.add(row[0])

    # Example feature functions, replace these with actual logic
    def egress(path): return "egress" in path
    def ingress(path): return "ingress" in path
    def shortest_path(path): return "shortest_path" in path
    def org(path): return "org" in path

    feature_functions = {egress, ingress, shortest_path, org}
    output_set = ComPass(routing_paths, feature_functions, 3, 3)
    spec_set = None

    for spec in output_set:
        spec_set = [f.__name__ for f in spec]  # List comprehension to get function names

    print(spec_set)
    con.close()