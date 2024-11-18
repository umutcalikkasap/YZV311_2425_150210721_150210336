import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

# Load the expanded catalog
expanded_product_catalog = pd.read_csv('expanded_product_catalog.csv')

# parent_category sütunundaki `Unknown` gibi eksik değerleri doldurmadan önce encode ediyoruz
expanded_product_catalog['parent_category'] = expanded_product_catalog['parent_category'].fillna('Unknown')
parent_category_le = LabelEncoder()
expanded_product_catalog['parent_category'] = parent_category_le.fit_transform(expanded_product_catalog['parent_category'].astype(str))

# İmpute işlemi için gerekli sütunları seçiyoruz (attribute sütunları ile tahmin yapacağız)
features_for_imputation = ['attribute_1', 'attribute_2', 'attribute_3', 'attribute_4', 'attribute_5', 'category_id', 'parent_category']
imputation_data = expanded_product_catalog[features_for_imputation].copy()

# KNNImputer kullanarak eksik 'category_id' ve 'parent_category' değerlerini dolduruyoruz
imputer = KNNImputer(n_neighbors=5)
imputed_data = imputer.fit_transform(imputation_data)

# Doldurulmuş veriyi orijinal dataframe'e geri aktarıyoruz
expanded_product_catalog['category_id'] = imputed_data[:, features_for_imputation.index('category_id')]
expanded_product_catalog['parent_category'] = imputed_data[:, features_for_imputation.index('parent_category')]

# Sonuçları kaydediyoruz
expanded_product_catalog.to_csv('expanded_product_catalog_imputed.csv', index=False)
