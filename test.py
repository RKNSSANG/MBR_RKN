import networkx as nx
import random
import matplotlib.pyplot as plt
r=0.1
c_number=0
rewardMat = {
    'C': {'C': (1, 1), 'D': (1 - r, 1 + r)},
    'D': {'C': (1 + r, 1 - r), 'D': (0, 0)}
}
# 创建一个 BA 图
ba_graph = nx.barabasi_albert_graph(1000, 3)
print(ba_graph[743])



