import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import gc
import ast

# Sonuç dosyasını temizle
output_file = 'filled_product_catalog.csv'
if os.path.exists(output_file):
    os.remove(output_file)

# expanded_product_catalog_imputed.csv dosyasını eğitim için yükle
expanded_product_catalog_imputed = pd.read_csv('expanded_product_catalog_imputed.csv')
train_data = expanded_product_catalog_imputed.dropna(subset=['categories'])

# product_catalog.csv dosyasını yükle
product_catalog = pd.read_csv('product_catalog.csv')

# product_catalog'taki categories kolonundaki listeleri ilk elemanına indirgeme
def extract_first_category(categories):
    if pd.isna(categories):
        return None
    try:
        categories_list = ast.literal_eval(categories)
        if isinstance(categories_list, list) and len(categories_list) > 0:
            return categories_list[0]
        return categories_list
    except (ValueError, SyntaxError):
        return categories

product_catalog['first_category'] = product_catalog['categories'].apply(extract_first_category)

# training data
features = ['product_id', 'manufacturer_id', 'attribute_1', 'attribute_2', 'attribute_3', 'attribute_4', 'attribute_5']
X_train = train_data[features]
y_train = train_data['categories']

# Random Forest model training
clf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
clf.fit(X_train, y_train)

# predict the missing categoriess
chunk_size = 500
with pd.read_csv('product_catalog.csv', chunksize=chunk_size) as reader:
    for chunk in reader:
        chunk['first_category'] = chunk['categories'].apply(extract_first_category)
        missing_categories = chunk[chunk['first_category'].isna()]
        
        if not missing_categories.empty:
            X_test = missing_categories[features]
            predicted_categories = clf.predict(X_test)
            chunk.loc[chunk['first_category'].isna(), 'first_category'] = predicted_categories
        
        # save the results
        chunk.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))
        
        # free memory
        del X_test, missing_categories, chunk
        gc.collect()
