import numpy as np
from scipy.interpolate import CubicSpline

def smooth_path(waypoints, num_samples=500):

    pts = np.array(waypoints)

    deltas = np.diff(pts, axis=0)
    dist = np.hypot(deltas[:,0], deltas[:,1])

    s = np.concatenate(([0], np.cumsum(dist)))

    cs_x = CubicSpline(s, pts[:,0])
    cs_y = CubicSpline(s, pts[:,1])

    s_new = np.linspace(0, s[-1], num_samples)

    x_new = cs_x(s_new)
    y_new = cs_y(s_new)

    return np.vstack((x_new, y_new)).T