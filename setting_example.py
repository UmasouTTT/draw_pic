import numpy as np
import matplotlib.pyplot as plt





plt.plot([0, 2000], [0, 1000], color="orange", label="Error 1000")
plt.plot([200, 200], [100, 200], color="red", linestyle="--")

# 网格
plt.grid(True, linestyle="--", alpha=0.5)

# 横纵坐标单位长度一致
plt.gca().set_aspect(1)
plt.xlabel("key", fontsize=16, fontweight='bold')
plt.ylabel("block changes", fontsize=16, fontweight='bold')
plt.legend(fontsize=18)

plt.savefig("worstCase.pdf", bbox_inches="tight")
plt.show()

