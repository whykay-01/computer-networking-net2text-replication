import networkx as nx
import numpy as np

def compass(R, q, k, t):
    """
    Algorithm 1: ComPass (R, q1,...ql , k, t)
    # Input : R: a set of routing paths.
    # q1; : : : ;ql : a set of feature functions.
    # k: limit on the number of specifications.
    # t: limit on the size of specifications.
    # Output: A set of specifications S.
    """
    # Step 1: Construct the graph G
    G = nx.DiGraph()
    for r in R:
        for i in range(len(r)-1):
            G.add_edge(r[i], r[i+1])
    
    # Step 2: Compute the feature matrix F
    F = np.zeros((len(q), len(G.nodes())))
    for i in range(len(q)):
        for j, node in enumerate(G.nodes()):
            F[i][j] = q[i](node)
    
    # Step 3: Compute the correlation matrix C
    C = np.corrcoef(F)
    
    # Step 4: Compute the specification set S
    S = set()
    for i in range(k):
        max_corr = np.unravel_index(np.argmax(C), C.shape)
        if C[max_corr] < t:
            break
        S.add((max_corr[0], G.nodes()[max_corr[1]]))
        C[max_corr[0], max_corr[1]] = -1
    
    return S