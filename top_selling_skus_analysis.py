
import pandas as pd
import matplotlib.pyplot as plt

def top_selling_skus_analysis(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)

    # Group data by SKU and sum the quantity and revenue
    sku_sales_data = data.groupby('sku').agg({'quantity': 'sum', 'revenue': 'sum'}).sort_values(by='quantity', ascending=False).head(10)

    # Plotting top selling SKUs
    plt.figure(figsize=(14, 6))
    sku_sales_data['quantity'].plot(kind='bar', color='skyblue', label='Quantity Sold')
    plt.title('Top 10 Selling SKUs')
    plt.xlabel('SKU')
    plt.ylabel('Quantity Sold')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

# Uncomment the line below to run the analysis with your data path
# top_selling_skus_analysis('path_to_your_data.csv')
