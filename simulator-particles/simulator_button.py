'''
Simulate a system containing particles than constanly rotate around a central point of
variois speeds, just like the hands of a clock.
'''
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button
import numpy as np


class Particle:

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                #1. calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y/norm
                v_y = p.x/norm

                #2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x +=d_x
                p.y +=d_y
                #3. repeat for all the time steps


def visualize(simulator):
    
    def init():
        line.set_data([], [])
        return line,

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    print("X", "Y")
    print(X, Y)
    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    
    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,
    
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10, cache_frame_data=False)
    plt.show()

def visualize(simulator):
    fig, axs = plt.subplots(2,2)
    for ax in axs.flat:
        ax.set_aspect('equal')
        ax.set_xlim(-3, 1)
        ax.set_ylim(-1, 1)
        line, = ax.plot([], [], 'ro')

    # Button to add particles
    add_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
    add_button = Button(add_ax, 'Add Particle')



    def add_particle(event):
        x, y = np.random.uniform(-0.5, 0.5, 2)
        ang_vel = np.random.uniform(-2, 2)
        simulator.particles.append(Particle(x, y, ang_vel))

    add_button.on_clicked(add_particle)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10, cache_frame_data=False)
    plt.show()

def test_visualize():
    particles = []
    simulator = ParticleSimulator(particles)
    visualize(simulator)

if __name__ == '__main__':
    test_visualize()




