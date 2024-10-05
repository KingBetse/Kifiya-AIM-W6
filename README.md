# Building a Credit Scoring Model for Buy-Now-Pay-Later Services: A Comprehensive Analysis of Credit Risk Classification

## Project Overview
This project aims to create a credit scoring model for Bati Bank, a leading financial service provider, in collaboration with a successful eCommerce platform. The goal is to enable a buy-now-pay-later service that allows customers to purchase products on credit if they qualify.

## Business Need
Bati Bank recognizes the growing demand for flexible payment solutions and aims to provide customers with the ability to buy products by credit. This requires developing a robust credit scoring model to assess the creditworthiness of potential borrowers. The model will utilize data from customer transactions to evaluate risk and determine suitable loan conditions.

## Objectives
- Define a proxy variable to categorize users as high risk (bad) or low risk (good).
- Select observable features that are strong predictors of the defined default variable.
- Develop a model that assigns risk probabilities for new customers.
- Develop a model that assigns credit scores based on risk probability estimates.
- Predict the optimal amount and duration of loans.

## Data and Features
The data for this project is sourced from the Xente Challenge on Kaggle. The dataset includes the following fields:

- **TransactionId**: Unique transaction identifier.
- **BatchId**: Unique batch number for processing.
- **AccountId**: Unique customer identifier on the platform.
- **SubscriptionId**: Unique identifier for customer subscriptions.
- **CustomerId**: Unique customer identifier.
- **CurrencyCode**: Currency of the transaction.
- **CountryCode**: Geographical code of the customer's country.
- **ProviderId**: Source provider of the purchased item.
- **ProductId**: Name of the purchased item.
- **ProductCategory**: Broader categories for products.
- **ChannelId**: Identifies the transaction channel (e.g., web, Android, iOS).
- **Amount**: Transaction value.
- **Value**: Absolute value of the transaction.
- **TransactionStartTime**: Timestamp of the transaction.
- **PricingStrategy**: Category of pricing structure.
- **FraudResult**: Fraud status (1 for yes, 0 for no).

## Folder Structure
- **src/**: Contains source code for data loading, feature engineering, and EDA.
- **tests/**: Contains unit and integration tests.
- **data/**: Contains raw and processed data files.
- **.github/**: Contains CI/CD configurations.
- **notebook/**: Contains the prediction, preprocessing, and analysis model.
- **scripts/**: Contains the main script to run and visualize.

