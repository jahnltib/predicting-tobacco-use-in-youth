# Tasks:
- Make appropriate transformations (wrote about most of them in `map_annotated.py`) before handling missing values.
  1. Merge columns together into new columns and drop all the old ones that were previously separate. Similar columns become one umbrella column. Ex. "Respondent used e-cigarettes due to exposure from friends, media, or family" encompasses multiple columns and reduces dimensions.
  2. Use one-hot encoding to separate a categorical labeled columns into separate columns for each category. Ex. Ages 0-13, 14-18, 19+ become their own categories.
  3. Consider combining attributes together that aren't necessarily similar but may be correlated.
- Then handle missing values with a high missing rate by replacing it with 0. Read explanation in `data_preprocessing.ipynb`.
- Exploratory Data Analysis Section could use some visualization but only if needed.

# READ:
1. Before running any code cells make sure to set up your venv following the instructions in the `data_preprocessing.ipynb` file.
