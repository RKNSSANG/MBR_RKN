import networkx as nx
import random
import matplotlib.pyplot as plt

def getReward(n):
    value=0
    for adj_node in ba_graph.adj[n]:
        value +=rewardMat[ba_graph.nodes[n]['state']][ba_graph.nodes[adj_node]['state']][0]
    return value
#使用networx重写，1. 循环终止条件 2. value各个相加  3.记忆长度可变
#记忆长度是8
memory_length=8
#判断是否完全一致

r=0.1
c_number=0
rewardMat = {
    'C': {'C': (1, 1), 'D': (1 - r, 1 + r)},
    'D': {'C': (1 + r, 1 - r), 'D': (0, 0)}
}
# 创建一个 BA 图
ba_graph = nx.barabasi_albert_graph(1000, 2)
# 为每个节点分配随机的 C 或 D
for node in ba_graph.nodes():
    ba_graph.nodes[node]['state'] = random.choice(['C', 'D'])
    ba_graph.nodes[node]['states']=['C','D','C','D']
    ba_graph.nodes[node]['value'] = 0
    # ba_graph.nodes[node]['all_value'] = 0
    if ba_graph.nodes[node]['state']=='C':
        ba_graph.nodes[node]['states'].append('C')
    elif ba_graph.nodes[node]['state']=='D':
        ba_graph.nodes[node]['states'].append('D')

#计算当前每一个值
# for node in ba_graph.nodes():
#     for adj_node in ba_graph.adj[node]:
#         ba_graph.nodes[node]['value'] =getReward(node)
#更新
flag= True
while flag :
    for node in ba_graph.nodes():
        if ba_graph.nodes[node]['state'] == 'C':
            reward1=getReward(node)
            ba_graph.nodes[node]['state'] = 'D'
            reward2=getReward(node)
            if reward2 <= reward1 :
                del(ba_graph.nodes[node]['states'][0])
                ba_graph.nodes[node]['states'].append('C')
                ba_graph.nodes[node]['state'] = random.choice(ba_graph.nodes[node]['states'])
                continue
            elif reward2 >= reward1:
                del(ba_graph.nodes[node]['states'][0])
                ba_graph.nodes[node]['states'].append('D')
                ba_graph.nodes[node]['state'] = random.choice(ba_graph.nodes[node]['states'])
                continue
        elif ba_graph.nodes[node]['state'] == 'D':
            reward1=getReward(node)
            ba_graph.nodes[node]['state'] = 'C'
            reward2=getReward(node)
            if reward2 <= reward1 :
                del(ba_graph.nodes[node]['states'][0])
                ba_graph.nodes[node]['states'].append('D')
                ba_graph.nodes[node]['state'] = random.choice(ba_graph.nodes[node]['states'])
                continue
            elif reward2 >= reward1:
                del(ba_graph.nodes[node]['states'][0])
                ba_graph.nodes[node]['states'].append('C')
                ba_graph.nodes[node]['state'] = random.choice(ba_graph.nodes[node]['states'])
                continue
    #判断 记忆中所有元素是否相同 相同则改变flag 退出循环
    memory = []
    for node in ba_graph.nodes():
        if len(set(ba_graph.nodes[node]['states'])) == 1:
            memory.append(1)
        else:
            memory.append(0)
    if all(memory):
        flag = False
    else:
        flag = True
for node in ba_graph.nodes():
    if ba_graph.nodes[node]['state']=='C':
        c_number +=1
print(c_number)
for node in ba_graph.nodes():
    print(ba_graph.nodes[node]['states'])
#
#
# for node in ba_graph.nodes():
#     print(ba_graph.nodes[node])
# a.all_value += rewardMat[a.state][b.state][0]

