import numpy as np

from path_smoother import smooth_path
from trajectory_generator import generate_trajectory
from controller import simulate
from visualiser import plot_path_comparison, plot_velocity_profile, plot_tracking_result, plot_angular_velocity

WAYPOINTS = [
    (0.0,0.0),
    (2.0,1.0),
    (4.0,0.5),
    (6.0,2.0),
    (8.0,1.5),
    (9.0,3.5),
    (7.0,5.0),
    (5.0,4.5),
    (3.0,6.0),
    (1.0,5.5),
    (0.0,7.0)
]

V_MAX = 1.0
A_MAX = 0.5
LOOKAHEAD = 0.5
DT = 0.05

def main():
    print("Running robot navigation pipeline...")

    smooth = smooth_path(WAYPOINTS)
    trajectory, vel_profile, t_vec = generate_trajectory(smooth, V_MAX, A_MAX)

    history = simulate(trajectory, LOOKAHEAD, DT)

    plot_path_comparison(WAYPOINTS, smooth)
    plot_velocity_profile(t_vec, vel_profile)
    plot_tracking_result(trajectory, history)
    plot_angular_velocity(history)

    print("Plots saved in project folder.")

if __name__ == "__main__":
    main()