# matplotlib we use for a graphic
import matplotlib.pyplot as plt
x = [300,400,200]
y = [0,-25,-50]

plt.plot(x, y)
plt.show()

# parabola
z = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
l = [25,16,9,4,1,0,1,4,9,16,25]
plt.plot(z,l)
plt.show()
plt.plot(x,y,z,l)
plt.show()


