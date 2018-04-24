import sys
import random
import math

def mstType1(n):
    SCALE = 1.0 / n * 60
    # init graph, store as adjacency list, if there is an directed edge (u, v, w) in graph, then tuple (v, w) will in array g[u]
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.random()
            # cut off large weighted edges
            if weight < SCALE:
                g[i].append((j, weight))
                g[j].append((i, weight))

    # do prime algorithm
    # dis means distance array in prime algorithm
    dis = [1e9] * n
    # used store whether vertex is choosen
    used = [False] * n
    dis[0] = 0

    # S: total weight
    S = 0.0
    for t in range(n):
        # find minimum cost vertex
        vertex, least = -1, 1e8
        for u in range(n):
            if not used[u] and dis[u] < least:
                least = dis[u]
                vertex = u
        if vertex == -1:
            raise Exception("edges are not enough, increase SCALE")

        # update weights of vertex connected choosen vertex
        S += dis[vertex]
        used[vertex] = True
        for edge in g[vertex]:
            v, weight = edge
            if not used[v] and weight < dis[v]:
                dis[v] = weight
    return S

def mstType2(n, dimension):
    coor = [[random.random() for i in range(dimension)] for _ in range(n)]
    # calculate euclidean distance distance between two vertor
    def distance(x, y):
        d = 0.0
        for i in range(len(x)):
            d += (x[i] - y[i]) ** 2
        return math.sqrt(d)
    
    # do prim algorithm
    # dis means distance array in prime algorithm
    # used store whether vertex is choosen
    dis = [1e9] * n
    used = [False] * n
    dis[0] = 0

    # total weight
    weight = 0.0
    for t in range(n):
        # find minimum cost vertex
        vertex, least = -1, 1e9
        for u in range(n):
            if not used[u] and dis[u] < least:
                least = dis[u]
                vertex = u

        # update weights of vertex connected choosen vertex
        weight += dis[vertex]
        used[vertex] = True
        for v in range(n):
            if not used[v] and distance(coor[vertex], coor[v]) < dis[v]:
                dis[v] = distance(coor[vertex], coor[v])
    return weight


def main(numpoints, numtrials, dimension):
    avg = 0.0
    for t in range(numtrials):
        if dimension == 0:
            avg += mstType1(numpoints)
        else:
            avg += mstType2(numpoints, dimension)
    avg /= numtrials
    print(avg, numpoints, numtrials, dimension)
    return avg

if __name__ == '__main__':
    main(numpoints=int(sys.argv[2]), numtrials=int(sys.argv[3]), dimension=int(sys.argv[4]))
