import pandas as pd

# Load datasets
product_catalog = pd.read_csv('product_catalog.csv')
product_category_map = pd.read_csv('product_category_map.csv')

# Ensure both merge keys have the same data type
product_catalog['categories'] = product_catalog['categories'].astype(str)
product_category_map['category_id'] = product_category_map['category_id'].astype(str)

# Split categories lists into separate rows
# Remove brackets and split by comma, then explode into separate rows
product_catalog['categories'] = product_catalog['categories'].str.strip('[]').str.split(', ')
product_catalog = product_catalog.explode('categories')

# Trim any extra whitespace and ensure categories are strings
product_catalog['categories'] = product_catalog['categories'].str.strip()
product_catalog['categories'] = product_catalog['categories'].astype(str)

# Merge with product_category_map to add parent_category information
product_catalog = product_catalog.merge(
    product_category_map,
    left_on='categories',
    right_on='category_id',
    how='left'
).rename(columns={'parent_category_id': 'parent_category'})

# Fill any remaining NaN values in parent_category if necessary
product_catalog['parent_category'] = product_catalog['parent_category'].fillna('Unknown')

# Save or inspect the results
product_catalog.to_csv('expanded_product_catalog.csv', index=False)
