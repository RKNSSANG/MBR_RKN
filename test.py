# import networkx as nx
# import matplotlib.pyplot as plt
#
# # 生成ER图
# G = nx.erdos_renyi_graph(10, 0.4, seed=42)
#
# # 绘制ER图
# nx.draw(G, with_labels=True)
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

n = 20
k = 4
p = 0.2
ws = nx.watts_strogatz_graph(n, k, p)

pos = nx.circular_layout(ws)
nx.draw(ws, pos, with_labels=True)
plt.show()


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/RKNSSANG/MRB_RKN.git
git push -u origin main
