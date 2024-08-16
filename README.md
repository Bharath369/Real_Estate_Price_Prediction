# Real Estate Price Prediction

## Overview
This project focuses on predicting real estate prices using various machine learning models. The goal is to provide accurate predictions based on a dataset containing features such as location, size, and amenities of properties.

### Problem Statement
The objective is to develop a model that can predict the sale prices of houses based on historical data. The project involves data preprocessing, feature engineering, model training, and evaluation.

## Data
The dataset includes features like:
- **Location**: City or neighborhood of the property.
- **Size**: Total area of the property in square feet.
- **Bedrooms**: Number of bedrooms.
- **Bathrooms**: Number of bathrooms.
- **Year Built**: The year the property was constructed.
- **Sale Price**: The target variable representing the property's sale price.

### Key Data Files
- `training_data.csv`: The training dataset used for model development.
- `test_data.csv`: The testing dataset used for model evaluation.

## Analysis
Data analysis and feature engineering were performed using Jupyter notebooks. The model development process included the following steps:
1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and feature scaling.
2. **Feature Engineering**: Creating new features to improve model performance.
3. **Model Training**: Various machine learning models were trained and evaluated, including Linear Regression, Random Forest, and Gradient Boosting.
4. **Model Evaluation**: Models were evaluated based on RMSE, R², and other relevant metrics.

For detailed analysis, refer to the [Python Scripts](scripts/Home.py).

## Strategy and Recommendations
The best-performing model was selected based on evaluation metrics. It was then fine-tuned to optimize prediction accuracy. The final model can be used by real estate agencies to provide price estimates for properties based on their features.

### Model Files
- `house_price_model.pkl`: The saved model file for deployment or further use.

## Tools Used
- **Python**: Core programming language used for data manipulation and model training.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For model training and evaluation.
- **Jupyter Notebook**: For exploratory data analysis and prototyping.
- **Matplotlib/Seaborn**: For data visualization.

## Installation
To run this project, install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
