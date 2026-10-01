import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# Simulating latency data for the practical class based on the zanbil.ir dataset context
# Log-normal distribution is common for web latency
np.random.seed(42)
data = np.random.lognormal(mean=5, sigma=0.8, size=10000)

# Statistics calculation
mean_val = np.mean(data)
median_val = np.median(data)
mode_res = stats.mode(data, keepdims=True)
mode_val = mode_res.mode[0]
p90 = np.percentile(data, 90)
p98 = np.percentile(data, 98)
p99 = np.percentile(data, 99)

# Outliers detection (using IQR)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data[(data < lower_bound) | (data > upper_bound)]
outliers_count = len(outliers)

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Mode: {mode_val:.2f}")
print(f"P90: {p90:.2f}")
print(f"P98: {p98:.2f}")
print(f"P99: {p99:.2f}")
print(f"Outliers count: {outliers_count}")

# Plotting Frequency Distribution
plt.figure(figsize=(10, 6))
plt.hist(data, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Média: {mean_val:.2f}ms')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Mediana: {median_val:.2f}ms')
plt.axvline(p90, color='orange', linestyle='dotted', linewidth=2, label=f'P90: {p90:.2f}ms')
plt.title('Distribuição de Frequência da Latência (ms)')
plt.xlabel('Latência (ms)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/sergio/Documentos/unirv/2026-01/ENGENHARIA DA QUALIDADE E CONFIABILIDADE/aulas/6.AtividadeAnaliseDados/latencia_dist.png')
print("Plot saved as latencia_dist.png")
