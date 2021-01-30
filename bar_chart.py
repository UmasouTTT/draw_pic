import matplotlib.pyplot as plt
from matplotlib import font_manager

#设置字体
font = font_manager.FontProperties(fname="D:\\fonts\\msyhl.ttc")

#数据
a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：\n最后的骑士","摔跤吧！爸爸","加勒比海盗5：\n死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
x = [i for i in  range(0, len(b))]



plt.bar(x, b, width=0.3)


#调整刻度
plt.xticks(x, a, fontproperties=font, rotation=45)

#添加描述信息
plt.xlabel("电影")
plt.ylabel("票房")
plt.title("电影票房柱状图图", fontproperties=font)

#显示图例
#plt.legend(loc="best", prop=font)

#设置图形
plt.figure(figsize=(20, 8), dpi=80)


#展示
plt.show()