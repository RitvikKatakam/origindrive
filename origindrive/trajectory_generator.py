import numpy as np

def generate_trajectory(path, v_max=1.0, a_max=0.5):

    deltas = np.diff(path, axis=0)
    dist = np.hypot(deltas[:,0], deltas[:,1])
    s = np.concatenate(([0], np.cumsum(dist)))

    total_dist = s[-1]

    t_acc = v_max/a_max
    d_acc = 0.5*a_max*t_acc**2

    if 2*d_acc > total_dist:
        t_acc = np.sqrt(total_dist/a_max)

    t_total = 2*t_acc + (total_dist - 2*d_acc)/v_max

    t_vec = np.linspace(0, t_total, len(path))
    v_profile = np.minimum(v_max, a_max*t_vec)

    trajectory = [(path[i,0], path[i,1], t_vec[i]) for i in range(len(path))]

    return trajectory, v_profile, t_vec