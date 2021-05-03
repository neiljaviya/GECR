#Write a program to plot different types of graphs using PyPlot.

import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x1 = [0]*n
y1 = [0]*n
x2 = [0]*n
y2 = [0]*n

for i in range(n):
    temp = input("Enter x%d y%d: "%(i,i)).split()
    x1[i],y1[i] = int(temp[0]),int(temp[1])

for i in range(n):
    temp = input("Enter x'%d y'%d: "%(i,i)).split()
    x2[i],y2[i] = int(temp[0]),int(temp[1])

plt.plot(x1, y1, label="line 1", color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.plot(x2, y2, label="line 2", color='red', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='black', markersize=12,)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two lines on same graph!')
plt.legend()
plt.show()