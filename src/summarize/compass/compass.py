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


class RoutingPath:
    def __init__(self, path, destination, ingress, egress, shortest_path, traffic_size):
        self.path = path
        self.destination = destination
        self.ingress = ingress
        self.egress = egress
        self.shortest_path = shortest_path
        self.traffic_size = traffic_size


class FeatureValue:
    def __init__(self, q, v):
        """
        :param q: a feature function
        :param v: a feature value

        set of feature functions in our use case:
        {"egress": row[5], "ingress": row[4], "shortest_path": row[6], "destination": row[3]}
        """
        self.q = q
        self.v = v


def score_feature(q, v, R):
    """
    takes a routing path, and calculates the traffic size of the path
    :param q: a feature function (egress, ingress, shortest_path, destination)
    :param v: a feature value (NY, LA, etc. for ingress or egress, 1 or 0 for shortest_path, name of the destination and etc)
    :param R: a set of routing paths
    """
    # Use traffic size as weight
    weight = 0
    for path in R:
        if q == "egress":
            if path.egress == v:
                weight += path.traffic_size
        elif q == "ingress":
            if path.ingress == v:
                weight += path.traffic_size
        elif q == "shortest_path":
            if path.shortest_path == v:
                weight += path.traffic_size
        elif q == "destination":
            if path.destination == v:
                weight += path.traffic_size
    return weight


def argmax(Q, R):
    max_score = -float("inf")
    best_feature = None
    best_feature_value = None

    score = score_feature(v, R)  # return a score for feature q with value v
    if score > max_score:
        max_score = score
        best_feature = q
        best_feature_value = v
    return best_feature, best_feature_value


def ComPass(R, q, k, t):
    S = set()  # The specifications set, set of solutions
    L = set()  # The last computed specification
    Q = q  # The set of candidate features

    while len(S) < k:
        q, v = argmax(Q, R)
        curr_feature = FeatureValue(q, v)
        L.add(curr_feature)
        Q.remove(q)

        if len(L) == t:
            break

        for path in Q:
            for feat_func, feat_val in path:
                while L.union(FeatureValue(feat_func, feat_val)) == L:
                    L.add(FeatureValue(feat_func, feat_val))
                    if len(L) == t:
                        S.add(L)
                        break
                    Q.remove(feat_func)

        S.add(L)

    return S


if __name__ == "__main__":
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    routing_paths = []
    # NL TO SQL
    for row in cur.execute(
        "SELECT path, destination, traffic_size, ingress, egress, shortest_path FROM network;"
    ):
        routing_paths.append(
            {
                "path": row[0],
                "destination": row[1],
                "traffic_size": row[2],
                "ingress": row[3],
                "egress": row[4],
                "shortest_path": row[5],
            }
        )

    # Example execution
    specifications = ComPass(
        routing_paths, {"egress", "ingress", "shortest_path", "organization"}, k=5, t=3
    )
    print(specifications)
