import networkx as nx
import random

def getReward(graph_model, n):
    value = 0
    for adj_node in graph_model.adj[n]:
        value += rewardMat[graph_model.nodes[n]['state']][graph_model.nodes[adj_node]['state']][0]
    return value
# 超参数
memory_length = 20
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
        for i in range(memory_length):
            graph_model.nodes[node]['states'].append(random.choice(['C', 'D']))
        graph_model.nodes[node]['state'] = graph_model.nodes[node]['states'][-1]
        graph_model.nodes[node]['value'] = 0
    # 更新
    flag = True
    while flag:
        for node in graph_model.nodes():
            if graph_model.nodes[node]['state'] == 'C':
                reward1 = getReward(graph_model, node)
                graph_model.nodes[node]['state'] = 'D'
                reward2 = getReward(graph_model, node)
                if reward2 <= reward1:
                    graph_model.nodes[node]['state'] = 'C'
                    graph_model.nodes[node]['next_state']='C'
                    continue
                else:
                    graph_model.nodes[node]['state'] = 'C'
                    graph_model.nodes[node]['next_state']='D'
                    continue
            elif graph_model.nodes[node]['state'] == 'D':
                reward1 = getReward(graph_model, node)
                graph_model.nodes[node]['state'] = 'C'
                reward2 = getReward(graph_model, node)
                if reward2 <= reward1:
                    graph_model.nodes[node]['state'] = 'D'
                    graph_model.nodes[node]['next_state']='D'
                    continue
                else:
                    graph_model.nodes[node]['state'] = 'D'
                    graph_model.nodes[node]['next_state']='C'
                    continue
        # 判断 记忆中所有元素是否相同 相同则改变flag 退出循环
        memory = []
        for node in graph_model.nodes():
            if (set(graph_model.nodes[node]['states']) == set(graph_model.nodes[node]['next_state'])):
                memory.append(1)
            else:
                memory.append(0)
        if all(memory):
            flag = False
        else:
            flag = True
            for node in graph_model.nodes():
                del (graph_model.nodes[node]['states'][0])
                graph_model.nodes[node]['states'].append(graph_model.nodes[node]['next_state'])
                graph_model.nodes[node]['state'] = random.choice(graph_model.nodes[node]['states'])

    for node in graph_model.nodes():
        if graph_model.nodes[node]['state'] == 'C':
            c_number += 1

    for node in graph_model.nodes():
        print(graph_model.nodes[node]['states'])
    return c_number

print(cal_nodes(graph_BA))


