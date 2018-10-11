import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


def life_step(X):
    """Game of life step using generator expressions"""
    nbrs_count = sum(np.roll(np.roll(X, i, 0), j, 1) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i != 0 or j != 0))
    return (nbrs_count == 3) | (X & (nbrs_count == 2))


def life_animation(X, frames=5, interval=300, mode='loop'):
    X = np.asarray(X)

    X_blank = np.zeros_like(X)

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
    im = ax.imshow(X, cmap="Greys", interpolation='nearest')

    # initialization function: plot the background of each frame
    def init():
        im.set_data(X_blank)
        return (im,)

    # animation function.  This is called sequentially
    def animate(i):
        im.set_data(animate.X)
        animate.X = life_step(animate.X)
        return (im,)
    animate.X = X

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frames, interval=interval)
    plt.show()

# MAIN

np.random.seed(101)
X = np.zeros((80, 90), dtype=bool)

xCoordinate = 20
yCoordinate = 10

r = np.random.random((yCoordinate, xCoordinate))
X[yCoordinate:(yCoordinate+yCoordinate), yCoordinate:(yCoordinate+xCoordinate)] = r > 0.7326
life_animation(X, frames=40, mode='once')
