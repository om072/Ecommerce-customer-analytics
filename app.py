import os
import streamlit as st
import pandas as pd
from utils import (
    load_data,
    perform_eda,
    create_customer_features,
    find_lookalikes,
    perform_clustering,
)

# App Config
st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide")

# Create results directory if it doesn't exist
if not os.path.exists("results"):
    os.makedirs("results")

# Load Data
st.title("Customer Analytics Dashboard")
st.sidebar.header("Navigation")

st.sidebar.markdown("Choose an option:")
options = st.sidebar.radio(
    "",
    [
        "Home",
        "EDA",
        "Lookalike Model",
        "Customer Segmentation",
        "Product Recommendations",
    ],
)

# Load the data
customers_df, products_df, transactions_df = load_data()

# Task: Home Page
if options == "Home":
    st.write("Welcome to the Customer Analytics Dashboard!")
    st.write(
        "Navigate through the options in the sidebar for detailed insights and analyses."
    )

# Task: EDA
if options == "EDA":
    st.header("Exploratory Data Analysis (EDA)")
    st.write("Key metrics and visualizations:")

    # Display metrics
    metrics = perform_eda(customers_df, products_df, transactions_df)
    st.write(metrics)

    # Visualizations
    st.subheader("Visualizations")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "eda_plots/customer_region_distribution.png",
            caption="Customer Distribution by Region",
        )

    with col2:
        st.image(
            "eda_plots/product_category_distribution.png",
            caption="Products by Category",
        )

    with col3:
        st.image("eda_plots/daily_transactions.png", caption="Daily Transaction Values")

# Task: Lookalike Model
if options == "Lookalike Model":
    st.header("Lookalike Model")

    customer_id = st.sidebar.selectbox("Select Customer ID", customers_df["CustomerID"])
    customer_features = create_customer_features(
        customers_df, transactions_df, products_df
    )

    if st.sidebar.button("Generate Lookalikes"):
        lookalikes = find_lookalikes(customer_features, customer_id)
        st.write(f"Customers similar to {customer_id}:")
        for lookalike, score in lookalikes:
            st.write(f"Customer ID: {lookalike}, Similarity Score: {score:.2f}")

# Task: Customer Segmentation
if options == "Customer Segmentation":
    st.header("Customer Segmentation")
    n_clusters = st.sidebar.slider(
        "Select Number of Clusters", min_value=2, max_value=10, value=5
    )

    if st.sidebar.button("Perform Clustering"):
        customer_features = create_customer_features(
            customers_df, transactions_df, products_df
        )
        clustered_customers, db_index = perform_clustering(
            customer_features, n_clusters
        )

        st.write(f"Davies-Bouldin Index: {db_index:.2f}")

        # Show clustering results
        st.subheader("Clustered Customers")
        st.dataframe(clustered_customers[["CustomerID", "Cluster"]])

        # Show cluster visualization
        st.image("cluster_visualization.png", caption="Cluster Visualization")

# Task: Product Recommendations
if options == "Product Recommendations":
    st.header("Product Recommendations")

    # Select Customer
    customer_id = st.sidebar.selectbox("Select Customer ID", customers_df["CustomerID"])
    customer_features = create_customer_features(
        customers_df, transactions_df, products_df
    )

    if st.sidebar.button("Get Recommendations"):
        # Generate lookalikes
        lookalikes = find_lookalikes(customer_features, customer_id)
        similar_customer_ids = [cust for cust, _ in lookalikes]

        # Get products bought by similar customers but not by the selected customer
        customer_purchases = transactions_df[
            transactions_df["CustomerID"] == customer_id
        ]["ProductID"].unique()
        similar_customers_purchases = transactions_df[
            transactions_df["CustomerID"].isin(similar_customer_ids)
        ]["ProductID"].unique()

        recommended_products = set(similar_customers_purchases) - set(
            customer_purchases
        )
        recommended_products_df = products_df[
            products_df["ProductID"].isin(recommended_products)
        ]

        # Display Recommendations
        st.write(f"Products recommended for Customer ID {customer_id}:")
        st.dataframe(recommended_products_df)

        # Save Recommendations to a CSV
        file_path = f"results/recommendations_{customer_id}.csv"
        recommended_products_df.to_csv(file_path, index=False)
        st.write(f"Recommendations saved to: `{file_path}`")
