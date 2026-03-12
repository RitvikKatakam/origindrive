import numpy as np

class RobotState:
    def __init__(self,x=0,y=0,theta=0):
        self.x=x
        self.y=y
        self.theta=theta

def pure_pursuit(state, target, lookahead):

    dx = target[0]-state.x
    dy = target[1]-state.y

    alpha = np.arctan2(dy,dx)-state.theta

    curvature = 2*np.sin(alpha)/lookahead

    v = 1.0
    omega = v*curvature

    return v, omega

def simulate(trajectory, lookahead=0.5, dt=0.05):

    state = RobotState()
    history = {"x":[],"y":[],"omega":[]}

    for p in trajectory:

        v,omega = pure_pursuit(state,p,lookahead)

        state.x += v*np.cos(state.theta)*dt
        state.y += v*np.sin(state.theta)*dt
        state.theta += omega*dt

        history["x"].append(state.x)
        history["y"].append(state.y)
        history["omega"].append(omega)

    return history