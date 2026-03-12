import rclpy
from rclpy.node import Node
import numpy as np

from origindrive.path_smoother import smooth_path
from origindrive.trajectory_generator import generate_trajectory
from origindrive.controller import simulate
from origindrive.visualiser import plot_path_comparison, plot_velocity_profile, plot_tracking_result, plot_angular_velocity

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

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.get_logger().info('Initializing robot navigation node...')
        self.run_pipeline()

    def run_pipeline(self):
        self.get_logger().info('Running robot navigation pipeline...')
        smooth = smooth_path(WAYPOINTS)
        trajectory, vel_profile, t_vec = generate_trajectory(smooth, V_MAX, A_MAX)

        history = simulate(trajectory, LOOKAHEAD, DT)

        plot_path_comparison(WAYPOINTS, smooth)
        plot_velocity_profile(t_vec, vel_profile)
        plot_tracking_result(trajectory, history)
        plot_angular_velocity(history)

        self.get_logger().info('Plots saved in project folder. Shutting down...')

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    
    # Run the batch simulation and exit
    rclpy.spin_once(node, timeout_sec=0.1)
    
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()

if __name__ == "__main__":
    main()