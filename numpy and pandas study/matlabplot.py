# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.linspace(-2,2,100)
# y1=2*x+1
# y2=x**2
# plt.figure(num=1,figsize=(5,5))
# l1=plt.plot(x,y1,color='red',linewidth=2,linestyle="--",label='f(x)')
# l2=plt.plot(x,y2,color='red',linewidth=2,linestyle="-",label='f1(x)')
# plt.xlim((0,2))
# plt.ylim((0,8))
# plt.xlabel('x')
# plt.ylabel('y')
# tick=np.linspace(-1,2,10)
# plt.xticks(tick)
# plt.yticks([-1,0,1,2],[r'$-one \alpha$','zero','one','two'])
# ax=plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
# plt.legend()
# #  plt.legend(handles=[l1,l2],label=['fef','sdfsd'],loc='best')
#
# plt.show()


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()