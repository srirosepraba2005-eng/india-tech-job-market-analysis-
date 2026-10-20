
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/raw/india_job_market_2024_2026.csv")

# Count job postings by work mode
work_modes = df["Work_Mode"].value_counts()

# Create the chart
plt.figure(figsize=(8, 5))
sns.barplot(x=work_modes.index, y=work_modes.values)

plt.title("Job Postings by Work Mode")
plt.xlabel("Work Mode")
plt.ylabel("Number of Job Postings")
plt.tight_layout()

# Save the chart
plt.savefig("data/charts/work_mode_chart.png", dpi=300)
plt.show()
