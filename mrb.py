import networkx as nx
import random
import matplotlib.pyplot as plt


def getReward(graph_model, n):
    value = 0
    for adj_node in graph_model.adj[n]:
        value += rewardMat[graph_model.nodes[n]['state']][graph_model.nodes[adj_node]['state']][0]
    return value


# 使用networx重写，1. 循环终止条件 2. value各个相加  3.记忆长度可变
# 记忆长度是8
memory_length = 30
# 判断是否完全一致

r = 0.001

rewardMat = {
    'C': {'C': (1, 1), 'D': (1 - r, 1 + r)},
    'D': {'C': (1 + r, 1 - r), 'D': (0, 0)}
}
# 创建一个 BA 图
graph_BA = nx.barabasi_albert_graph(1024, 1)
graph_ER = nx.random_graphs.erdos_renyi_graph(1000, 0.002)  # 平均度K = p ( N − 1 )

graph_WS = nx.random_graphs.watts_strogatz_graph(100, 2, 0.1)


# 为每个节点分配随机的 C 或 D
def cal_nodes(graph_model):
    c_number = 0
    for node in graph_model.nodes():
        graph_model.nodes[node]['states'] = []
        # graph_model.nodes[node]['state'] = random.choice(['C', 'D'])
        for i in range(memory_length):
            graph_model.nodes[node]['states'].append(random.choice(['C', 'D']))
        graph_model.nodes[node]['state'] = graph_model.nodes[node]['states'][-1]
        graph_model.nodes[node]['value'] = 0
        # graph_model.nodes[node]['all_value'] = 0
        # if graph_model.nodes[node]['state']=='C':
        #     graph_model.nodes[node]['states'].append('C')
        # elif graph_model.nodes[node]['state']=='D':
        #     graph_model.nodes[node]['states'].append('D')

    # 计算当前每一个值
    # for node in graph_model.nodes():
    #     for adj_node in graph_model.adj[node]:
    #         graph_model.nodes[node]['value'] =getReward(node)
    # 更新
    flag = True
    while flag:
        for node in graph_model.nodes():
            if graph_model.nodes[node]['state'] == 'C':
                reward1 = getReward(graph_model, node)
                graph_model.nodes[node]['state'] = 'D'
                reward2 = getReward(graph_model, node)
                if reward2 <= reward1:
                    del (graph_model.nodes[node]['states'][0])
                    graph_model.nodes[node]['states'].append('C')
                    graph_model.nodes[node]['state'] = 'C'
                    continue
                elif reward2 >= reward1:
                    del (graph_model.nodes[node]['states'][0])
                    graph_model.nodes[node]['states'].append('D')
                    graph_model.nodes[node]['state'] = 'C'
                    continue
            elif graph_model.nodes[node]['state'] == 'D':
                reward1 = getReward(graph_model, node)
                graph_model.nodes[node]['state'] = 'C'
                reward2 = getReward(graph_model, node)
                if reward2 <= reward1:
                    del (graph_model.nodes[node]['states'][0])
                    graph_model.nodes[node]['states'].append('D')
                    graph_model.nodes[node]['state'] = 'D'
                    continue
                elif reward2 >= reward1:
                    del (graph_model.nodes[node]['states'][0])
                    graph_model.nodes[node]['states'].append('C')
                    graph_model.nodes[node]['state'] = 'D'
                    continue
        for node in graph_model.nodes():  # graph_model.nodes[node]['state'] = random.choice(graph_model.nodes[node]['states'])
            graph_model.nodes[node]['state'] = random.choice(graph_model.nodes[node]['states'])
        # 判断 记忆中所有元素是否相同 相同则改变flag 退出循环
        memory = []
        for node in graph_model.nodes():
            if len(set(graph_model.nodes[node]['states'])) == 1:
                memory.append(1)
            else:
                memory.append(0)
        if all(memory):
            flag = False
        else:
            flag = True
    for node in graph_model.nodes():
        if graph_model.nodes[node]['state'] == 'C':
            c_number += 1

    for node in graph_model.nodes():
        print(graph_model.nodes[node]['states'])
    return c_number


print(cal_nodes(graph_WS))
#
#
# for node in graph_model.nodes():
#     print(graph_model.nodes[node])
# a.all_value += rewardMat[a.state][b.state][0]

