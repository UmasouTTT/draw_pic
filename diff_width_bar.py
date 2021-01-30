import matplotlib.pyplot as plt
from matplotlib import font_manager

#设置字体
font = font_manager.FontProperties(fname="D:\\fonts\\msyhl.ttc")

interval = [0,5,10,15,20,25,30,35,40,45,60,90, 150]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

#绘图
x = [(interval[i] + interval[i + 1]) / 2 for i in range(len(interval) - 1)]
print(x)
plt.bar(x, quantity, width=width)

#设置标签
plt.xticks(interval)

#网格
plt.grid()

#设置图形
plt.figure(figsize=(40, 8), dpi=80)



#展示
plt.show()
