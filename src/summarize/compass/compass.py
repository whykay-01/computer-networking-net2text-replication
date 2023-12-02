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

from NL2SQL import parse
from SQL2NL import back_to_natural_language
import sqlite3


class RoutingPath:
    def __init__(self, path, destination, traffic_size, ingress, egress, shortest_path):
        self.path = path
        self.destination = destination
        self.traffic_size = traffic_size
        self.ingress = ingress
        self.egress = egress
        self.shortest_path = shortest_path

    def get_feature_value(self, feature_function):
        if feature_function == "egress":
            return self.egress
        elif feature_function == "ingress":
            return self.ingress
        elif feature_function == "shortest_path":
            return self.shortest_path
        elif feature_function == "destination":
            return self.destination

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


def argmax(Q: set, R):
    max_score = -float("inf")
    best_feature = None
    best_feature_value = None

    for q in Q:
        feature_values = set()
        con = sqlite3.connect("src/db/network.db")
        cur = con.cursor()
        # select all the values for the feature function
        for row in cur.execute(
            f"SELECT DISTINCT {q} FROM network;"
        ):
            feature_values.add(row)
        cur.close()
        for v in feature_values:
            v = v[0]
            score = score_feature(q, v, R)
            if score > max_score:
                max_score = score
                best_feature = q
                best_feature_value = v

    return best_feature, best_feature_value


def ComPass(R, q, k, t):
    S = set()  # The specifications set, set of solutions
    ss = [] # Return specifications
    L = set()  # The last computed specification
    Q = q  # The set of candidate features

    while len(S) <= k:
        q, v = argmax(Q, R)
        curr_feature = (q, v)
        L = L.union(frozenset([curr_feature]))
        Q = Q.difference({q})

        if len(L) > t:
            S = S.union(L)
            L = set()
            break

        for path in R:
            for feature_function in Q:
                feature_value = path.get_feature_value(feature_function)
                new_feature = frozenset([(feature_function, feature_value)])
                while L.union(new_feature) == L:
                    L = L.union(new_feature)
                    if len(L) == t:
                        S = S.union(L)
                        break
                    Q = Q.difference({feature_function})

        S = S.union(L)
        ss.append(S)

    return ss


if __name__ == "__main__":
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    routing_paths = []
    parse_result, condition = parse("How does Yahoo's traffic from Chicago get handled?")
    for row in cur.execute(
        parse_result
         #"SELECT path, destination, traffic_size, ingress, egress, shortest_path FROM network;"
    ):
        routing_paths.append(
            RoutingPath(
                path=row[0],
                destination=row[1],
                traffic_size=row[2],
                ingress=row[3],
                egress=row[4],
                shortest_path=row[5],
            )
        )

    # Example execution
    specifications = ComPass(
        routing_paths, {"egress", "ingress", "shortest_path", "destination"}, k=5, t=4
    )
    print(specifications)
    final_result = back_to_natural_language(specifications, condition)
    print(final_result)
    
