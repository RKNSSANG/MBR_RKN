import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# 定义雪堆博弈函数
def snowdrift_game(G, rounds):
    for i in range(rounds):
        # 计算每个玩家的邻居节点的平均出度
        avg_degrees = {}
        for node in G.nodes():
            neighbors = G.neighbors(node)
            avg_degree = np.mean([G.out_degree(n) for n in neighbors])
            avg_degrees[node] = avg_degree

        # 更新每个玩家的出度
        for node in G.nodes():
            neighbors = G.neighbors(node)
            if all([G.out_degree(n) == 1 for n in neighbors]):
                G.nodes[node]['decision'] = 1
            elif any([G.nodes[n]['decision'] == 0 for n in neighbors]):
                G.nodes[node]['decision'] = 0
            else:
                if np.random.rand() < (1 - avg_degrees[node]):
                    G.nodes[node]['decision'] = 1
                else:
                    G.nodes[node]['decision'] = 0

    # 绘制结果
    pos = nx.circular_layout(G)
    node_colors = ['green' if G.nodes[n]['decision'] == 1 else 'red' for n in G.nodes()]
    nx.draw(G, pos, node_color=node_colors, with_labels=True)
    plt.show()


# 创建一个有向图
G = nx.DiGraph()

# 添加10个节点
G.add_nodes_from(range(10))

# 随机添加边
for i in range(10):
    for j in range(10):
        if i != j and np.random.rand() < 0.3:
            G.add_edge(i, j)

# 初始化每个玩家的决策为随机值
for node in G.nodes():
    G.nodes[node]['decision'] = np.random.randint(2)

# 运行雪堆博弈函数
snowdrift_game(G,1)
