'''
Simulate a system containing particles than constanly rotate around a central point of
variois speeds, just like the hands of a clock.
'''
from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
from IPython import get_ipython
import timeit

class Particle:

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel
    
    def __repr__(self):
        return f"Particle x={self.x} y={self.y} ang_vel={self.ang_vel}"
    
    # def __str__(self):
    #     return f"Particle x={self.x} y={self.y} ang_vel={self.ang_vel}"

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

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

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
    particles = [Particle(0.3, 0.5, 1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def test_evolve():
    particles = [Particle(0.3, 0.5, 1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0, p1, p2 = simulator.particles

    def fequal(a, b, eps=1e-5):
        print(abs(a - b) < eps)
        return abs(a - b) < eps
    print(p0, p1, p2)
    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)
    
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
    
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)

    print("test_evolve passed")

def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(2000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    
if __name__ == '__main__':
    ipython = get_ipython()
    if ipython:
        ipython.run_line_magic("timeit", "benchmark()")
    else:
        result = timeit.timeit("benchmark()", setup="from __main__ import benchmark", number=10)
        benchmark()