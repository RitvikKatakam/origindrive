import matplotlib.pyplot as plt
import numpy as np

def plot_path_comparison(waypoints, smooth):

    w = np.array(waypoints)

    plt.figure()
    plt.plot(w[:,0],w[:,1],'ro--',label="Waypoints")
    plt.plot(smooth[:,0],smooth[:,1],'b',label="Smooth path")
    plt.legend()
    plt.title("Path Smoothing")

    plt.savefig("path_smoothing.png")
    plt.close()

def plot_velocity_profile(t,v):

    plt.figure()
    plt.plot(t,v)
    plt.title("Velocity Profile")
    plt.xlabel("Time")
    plt.ylabel("Speed")

    plt.savefig("velocity_profile.png")
    plt.close()

def plot_tracking_result(traj,history):

    traj=np.array([[p[0],p[1]] for p in traj])

    plt.figure()
    plt.plot(traj[:,0],traj[:,1],'b--',label="Reference")
    plt.plot(history["x"],history["y"],'r',label="Robot")
    plt.legend()
    plt.title("Tracking Performance")

    plt.savefig("tracking_result.png")
    plt.close()

def plot_angular_velocity(history):

    plt.figure()
    plt.plot(history["omega"])
    plt.title("Angular Velocity")

    plt.savefig("omega_profile.png")
    plt.close()