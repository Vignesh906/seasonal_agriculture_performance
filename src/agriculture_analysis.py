import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = os.path.join("data", "seasonal_agriculture_performance_dataset.csv")
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Data cleaning / preprocessing
# -----------------------------
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(exclude=np.number).columns.tolist()

missing_before = df.isna().sum()
duplicate_rows = int(df.duplicated().sum())

# Median imputation for numeric columns; mode imputation for categorical columns.
# Original missingness is preserved in the summary table.
df_clean = df.copy()
for col in numeric_cols:
    if df_clean[col].isna().any():
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

for col in categorical_cols:
    if df_clean[col].isna().any():
        mode = df_clean[col].mode()
        if not mode.empty:
            df_clean[col] = df_clean[col].fillna(mode.iloc[0])

# -----------------------------
# Summary analysis
# -----------------------------
season_summary = (
    df_clean.groupby("Season")
    .agg(
        Average_Yield_Tonnes_Ha=("Yield_Tonnes_Ha", "mean"),
        Average_Production_Tonnes=("Production_Tonnes", "mean"),
        Average_Revenue_INR=("Revenue_INR", "mean"),
        Average_Cost_INR=("Total_Cost_INR", "mean"),
        Average_Profit_INR=("Profit_INR", "mean"),
        Average_Water_Used_m3=("Water_Used_m3", "mean"),
        Average_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean"),
        Average_Disease_Pest_Risk=("Disease_Pest_Risk_pct", "mean"),
    )
    .reset_index()
)
season_summary.to_csv(os.path.join(OUTPUT_DIR, "season_summary.csv"), index=False)

crop_summary = (
    df_clean.groupby("Crop")
    .agg(
        Average_Yield_Tonnes_Ha=("Yield_Tonnes_Ha", "mean"),
        Average_Production_Tonnes=("Production_Tonnes", "mean"),
        Average_Revenue_INR=("Revenue_INR", "mean"),
        Average_Profit_INR=("Profit_INR", "mean"),
    )
    .sort_values("Average_Yield_Tonnes_Ha", ascending=False)
    .reset_index()
)
crop_summary.to_csv(os.path.join(OUTPUT_DIR, "crop_summary.csv"), index=False)

# Correlation matrix for important numeric variables
corr_cols = [
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Soil_Moisture_pct",
    "Seed_Quality_Score",
    "Water_Efficiency_t_per_1000m3",
    "Fertilizer_kg_ha",
    "Disease_Pest_Risk_pct",
    "Market_Price_INR_Tonne",
    "Total_Cost_INR",
    "Yield_Tonnes_Ha",
    "Profit_INR",
]
corr = df_clean[corr_cols].corr(numeric_only=True)
corr.to_csv(os.path.join(OUTPUT_DIR, "correlation_matrix.csv"))

# Data-quality summary
quality = pd.DataFrame({
    "Metric": [
        "Rows",
        "Columns",
        "Missing values",
        "Rows with missing values",
        "Duplicate rows",
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.isna().sum().sum()),
        int(df.isna().any(axis=1).sum()),
        duplicate_rows,
    ],
})
quality.to_csv(os.path.join(OUTPUT_DIR, "data_quality_summary.csv"), index=False)

# -----------------------------
# Charts
# -----------------------------
plt.figure(figsize=(9, 5))
plt.bar(season_summary["Season"], season_summary["Average_Yield_Tonnes_Ha"])
plt.title("Average Yield by Season")
plt.xlabel("Season")
plt.ylabel("Average Yield (Tonnes/Ha)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "seasonal_yield.png"), dpi=200)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(season_summary["Season"], season_summary["Average_Profit_INR"])
plt.title("Average Profit by Season")
plt.xlabel("Season")
plt.ylabel("Average Profit (INR)")
plt.axhline(0, linewidth=1)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "seasonal_profit.png"), dpi=200)
plt.close()

plt.figure(figsize=(10, 5))
plt.bar(crop_summary["Crop"], crop_summary["Average_Yield_Tonnes_Ha"])
plt.title("Average Yield by Crop")
plt.xlabel("Crop")
plt.ylabel("Average Yield (Tonnes/Ha)")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "crop_yield.png"), dpi=200)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(season_summary["Season"], season_summary["Average_Water_Efficiency"])
plt.title("Average Water Efficiency by Season")
plt.xlabel("Season")
plt.ylabel("Water Efficiency (t/1000 m³)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "water_efficiency.png"), dpi=200)
plt.close()

plt.figure(figsize=(10, 8))
plt.imshow(corr, aspect="auto")
plt.colorbar(label="Pearson correlation")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_matrix.png"), dpi=200)
plt.close()

# Print concise results for terminal use
print("\n=== Seasonal Agriculture Performance Analysis ===")
print(f"Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Missing values: {int(df.isna().sum().sum())}")
print(f"Duplicate rows: {duplicate_rows}\n")
print(season_summary[[
    "Season",
    "Average_Yield_Tonnes_Ha",
    "Average_Profit_INR",
    "Average_Water_Efficiency"
]].to_string(index=False))

print("\nTop crops by average yield:")
print(crop_summary[["Crop", "Average_Yield_Tonnes_Ha"]].head(8).to_string(index=False))

print("\nImportant correlations with Yield:")
print(corr["Yield_Tonnes_Ha"].sort_values(ascending=False).to_string())

print("\nAnalysis completed. Check the outputs/ folder.")
