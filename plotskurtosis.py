import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis

np.random.seed(42)
returns = np.random.normal(0, 0.01, 1000) * 100

kurt_val = kurtosis(returns, fisher=True)

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(returns, bins=30, kde=True, ax=axs[0, 0], color='skyblue', edgecolor='black')
axs[0, 0].set_title(f"Histogram of Returns\nKurtosis: {kurt_val:.2f}")
axs[0, 0].set_xlabel("Return (%)")
axs[0, 0].set_ylabel("Frequency")

sns.boxplot(x=returns, ax=axs[0, 1], color='lightgreen')
axs[0, 1].set_title("Boxplot of Returns")
axs[0, 1].set_xlabel("Return (%)")

axs[1, 0].plot(returns, marker='o', linestyle='-', color='magenta', markersize=3)
axs[1, 0].set_title("Line Plot of Returns")
axs[1, 0].set_xlabel("Day")
axs[1, 0].set_ylabel("Return (%)")
axs[1, 0].grid(True, linestyle="--", alpha=0.7)

sns.kdeplot(returns, ax=axs[1, 1], color='orange', fill=True)
axs[1, 1].set_title("Density Plot of Returns")
axs[1, 1].set_xlabel("Return (%)")
axs[1, 1].set_ylabel("Density")

plt.tight_layout()
plt.savefig("synthetic_kurtosis_visualization.png", dpi=300)
plt.show()
