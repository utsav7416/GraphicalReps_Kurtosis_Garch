import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis

np.random.seed(42)
returns = np.random.normal(0, 0.01, 1000)
kurt_val = kurtosis(returns)

plt.figure(figsize=(10, 6))
sns.histplot(returns, bins=30, kde=True, color="blue", edgecolor="black")
plt.title(f"Returns Histogram & KDE (Kurtosis: {kurt_val:.2f})")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("short_kurtosis.png", dpi=300)
plt.show()
