import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

data_apple = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Average Stock Price': [130.1, 135.8, 140.2, 145.3, 150.5]
}
data_nvidia = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Average Stock Price': [260.3, 270.5, 280.1, 290.4, 300.7]
}

df_apple = pd.DataFrame(data_apple)
df_nvidia = pd.DataFrame(data_nvidia)

kurtosis_apple = kurtosis(df_apple['Average Stock Price'])
kurtosis_nvidia = kurtosis(df_nvidia['Average Stock Price'])

# Plotting dynamic graphs
plt.figure(figsize=(12, 8))

# Apple stock price plot
plt.plot(
    df_apple['Year'], 
    df_apple['Average Stock Price'], 
    label=f'Apple (Kurtosis: {kurtosis_apple:.2f})', 
    marker='o', 
    linestyle='--', 
    color='blue'
)

plt.plot(
    df_nvidia['Year'], 
    df_nvidia['Average Stock Price'], 
    label=f'Nvidia (Kurtosis: {kurtosis_nvidia:.2f})', 
    marker='s', 
    linestyle='-', 
    color='orange'
)

# Adding graph details
plt.title('Stock Price Comparison with Kurtosis (Apple vs Nvidia)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Stock Price (USD)', fontsize=14)
plt.xticks(df_apple['Year'], fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
