
YZV311E - Data Mining Project Proposal
Predictive Model for E-commerce Replenishment

1. Introduction
In the rapidly evolving world of e-commerce, personalized customer experience is increasingly essential. This project addresses a key challenge faced by an e-commerce platform: predicting when customers will need to repurchase essential household items like personal care products, cleaning supplies, and pet food. By accurately forecasting which products are needed and the likely week they’ll be needed, our model aims to provide timely and useful recommendations to customers. This will not only enhance customer satisfaction but also promote long-term loyalty to the platform.

2. Dataset Overview
The dataset for this project, provided by Kaggle, includes transaction histories that detail customer purchasing patterns over time. This data allows us to explore the frequency of purchases and identify key trends in buying behavior. Our goal is to use these patterns to predict future needs, helping the platform give recommendations just when customers might be running low on essential items. We believe the insights gained will make a meaningful impact on the platform’s service quality.

3. Literature Review
Our research focuses on understanding the models commonly used in predictive analytics, especially those applied in recommendation systems. Classical models like collaborative filtering and decision trees have been widely studied for their effectiveness in providing personalized suggestions. However, they sometimes struggle with time-specific recommendations, which are crucial for restocking predictions. More recent studies highlight advanced models, such as gradient boosting machines (GBM) and recurrent neural networks (RNN), which offer greater predictive power for temporal data. In our project, we aim to test a mix of these traditional and advanced models to achieve high accuracy while balancing complexity.

4. Candidate Models
To tackle this problem, we plan to experiment with several models:

Logistic Regression and Decision Trees: These will serve as our baseline models to provide an initial understanding of prediction accuracy.
Random Forests and Gradient Boosting Machines (GBMs): These models are more sophisticated and capable of capturing complex data patterns, making them promising for this task.
Recurrent Neural Networks (RNNs): Since purchase data is sequential, RNNs could capture temporal dependencies effectively, giving more precise predictions about repurchase timing.
Each model will be evaluated based on its ability to deliver accurate and practical recommendations.

5. Evaluation Strategy
We’ll evaluate our models based on:

Accuracy: To ensure our predictions align closely with actual purchase behavior.
F1 Score: For balancing precision and recall, especially important in ensuring relevant recommendations.
Root Mean Square Error (RMSE): To assess the deviation between predicted and actual purchase times.
Additionally, cross-validation will be employed to verify model reliability and minimize overfitting, ensuring the model generalizes well on unseen data.
