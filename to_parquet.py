import pandas as pd

print("Reading ASI data...")
df1 = pd.read_stata("ASI_Final_Merged.dta")

print("Reading PLFS data...")
df2 = pd.read_stata("PLFS_Final_Merged.dta")

# Convert categorical columns to string before saving to parquet
print("Converting categorical columns in ASI data...")
for col in df1.select_dtypes(include=["category"]).columns:
    df1[col] = df1[col].astype(str)

print("Converting categorical columns in PLFS data...")
for col in df2.select_dtypes(include=["category"]).columns:
    df2[col] = df2[col].astype(str)

print("Saving ASI data...")
df1.to_parquet("ASI_Final_Merged.parquet", index=False)

print("Saving PLFS data...")
df2.to_parquet("PLFS_Final_Merged.parquet", index=False)

print("Done!")
print(df1.head(10))

print(df2.head(10))
