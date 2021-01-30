import matplotlib.pyplot as plt
from matplotlib import font_manager

#设置字体
font = font_manager.FontProperties(fname="D:\\fonts\\msyhl.ttc")

#数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

#绘图
bar_width = 0.2

x_14 = [i for i in range(len(a))]
x_15 = [i + bar_width for i in range(len(a))]
x_16 = [i + bar_width * 2 for i in range(len(a))]

plt.bar(x_14, b_14, width=bar_width, label="14日")
plt.bar(x_15, b_15, width=bar_width, label="15日")
plt.bar(x_16, b_16, width=bar_width, label="16日")

#调整刻度
plt.xticks(x_15, a, fontproperties=font)

#显示图例
plt.legend(prop=font)

#展示
plt.show()