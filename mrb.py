import networkx as nx
import random
import matplotlib.pyplot as plt

#使用networx重写，1. 循环终止条件 2. value各个相加  3.记忆长度可变
r=0.1
c_number=0
rewardMat = {
    'C': {'C': (1, 1), 'D': (1 - r, 1 + r)},
    'D': {'C': (1 + r, 1 - r), 'D': (0, 0)}
}
# 创建一个 BA 图
ba_graph = nx.barabasi_albert_graph(1000, 3)
# 为每个节点分配随机的 C 或 D
for node in ba_graph.nodes():
    ba_graph.nodes[node]['state'] = random.choice(['C', 'D'])
    ba_graph.nodes[node]['states']=[]
    ba_graph.nodes[node]['value']=0
    ba_graph.nodes[node]['all_value'] = 0
    if ba_graph.nodes[node]['state']=='C':
        ba_graph.nodes[node]['states'].append('C')
    elif ba_graph.nodes[node]['state']=='D':
        ba_graph.nodes[node]['states'].append('D')


#更新

#计算当前节点的收益
def calValue():
    










# 计算覆盖点数目
for node in ba_graph.nodes():
    if ba_graph.nodes[node]['state']=='C':
        c_number +=1
print(c_number)