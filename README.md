# 🌾 Seasonal Agriculture Performance Analysis

**VOIS AICTE Major Project — Data Analytics**

This project analyzes seasonal agricultural performance using a dataset containing crop, farm, environmental, irrigation, resource-use, risk, revenue, cost, and profit information.

## 📌 Objectives
- Compare Kharif, Rabi, and Zaid agricultural performance.
- Analyze yield, production, revenue, cost, and profit.
- Study rainfall, temperature, humidity, sunlight, and soil moisture.
- Evaluate water usage and water efficiency.
- Compare crop-level performance.
- Analyze relationships between agricultural variables using Pearson correlation.
- Provide data-driven recommendations for better resource and farm management.

## 📂 Repository Structure

```text
Seasonal-Agriculture-Performance-Analysis/
├── data/
│   └── seasonal_agriculture_performance_dataset.csv
├── outputs/
│   ├── season_summary.csv
│   ├── crop_summary.csv
│   ├── correlation_matrix.csv
│   ├── data_quality_summary.csv
│   ├── seasonal_yield.png
│   ├── seasonal_profit.png
│   ├── crop_yield.png
│   ├── water_efficiency.png
│   └── correlation_matrix.png
├── src/
│   └── agriculture_analysis.py
├── Seasonal_Agriculture_Performance_Analysis.ipynb
├── requirements.txt
└── README.md
```

## 🧹 Data Quality
The supplied dataset contains **4,000 rows and 28 columns**. There are **120 missing values across 120 rows**, with missing values in rainfall, soil moisture, and yield fields. There are **no duplicate rows**.

For the analysis workflow, numeric missing values are median-imputed and categorical missing values are mode-imputed. The original dataset remains unchanged in `data/`.

## 📊 Key Findings
- **Kharif** records the highest average yield and average profit among the three seasons.
- **Zaid** records the lowest average yield and negative average profit.
- Zaid has the highest average water use and lowest average water efficiency.
- Kharif has the highest average water efficiency.
- Sugarcane has a much higher average yield than the other crops, so crop mix is important when interpreting seasonal averages.
- Water efficiency and yield show a very strong positive correlation in the supplied data. This should be interpreted cautiously because the variables are structurally related.
- Rainfall and soil moisture have very weak pooled linear correlations with yield.
- Correlation indicates association and does **not** establish causation.

## ▶️ Run the Python Analysis

```bash
pip install -r requirements.txt
python src/agriculture_analysis.py
```

## 📓 Run the Notebook

Open `Seasonal_Agriculture_Performance_Analysis.ipynb` in Jupyter Notebook, JupyterLab, VS Code, or Google Colab.

## 🛠️ Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- CSV / tabular data analysis

## 📈 Deliverables
The `outputs/` directory contains the generated summary tables and charts used for the project presentation.

## 👤 Project Information
**Student Name:** THATI VIGNESH
**College:** Chaitanya Bharathi Institute Of Technology 
**AICTE STU ID:** STU6a1beae960e691780214505
**GitHub:** https://github.com/Vignesh906/seasonal_agriculture_performance

Replace the first three placeholders before final submission.
