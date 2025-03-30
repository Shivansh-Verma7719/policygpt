import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

asi_df = pd.read_parquet("ASI_Final_Merged.parquet")
plfs_df = pd.read_parquet("PLFS_Final_Merged.parquet")

gender_col = "b4q5_perrv"
education_years_col = "b4q10_perrv"
age_col = "b4q6_perrv"

# Convert to float
plfs_df[education_years_col] = plfs_df[education_years_col].astype(float)

# print(asi_df.head(10))
# print(plfs_df.head(10))


# Convert to int
plfs_df[gender_col] = plfs_df[gender_col].astype(int)

male_data = plfs_df[plfs_df[gender_col] == 1]
female_data = plfs_df[plfs_df[gender_col] == 2]
trans_data = plfs_df[plfs_df[gender_col] == 3]

print("Analysis mean of education years")


male_education_years = male_data[education_years_col]
female_education_years = female_data[education_years_col]
trans_education_years = trans_data[education_years_col]

# print(male_education_years.mean())
# print("\n")
# print(female_education_years.mean())

# Plot distribution of education years
plt.figure(figsize=(10, 6))
sns.histplot(male_education_years, bins=20, kde=True, color="blue")
plt.title("Distribution of Education Years for Males")
plt.xlabel("Education Years")
plt.ylabel("Frequency")
plt.savefig("male_education_years_distribution.png")

plt.figure(figsize=(10, 6))
sns.histplot(female_education_years, bins=20, kde=True, color="red")
plt.title("Distribution of Education Years for Females")
plt.xlabel("Education Years")
plt.ylabel("Frequency")
plt.savefig("female_education_years_distribution.png")


hours_actually_worked_col = "b6q6_act2_3pt1_perrv"
money_paid_col = "b6q9_act2_3pt1_perrv"


male_hours_actually_worked = male_data[hours_actually_worked_col]
female_hours_actually_worked = female_data[hours_actually_worked_col]

# Remove people who worked 0 hours
male_hours_actually_worked = male_hours_actually_worked[male_hours_actually_worked > 0]
female_hours_actually_worked = female_hours_actually_worked[
    female_hours_actually_worked > 0
]

# Get money paid data
male_money_paid = male_data[money_paid_col]
female_money_paid = female_data[money_paid_col]

# Filter money paid for those who worked > 0 hours
male_money_paid = male_money_paid[male_data[hours_actually_worked_col] > 0]
female_money_paid = female_money_paid[female_data[hours_actually_worked_col] > 0]

male_hourly_wage = male_money_paid / male_hours_actually_worked
female_hourly_wage = female_money_paid / female_hours_actually_worked

print(f"Male hourly wage: {male_hourly_wage.mean()}")
print(f"Female hourly wage: {female_hourly_wage.mean()}")


# Save distributions
plt.figure(figsize=(10, 6))
sns.histplot(male_hourly_wage, bins=20, kde=True, color="blue")
plt.title("Distribution of Male Hourly Wage")
plt.xlabel("Hourly Wage")
plt.ylabel("Frequency")
plt.savefig("male_hourly_wage_distribution.png")

plt.figure(figsize=(10, 6))
sns.histplot(female_hourly_wage, bins=20, kde=True, color="red")
plt.title("Distribution of Female Hourly Wage")
plt.xlabel("Hourly Wage")
plt.ylabel("Frequency")
plt.savefig("female_hourly_wage_distribution.png")


# # Calculate correlation matrices
# print("\nASI Correlation Matrix:")
# asi_corr = asi_df.corr(numeric_only=True)
# print(asi_corr)

# print("\nPLFS Correlation Matrix:")
# plfs_corr = plfs_df.corr(numeric_only=True)
# print(plfs_corr)

# # Visualize correlation matrices
# plt.figure(figsize=(12, 10))
# plt.title("ASI Correlation Matrix")
# sns.heatmap(asi_corr, annot=False, cmap="coolwarm", center=0, linewidths=0.5)
# plt.tight_layout()
# plt.savefig("asi_correlation_matrix.png")
# plt.close()

# plt.figure(figsize=(12, 10))
# plt.title("PLFS Correlation Matrix")
# sns.heatmap(plfs_corr, annot=False, cmap="coolwarm", center=0, linewidths=0.5)
# plt.tight_layout()
# plt.savefig("plfs_correlation_matrix.png")
# plt.close()
