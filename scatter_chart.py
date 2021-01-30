import matplotlib.pyplot as plt
from matplotlib import font_manager
import random


#设置字体
font = font_manager.FontProperties(fname="D:\\fonts\\msyhl.ttc")

#数据
y_1 = [random.randint(10, 20) for i in range(0, 10)]
y_2 = [random.randint(20, 30) for i in range(0, 10)]

x_1 = [i for i in range(0, 10)]
x_2 = [i + 15 for i in range(0, 10)]

#设置图形
plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(x_1, y_1, label="3月份")
plt.scatter(x_2, y_2, label="10月份")

#调整刻度
_x = x_1 + x_2
x_labels = ["3月{}日".format(i) for i in x_1]
x_labels += ["10月{}日".format(i - 15) for i in x_2]
plt.xticks(_x[::2], x_labels[::2], fontproperties=font, rotation=45)

#添加描述信息
plt.xlabel("日期")
plt.ylabel("温度")
plt.title("温度随日期变化散点图", fontproperties=font)

#显示图例
plt.legend(loc="best", prop=font)

#展示
plt.show()