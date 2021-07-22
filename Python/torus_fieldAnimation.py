import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('fast')
plt.rcParams['figure.figsize'] = (10.5, 8.5)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.axis('off')
ax.grid(b=None)

R = 12
r = 7


def torus_mesh(M_radius, m_radius):

	u = np.linspace(0, 2*np.pi, num=25)
	v = np.linspace(0, 2*np.pi, num=25)
	u, v = np.meshgrid(u, v)

	x = np.cos(v)*(M_radius+m_radius*np.cos(u))
	y = np.sin(v)*(M_radius+m_radius*np.cos(u))
	z = m_radius*np.sin(u)

	return x, y, z

x, y, z = torus_mesh(R, r)

ax.plot_surface(x, y, z, cmap='plasma', alpha=0.35)

a = 9*np.cos(th)
b = 12.5*np.sin(th)

for i in range(10):
    phi = i*np.pi/5
    ax.plot(a*np.sin(phi)+12.5*np.sin(phi), a*np.cos(phi)+12.5*np.cos(phi), b, color='blue', linewidth=8, alpha=0.4)

lim = R*(2)

def init():
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])

def update_t(lenght, data, line):
    line.set_data(data[0:2, :lenght])
    line.set_3d_properties(data[2, :lenght])
    return line

theta = np.linspace(0, 2 * np.pi, 250)

x_ = 12.5*np.cos(theta)
y_ = 12.5*np.sin(theta)
z_ = np.linspace(0, 0.1, 250)
data = np.array([x_, y_, z_])

line = ax.plot(data[:, 0], data[:, 1], 0, color='green', linewidth=5.5, alpha=0.8, label='$B_{\phi}$')[0]


ax.legend(loc='best', fontsize=18)

fontdict = {
    'fontsize': 18,
    'verticalalignment': 'baseline'
}


plt.title('Toroidal Magnetic Field', fontdict=fontdict)


anim = animation.FuncAnimation(fig, update_t, frames=len(theta), blit=False, fargs=(data, line), interval=0.01, init_func=init)



writer = animation.FFMpegWriter(fps=250, metadata=dict(artist='torus'), bitrate=2500)
anim.save('torus.gif', writer=writer)