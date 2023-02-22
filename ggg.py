class UGV_model:
    """"""


Seeing 【https: // blog.csdn.net / u013468614 / article / details / 103489350】 for the complete code of UGV_model.
""""""

from scipy.spatial import KDTree

# set reference trajectory
refer_path = np.zeros((1000, 2))
refer_path[:, 0] = np.linspace(0, 1000, 1000)
# refer_path[:,1] = 5*np.sin(refer_path[:,0]/5.0) # generating sin reference trajectory
refer_tree = KDTree(refer_path)  # reference trajectory
plt.plot(refer_path[:, 0], refer_path[:, 1], '-.b', linewidth=5.0)

# Initial: pos_x is 0, pos_y is 1.0 m, heading is 0 m,
# wheelbase is 2.0 m,  speed is 2.0 m/s, decision period is 0.1s.
ugv = UGV_model(0, 1.0, 0, 2.0, 2.0, 0.1)
pind = 0
ind = 0
for i in range(1000):
    robot_state = np.zeros(2)
    robot_state[0] = ugv.x
    robot_state[1] = ugv.y
    _, ind = refer_tree.query(robot_state)
    if ind < pind:
        ind = pind
    else:
        pind = ind

    dist = np.linalg.norm(robot_state - refer_path[ind])
    dx, dy = refer_path[ind] - robot_state
    alpha = math.atan2(dy, dx)
    e = np.sign(np.sin(alpha - ugv.theta)) * dist  # bang-bang controller
    delta = np.sign(e) * np.pi / 6.0
    ugv.update(2.0, delta)
    ugv.plot_duration()
