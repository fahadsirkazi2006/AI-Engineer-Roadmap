## Exploratory Data Analysis (EDA) Findings

### 1. Data Quality and Cleaning

The original dataset contained missing values and invalid entries. Some values were represented as strings such as `"unknown"` and `"three"`, while missing salaries were read as `NaN` by Pandas. Since invalid strings are not automatically treated as missing values, I used numeric conversion with `errors="coerce"` to identify invalid numeric entries. I then removed a row with multiple missing fields, replaced missing salary values with the median, and validated the cleaned dataset.

### 2. Purchasing Behaviour

The exploratory analysis showed that customers who purchased the product had a higher average salary and a higher average age than customers who did not purchase it. I also compared age distributions using grouped statistics, quartiles, and a box plot. These observations suggest possible relationships between age, salary, and purchasing behaviour, but they do not establish causation or guarantee accurate predictions.

### 3. Dataset Limitations

The dataset contains only 10 customers after cleaning, which is too small to draw reliable conclusions about a larger population or train a dependable predictive model. Purchasing decisions may depend on additional factors, such as product preferences, customer needs, product pricing, and marketing exposure. The dataset is synthetic, so its patterns may not reflect real-world customer behaviour.
