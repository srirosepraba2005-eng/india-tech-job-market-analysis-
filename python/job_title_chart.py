
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/raw/india_job_market_2024_2026.csv")

# Count the 10 most common job titles
top_jobs = df["Job_Title"].value_counts().head(10)

# Create the chart
plt.figure(figsize=(12, 6))
sns.barplot(x=top_jobs.values, y=top_jobs.index)

plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Number of Job Postings")
plt.ylabel("Job Title")
plt.tight_layout()

# Save the chart
plt.savefig("data/charts/top_job_titles.png", dpi=300)
plt.show()
