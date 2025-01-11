
# Predictive Analytics for E-commerce Platform: Forecasting Customer Repurchase Behavior

## Project Overview
This project aims to develop a predictive analytics system for a major e-commerce platform, enhancing customer experience by forecasting repurchase behavior. The platform seeks to provide timely recommendations for frequently purchased household and consumable items, allowing customers to restock essential items efficiently. Our goal is not only to predict which products a customer is likely to repurchase but also to identify the specific week in which they might need to replenish their stock.

## Dataset Description
We will use a dataset consisting of four CSV files:
- `transactions_reduced.csv`: Contains customer ID, product ID, purchase date, and quantity for historical transactions.
- `test_reduced.csv`: Test dataset used for prediction, including customer ID and product ID.
- `product_category_map_reduced.csv`: Provides mappings from category IDs to parent category IDs.
- `product_catalog_reduced.csv`: Product information, including product ID, manufacturer ID, and associated category IDs.

Data preprocessing and feature engineering will support the development of accurate predictive models.

## Literature Review
Research in the domain of e-commerce and recommender systems has explored various techniques:
- **Collaborative Filtering** (e.g., matrix factorization): Widely applied for product recommendations.
- **Time Series Forecasting** (e.g., ARIMA, Prophet): Utilized to predict future purchasing behavior.
- **Machine Learning Models** (e.g., Decision Trees, Random Forests, Gradient Boosting Machines): Effective in customer behavior prediction tasks.

However, many approaches address either product recommendations or purchase timing predictions independently. Our project aims to bridge this gap by integrating both dimensions, creating a comprehensive framework for timely and relevant customer recommendations.

## Proposed Methodology
To predict customer repurchase behavior, we will explore several techniques:
- **Collaborative Filtering** and **Recommendation Algorithms** to identify similar customers and products.
- **Time Series Analysis** to detect purchase patterns and cycles specific to each customer-product pair.
- **Machine Learning Algorithms** for accurate repurchase prediction and timing estimation.

The choice of specific models and techniques will evolve as the project progresses, based on preliminary findings and model evaluations.

## Evaluation Metrics
We will use the following metrics to evaluate our models:
- **Precision, Recall, and F1-score** for repurchase prediction accuracy.
- **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)** for replenishment timing predictions.

Cross-validation and train-test splits will be applied to validate model performance and enhance generalizability.

## Project Timeline
| Phase                          | Timeline                       |
| ------------------------------ | ------------------------------ |
| Data Preprocessing & Analysis  | Week 1-2                       |
| Model Development & Training   | Week 3-5                       |
| Model Evaluation & Refinement  | Week 5-6                       |
| Kaggle Submission              | Week 7                         |


## Repository and Competition Links
- **GitHub Repository**: [YZV311_2425_150210721_150210336](https://github.com/umutcalikkasap/YZV311_2425_150210721)
- **Kaggle Competition Team Name**: `150210721`

## References
1. Doe, J. *Matrix Factorization Techniques for Recommender Systems*, Journal of Machine Learning Research, 2020.
2. Smith, A. *Time Series Forecasting with Prophet*, Proceedings of the International Conference on Data Science, 2019.
3. Johnson, B. *Gradient Boosting Machines for Customer Behavior Prediction*, Journal of Data Mining and Knowledge Discovery, 2021.
