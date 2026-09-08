# Seasonal Agriculture Performance Analysis

A data analytics project for analyzing seasonal agricultural performance using yield, production, revenue, cost, profit, environmental conditions, water use, and crop-risk indicators.

## Project Objectives
- Compare agricultural performance across Kharif, Rabi, and Zaid seasons.
- Study environmental conditions such as rainfall, temperature, humidity, sunlight, and soil moisture.
- Analyze water usage and water efficiency.
- Examine crop profitability and production.
- Identify relationships between agricultural variables using correlation analysis.
- Generate charts and summary tables for decision-making.

## Dataset
The project uses the supplied `seasonal_agriculture_performance_dataset.csv`.

Main categories include:
- Crop and location information
- Season and irrigation method
- Environmental conditions
- Farm area, yield, and production
- Water use and water efficiency
- Fertilizer and seed quality
- Disease/pest risk
- Market price, revenue, cost, and profit

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the analysis
```bash
python src/agriculture_analysis.py
```

The script creates charts and summary CSV files in the `outputs/` folder.

## Key Findings
- Kharif has the highest average yield and profit among the three seasons in the supplied dataset.
- Zaid has the lowest average yield and negative average profit.
- Zaid also shows the highest average water use and lowest water efficiency.
- Sugarcane has a much higher average yield than the other crops, so crop mix should be considered when comparing seasonal averages.
- Water efficiency and yield show a very strong positive correlation in the dataset; this should be interpreted carefully because the variables are structurally related.
- Rainfall and soil moisture have very weak pooled linear correlations with yield, indicating that seasonal and crop-level context matters.

## Project Deliverables
- Source dataset
- Python analysis script
- Generated charts
- Summary CSV files
- Project PowerPoint can be submitted separately

## Author
Student Name: [Your Name]  
College: [Your College]  
AICTE STU ID: [Your ID]  
GitHub: [Your GitHub Repository URL]
