# 🔎 AI Dataset Explorer — Python

A beginner-friendly data-quality and preprocessing pipeline built from scratch using Python's built-in `csv` module.

This project was created as part of my AI/ML engineering learning roadmap.

## 🎯 Why I Built This

Before using libraries such as Pandas, I wanted to understand what actually happens when raw data is loaded, inspected, validated, and cleaned.

Instead of immediately using high-level data-processing functions, I implemented the core workflow manually using Python.

The next step is to recreate this workflow using Pandas and compare both approaches.

---

## 🛠️ What This Project Does

The pipeline currently:

* Reads customer data from a CSV file
* Dynamically identifies columns from the CSV header
* Converts numeric values to appropriate Python types
* Detects missing values
* Validates values against expected data types
* Tracks invalid values by column
* Calculates invalid-value percentages
* Cleans invalid and missing values
* Converts `yes/no` values into `1/0`
* Generates a cleaning report
* Identifies records that are usable for machine learning

---

## 📊 Example Dataset

The dataset contains customer information such as:

| Column       | Description                                |
| ------------ | ------------------------------------------ |
| `name`       | Customer name                              |
| `age`        | Customer age                               |
| `salary`     | Customer salary                            |
| `experience` | Years of experience                        |
| `purchased`  | Whether the customer purchased the product |

The dataset intentionally contains a few malformed values so that the pipeline can detect and handle them.

For example:

```text
"unknown" → None
"N/A"     → None
"three"   → None
"yes"     → 1
"no"      → 0
```

---

## 🔄 Pipeline

```text
Raw CSV
   ↓
CSV Parsing
   ↓
Dictionary-based Dataset
   ↓
Automatic Type Detection
   ↓
Data Validation
   ↓
Invalid-value Analysis
   ↓
Data Cleaning
   ↓
Cleaning Report
   ↓
ML-ready Records
```

---

## 🧠 Concepts Practiced

This project helped me practice:

* Python lists
* Dictionaries
* Loops
* Conditional statements
* `try/except`
* Type conversion
* `isinstance()`
* `None`
* CSV iterators
* Data validation
* Data cleaning
* Basic data-quality metrics

---

## 📈 Data Quality Checks

The pipeline reports:

* Total number of rows
* Number of columns
* Missing values
* Invalid values
* Invalid values by column
* Invalid-value percentage
* Number of cleaned values
* Number of usable records

---

## 🚀 What's Next?

This is intentionally the **manual Python implementation**.

The next version of the project will use:

```text
🐼 Pandas
```

to perform the same data-processing tasks and explore how professional data-analysis workflows simplify the operations implemented manually here.

After that, the roadmap will progress toward:

```text
Python
   ↓
NumPy
   ↓
Pandas
   ↓
EDA & Statistics
   ↓
SQL
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
Computer Vision
   ↓
Generative AI
   ↓
RAG
   ↓
MLOps & Deployment
```

---

## 📁 Project Structure

```text
dataset-explorer/
│
├── data/
│   └── customers.csv
│
├── main.py
│
└── README.md
```

---

## ⚠️ Note

This is a learning project rather than a production data-processing system.

The goal was to understand the fundamentals of data ingestion, validation, cleaning, and preprocessing before relying on higher-level libraries.
