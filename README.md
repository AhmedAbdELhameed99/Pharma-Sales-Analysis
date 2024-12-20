# Pharma Sales Data Analysis

## Project Overview
This project involves analyzing pharmaceutical sales data to derive insights and improve business decision-making. The dataset includes daily, weekly, and monthly sales data for three products (`M01AB`, `M01AE`, `N02BA`). The analysis is performed using **Python**, **Power BI**, and **DAX** to create dynamic, interactive reports.

---

## Objectives
1. Analyze sales trends across daily, weekly, and monthly intervals.
2. Calculate growth rates and cumulative sales for better understanding of business performance.
3. Design interactive dashboards to help stakeholders explore the data effectively.

---

## Tools and Technologies
- **Python**: For initial data processing and exploratory analysis.
- **Power BI**: For creating dashboards and interactive reports.
- **DAX (Data Analysis Expressions)**: To build calculated measures for advanced analytics.

---

## Steps to Reproduce

### 1. Data Preprocessing
- **Input Files**: Load `salesdaily.csv`, `salesweekly.csv`, and `salesmonthly.csv`.
- **Cleaning**: Handle missing values and format date fields appropriately.
- **Tools**: Use Python's pandas library.

### 2. Data Analysis in Python
- Calculate total daily, weekly, and monthly sales.
- Compute cumulative and growth metrics.

### 3. Report Design in Power BI
- Import the cleaned datasets into Power BI.
- Build visualizations:
  - **Line Chart**: Daily sales trends.
  - **Clustered Column and Line Chart**: Monthly sales and growth rates.
  - **Area Chart**: Cumulative sales over time.

### 4. DAX Measures for Advanced Analytics
Examples of DAX measures used in Power BI:
- **Total Daily Sales**:
```DAX
Total Daily Sales = SUM(salesdaily[M01AB]) + SUM(salesdaily[M01AE]) + SUM(salesdaily[N02BA],...)
```
- **Monthly Growth**:
```DAX
Monthly Growth = DIVIDE(
    [Total Monthly Sales] - CALCULATE([Total Monthly Sales], PREVIOUSMONTH(salesmonthly[datum])),
    CALCULATE([Total Monthly Sales], PREVIOUSMONTH(salesmonthly[datum]))
)
```
---

## Visualization
### Power BI Dashboard:
![image_alt](https://github.com/AhmedAbdELhameed99/Pharma-Sales-Analysis/blob/main/Pharma%20Dashboard.jpg?raw=true)

---

## Contact
For questions or collaboration, feel free to reach out:
- **Email**: ahmed99abdelhameed@gmail.com
