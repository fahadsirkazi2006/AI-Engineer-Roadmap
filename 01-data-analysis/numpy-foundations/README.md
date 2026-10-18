# NumPy Foundations — AI/ML Roadmap

A hands-on Python project exploring **NumPy fundamentals for data analysis and machine learning**. This project focuses on numerical computation, array manipulation, statistical analysis, Boolean filtering, and feature scaling.

## 🎯 Project Objectives

- Understand NumPy arrays and their properties.
- Perform vectorized calculations without explicit loops.
- Analyze numerical data using statistical functions.
- Filter data using Boolean masks and multiple conditions.
- Work with multidimensional arrays through indexing and slicing.
- Understand axes and column-wise calculations.
- Implement min-max scaling using a reusable Python function.
- Handle edge cases such as arrays containing identical values.

## 🛠️ Tech Stack

- **Language:** Python
- **Library:** NumPy
- **Editor:** Visual Studio Code

## 📚 Concepts Practiced

### 1. NumPy Arrays and Vectorization

Created NumPy arrays and performed element-wise calculations, including increasing salaries by a percentage.

### 2. Statistical Analysis

Practiced calculating:

- Mean using `np.mean()`
- Median using `np.median()`
- Minimum and maximum using `np.min()` and `np.max()`
- Standard deviation using `np.std()`

Explored how extreme values can affect the mean and standard deviation, while the median is generally more robust to outliers.

### 3. Boolean Masking and Filtering

Used Boolean masks to identify salaries above the average and filter values within a specified range.

Also calculated the percentage of salaries above the average using Boolean values and `np.sum()`.

### 4. Array Properties

Explored:

- `array.shape` — dimensions along each axis
- `array.ndim` — number of dimensions
- `array.size` — total number of elements

### 5. Indexing and Slicing

Practiced selecting individual elements, rows, columns, and subsets of a two-dimensional array.

### 6. Axis-Based Calculations

Used `axis=0` to calculate statistics column-wise and `axis=1` to calculate them row-wise.

Learned that calculations can be mathematically valid without being meaningful when columns use incompatible units.

### 7. Min-Max Scaling

Implemented min-max scaling to transform numerical values into the range `[0, 1]`.

Formula:

`scaled = (value - minimum) / (maximum - minimum)`

Created a reusable `min_max_scale()` function and added handling for constant arrays, where the minimum equals the maximum.

## 💻 Example

```python
import numpy as np

def min_max_scale(values):
    x_min = np.min(values)
    x_max = np.max(values)

    if x_min == x_max:
        return np.zeros_like(values, dtype=float)

    return (values - x_min) / (x_max - x_min)

salaries = np.array([45000, 70000, 25000, 90000])

print("Mean salary:", np.mean(salaries))
print("Median salary:", np.median(salaries))
print("Normalized salaries:", min_max_scale(salaries))
```



## 🧠 Key Learnings

- Vectorized operations can make numerical calculations concise and efficient.
- Boolean indexing provides a convenient way to filter numerical data.
- Mean and median respond differently to extreme values.
- Array shapes and axes are important when preparing data for ML models.
- Feature scaling changes numerical ranges but does not remove the influence of outliers.
- Reusable functions should handle edge cases explicitly.

## 🔭 Next Steps

- Explore Pandas for real-world data cleaning and analysis.
- Practice descriptive statistics and exploratory data analysis.
- Learn SQL for data retrieval and aggregation.
- Apply these foundations to a supervised machine-learning project.



Learning AI/ML through practical, project-based development.

