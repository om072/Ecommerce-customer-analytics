# eCommerce Customer Analytics

## Project Overview
This project performs comprehensive analysis of eCommerce transaction data to derive business insights and build customer analytics models. The analysis includes exploratory data analysis (EDA), customer lookalike modeling, and customer segmentation using clustering techniques.

## Table of Contents
* [Dataset Description](#dataset-description)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Results](#results)
* [Technologies Used](#technologies-used)

## Dataset Description
The analysis uses three main datasets:

1. **Customers.csv**
   * CustomerID: Unique identifier for each customer
   * CustomerName: Name of the customer
   * Region: Continent where the customer resides
   * SignupDate: Date when the customer signed up

2. **Products.csv**
   * ProductID: Unique identifier for each product
   * ProductName: Name of the product
   * Category: Product category
   * Price: Product price in USD

3. **Transactions.csv**
   * TransactionID: Unique identifier for each transaction
   * CustomerID: ID of the customer who made the transaction
   * ProductID: ID of the product sold
   * TransactionDate: Date of the transaction
   * Quantity: Quantity of the product purchased
   * TotalValue: Total value of the transaction
   * Price: Price of the product sold

## Project Structure
```
ecommerce-customer-analytics/
│
├── data/
│   ├── Customers.csv
│   ├── Products.csv
│   └── Transactions.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Lookalike_Model.ipynb
│   └── Customer_Segmentation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_analysis.py
│   ├── lookalike_model.py
│   └── clustering.py
│
├── results/
│   ├── eda_plots/
│   ├── Lookalike.csv
│   └── clustering_results/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-customer-analytics.git
cd ecommerce-customer-analytics
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preparation**:
   * Place your CSV files in the `data/` directory
   * Ensure the file names match the expected format

2. **Run EDA**:
```bash
python src/eda_analysis.py
```

3. **Generate Lookalike Recommendations**:
```bash
python src/lookalike_model.py
```

4. **Perform Customer Segmentation**:
```bash
python src/clustering.py
```

## Features

### 1. Exploratory Data Analysis
* Customer distribution analysis
* Product category analysis
* Transaction patterns analysis
* Key business metrics calculation

### 2. Lookalike Model
* Customer feature engineering
* Similarity score calculation
* Top 3 similar customers recommendations
* Outputs recommendations for customers C0001-C0020

### 3. Customer Segmentation
* K-means clustering implementation
* Davies-Bouldin Index calculation
* Cluster visualization using PCA
* Detailed cluster analysis

## Results
The analysis generates several outputs:

1. **EDA Results**:
   * Visualizations in `results/eda_plots/`
   * Key metrics summary
   * Business insights report

2. **Lookalike Model Results**:
   * `Lookalike.csv` containing similar customer recommendations
   * Similarity scores for each recommendation

3. **Clustering Results**:
   * Customer segment assignments
   * Davies-Bouldin Index score
   * Cluster visualizations
   * Segment characteristics report

## Technologies Used
* Python 3.8+
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
