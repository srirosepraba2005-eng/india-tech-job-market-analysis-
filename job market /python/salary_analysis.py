
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/raw/india_job_market_2024_2026.csv")

# Convert salary to numeric values
df["Salary_LPA"] = pd.to_numeric(df["Salary_LPA"], errors="coerce")

# Calculate average salary for each job title
salary = (
    df.groupby("Job_Title")["Salary_LPA"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 Job Titles by Average Salary (LPA)")
print(salary.round(2))

# Create the chart
plt.figure(figsize=(10, 6))
sns.barplot(x=salary.values, y=salary.index)

plt.title("Top 10 Job Titles by Average Salary")
plt.xlabel("Average Salary (LPA)")
plt.ylabel("Job Title")
plt.tight_layout()

# Save the chart
plt.savefig("data/charts/top_average_salaries.png", dpi=300)
plt.show()
