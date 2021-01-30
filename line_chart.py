import matplotlib.pyplot as plt
from matplotlib import font_manager



#设置字体
font = font_manager.FontProperties(fname="D:\\fonts\\msyhl.ttc")

y_1 = [i for i in range(0, 20)]

y_2 = [i for i in range(2, 22)]

x = [i for i in range(0, 20)]

#设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

#设置数据，标签，线条属性
plt.plot(x, y_1, label="自己", color="r", linestyle="--", linewidth=5, alpha=0.5)
plt.plot(x, y_2, label="同桌")

#设置x轴刻度
x_ticks = ["{}岁".format(i) for i in x]
plt.xticks(x, x_ticks, fontproperties=font, rotation=45)


#绘制网格
plt.grid(alpha=0.4)

#添加图例
plt.legend(prop=font, loc="upper left")

#添加描述信息
plt.xlabel("年龄")
plt.ylabel("人数")
plt.title("人数随年龄变化折线图", fontproperties=font)

#展示
plt.show()