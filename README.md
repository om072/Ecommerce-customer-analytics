# Ecommerce_customer_analytics

This project provides a comprehensive analytics dashboard to analyze customer data, visualize trends, and offer actionable insights. The dashboard is built using Streamlit and supports interactive features like customer segmentation, lookalike models, and product recommendations.

## Screenshots
![image](https://github.com/user-attachments/assets/6c2b9aab-5861-49e3-a6d1-8978b63a1928)
![image](https://github.com/user-attachments/assets/70497136-451c-4cba-91e0-5a8836edb222)
![image](https://github.com/user-attachments/assets/720f3e52-c15b-4710-9d64-b7ebce4fb189)
![image](https://github.com/user-attachments/assets/d075f051-473a-4f9d-817a-d36f4d2d2d8d)





## Assignment Questions and Answers

### 1. Perform EDA on the provided dataset.

The EDA process includes:

* **Customer Analysis:**
    * Distribution by region
    * Signup dates and trends over time

* **Product Analysis:**
    * Most popular categories
    * Distribution of product sales

* **Transaction Analysis:**
    * Transaction values over time
    * Total revenue and average transaction value

Plots and metrics generated during EDA are saved in the `eda_plots` directory.

### 2. Derive at least 5 business insights from the EDA.

Here are the insights derived from the EDA:

1. **Regional Concentration:**
    * The majority of customers are concentrated in a few specific regions, indicating strong geographic preferences
    * These regions can be prioritized for targeted marketing campaigns

2. **Category Popularity:**
    * One or two product categories dominate sales, contributing significantly to revenue
    * Diversifying product offerings within these categories could increase cross-sell opportunities

3. **Revenue Seasonality:**
    * Transaction analysis reveals peaks during specific months, likely linked to holidays or seasonal demand
    * Planning inventory and marketing around these peaks can enhance profitability

4. **High-Value Customers:**
    * A small group of customers contributes disproportionately to the total revenue
    * Developing loyalty programs for these high-value customers can improve retention and lifetime value

5. **Underperforming Regions:**
    * Certain regions show significantly lower customer engagement and revenue
    * Exploring factors like product availability, pricing, or local preferences can help tap into these markets

## Deliverables

1. **EDA Code**
    * The EDA code is implemented in the `utils.py` module and executed as part of the `app.py` script
    * Key metrics and visualizations generated during EDA are saved in the `eda_plots` directory

2. **Business Insights**
    * A PDF report summarizing the above insights is included in the `results` directory

## Directory Structure
```
/data
    - Customers.csv
    - Products.csv
    - Transactions.csv
/utils.py
/app.py
/results
    - recommendations_<CustomerID>.csv (saved recommendation files)
    - business_insights_report.pdf (PDF report with EDA insights)
/eda_plots
    - customer_region_distribution.png
    - product_category_distribution.png
    - daily_transactions.png
```

## Installation

1. Clone the repository:
```bash
git clone 
cd 
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the data directory contains the following CSV files:
    * Customers.csv
    * Products.csv
    * Transactions.csv

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open the app in your browser at the URL displayed in the terminal (default: http://localhost:8501)

3. Navigate through the sidebar options for detailed insights and analyses

## Results

* **EDA Visualizations:** Saved in the `eda_plots` directory
* **Clustering and Recommendations:** Results saved in the `results` folder

## Future Enhancements

* Add time range filters for EDA
* Improve lookalike model with advanced algorithms
* Integrate predictive analytics for customer lifetime value (CLV) and churn prediction
* Deploy the app online using Streamlit Cloud, AWS, or Azure

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
OM KHANGAT
