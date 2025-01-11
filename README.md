
# YZV311E - Data Mining Project: Predictive Analytics for E-commerce Replenishment

## Project Overview
This project aims to develop a predictive model for a major e-commerce platform to enhance customer experience by anticipating their replenishment needs. By analyzing customer purchasing behavior, we aim to predict when essential items will be needed again, allowing the platform to provide timely and relevant product recommendations.

## Table of Contents
* [Project Overview](#project-overview)
* [Proposal](#proposal)
* [Dataset](#dataset)
* [Methodology](#methodology)
* [Evaluation](#evaluation)
* [Installation and Usage](#installation-and-usage)
* [Team](#team)
* [Timeline](#timeline)
* [License](#license)

## Proposal
In this project, we aim to develop a predictive analytics system for a leading global e-commerce platform to improve customer experience by forecasting customer repurchase behavior. The platform seeks to provide timely recommendations for customers to restock frequently purchased household and consumable products. Our goal is to predict not only which products a customer is likely to repurchase but also the specific week when they will need to replenish their stock. For a detailed description of the project objectives, dataset, candidate models, and our evaluation plan, please refer to the [Project Proposal](https://github.com/umutcalikkasap/YZV311_2425_150210721_150210336/blob/main/Proposal.md).

## Dataset
The dataset provided consists of four CSV files:
- `transactions_reduced.csv`: Transaction data containing customer ID, product ID, purchase date, and quantity.
- `test_reduced.csv`: Test dataset with customer ID and product ID for making predictions.
- `product_category_map_reduced.csv`: Mapping of category IDs to parent category IDs.
- `product_catalog_reduced.csv`: Product information including product ID, manufacturer ID, and associated category IDs.

The transaction dataset spans a specific time range and includes a large number of customers, products, and transactions. We plan to preprocess the data and engineer relevant features to support our predictive models. Access the dataset on [Kaggle](link-to-kaggle-competition).

## Methodology
We will explore a range of machine learning models, including:
- **Logistic Regression and Decision Trees**: For baseline performance.
- **Random Forests and Gradient Boosting Machines (GBMs)**: To capture complex relationships.
- **Recurrent Neural Networks (RNNs)**: For sequential pattern recognition, suited for time-dependent purchase prediction.

The specific algorithms and methods will be determined as the project progresses, based on initial findings and performance evaluations.

## Evaluation
Our models will be evaluated based on:
- **Accuracy**
- **F1 Score**
- **Root Mean Square Error (RMSE)**

Cross-validation will be used to ensure robustness and mitigate overfitting. We will employ cross-validation and train-test split techniques to validate our models and ensure their generalization ability.

## Installation and Usage
Instructions for installing and running the project code will be provided here once the project is underway.

## Team
- **Umut Çalıkkasap**: Focused on data preprocessing, literature review, and exploratory analysis, handling model development, tuning, and evaluation.

## Timeline
• **Week 1-2:** Data preprocessing and exploratory analysis
• **Week 3-5:** Model development and training
• **Week 5-6:** Model evaluation and refinement
• **Week 7:** Final predictions and submission to Kaggle

## License
This project is licensed under the MIT License. See [LICENSE]([link-to-license-file](https://github.com/umutcalikkasap/YZV311_2425_150210721_150210336/blob/main/LICENSE)) for more details.
