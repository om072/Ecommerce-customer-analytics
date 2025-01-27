# Import required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    customers_df = pd.read_csv("data/Customers.csv")
    products_df = pd.read_csv("data/Products.csv")
    transactions_df = pd.read_csv("data/Transactions.csv")

    # Convert date columns to datetime
    customers_df["SignupDate"] = pd.to_datetime(customers_df["SignupDate"])
    transactions_df["TransactionDate"] = pd.to_datetime(
        transactions_df["TransactionDate"]
    )

    return customers_df, products_df, transactions_df


# Task 1: Exploratory Data Analysis
def perform_eda(customers_df, products_df, transactions_df):
    # Create output directory for plots
    import os

    if not os.path.exists("eda_plots"):
        os.makedirs("eda_plots")

    # 1. Customer Analysis
    plt.figure(figsize=(10, 6))
    customers_df["Region"].value_counts().plot(kind="bar")
    plt.title("Customer Distribution by Region")
    plt.tight_layout()
    plt.savefig("eda_plots/customer_region_distribution.png")
    plt.close()

    # 2. Product Analysis
    plt.figure(figsize=(12, 6))
    products_df["Category"].value_counts().plot(kind="bar")
    plt.title("Products by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("eda_plots/product_category_distribution.png")
    plt.close()

    # 3. Transaction Analysis over time
    transactions_by_date = (
        transactions_df.groupby("TransactionDate")["TotalValue"].sum().reset_index()
    )
    plt.figure(figsize=(15, 6))
    plt.plot(
        transactions_by_date["TransactionDate"], transactions_by_date["TotalValue"]
    )
    plt.title("Daily Transaction Values")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("eda_plots/daily_transactions.png")
    plt.close()

    # 4. Calculate key metrics
    metrics = {
        "Total Customers": len(customers_df),
        "Total Products": len(products_df),
        "Total Transactions": len(transactions_df),
        "Total Revenue": transactions_df["TotalValue"].sum(),
        "Average Transaction Value": transactions_df["TotalValue"].mean(),
        "Most Common Region": customers_df["Region"].mode()[0],
        "Most Popular Category": products_df["Category"].mode()[0],
    }

    return pd.Series(metrics)


# Task 2: Lookalike Model
def create_customer_features(customers_df, transactions_df, products_df):
    # Merge transactions with products to get category information
    trans_prod = transactions_df.merge(products_df, on="ProductID")

    # Calculate customer-level features
    customer_features = pd.DataFrame()
    customer_features["CustomerID"] = customers_df["CustomerID"]

    # Transaction patterns
    transaction_stats = (
        transactions_df.groupby("CustomerID")
        .agg({"TotalValue": ["sum", "mean", "count"], "Quantity": ["sum", "mean"]})
        .reset_index()
    )
    transaction_stats.columns = [
        "CustomerID",
        "total_spend",
        "avg_transaction_value",
        "transaction_count",
        "total_quantity",
        "avg_quantity",
    ]

    # Category preferences
    category_pivot = pd.crosstab(trans_prod["CustomerID"], trans_prod["Category"])
    category_pivot = category_pivot.div(category_pivot.sum(axis=1), axis=0)

    # Combine all features
    customer_features = customer_features.merge(transaction_stats, on="CustomerID")
    customer_features = customer_features.merge(
        category_pivot, left_on="CustomerID", right_index=True, how="left"
    )

    # Fill NaN values
    customer_features = customer_features.fillna(0)

    return customer_features


def find_lookalikes(customer_features, customer_id, n_recommendations=3):
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(customer_features.drop("CustomerID", axis=1))

    # Calculate similarity scores
    similarity_matrix = cosine_similarity(features_scaled)

    # Get index of target customer
    customer_idx = customer_features[
        customer_features["CustomerID"] == customer_id
    ].index[0]

    # Get similarity scores for target customer
    customer_similarities = similarity_matrix[customer_idx]

    # Get indices of top similar customers (excluding self)
    similar_indices = np.argsort(customer_similarities)[::-1][1 : n_recommendations + 1]

    # Get customer IDs and similarity scores
    similar_customers = customer_features.iloc[similar_indices]["CustomerID"].values
    similarity_scores = customer_similarities[similar_indices]

    return list(zip(similar_customers, similarity_scores))


# Task 3: Customer Segmentation
def perform_clustering(customer_features, n_clusters=5):
    # Prepare features for clustering
    features_for_clustering = customer_features.drop("CustomerID", axis=1)

    # Scale features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features_for_clustering)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(features_scaled)

    # Calculate Davies-Bouldin Index
    db_index = davies_bouldin_score(features_scaled, clusters)

    # Add cluster labels to customer features
    customer_features["Cluster"] = clusters

    # Visualize clusters using PCA
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    features_pca = pca.fit_transform(features_scaled)

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(
        features_pca[:, 0], features_pca[:, 1], c=clusters, cmap="viridis"
    )
    plt.title("Customer Segments Visualization (PCA)")
    plt.colorbar(scatter)
    plt.savefig("cluster_visualization.png")
    plt.close()

    return customer_features, db_index
