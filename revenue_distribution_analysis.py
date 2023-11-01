
import pandas as pd
import matplotlib.pyplot as plt

def revenue_distribution_analysis(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)

    # Revenue distribution by color
    color_revenue_data = data.groupby('color').agg({'revenue': 'sum'}).sort_values(by='revenue', ascending=False).head(10)
    
    # Revenue distribution by size
    size_revenue_data = data.groupby('size').agg({'revenue': 'sum'}).sort_values(by='revenue', ascending=False)

    # Plotting revenue by color
    plt.figure(figsize=(14, 6))
    color_revenue_data['revenue'].plot(kind='bar', color='lightcoral', label='Total Revenue')
    plt.title('Top 10 Revenue Generating Colors')
    plt.xlabel('Color')
    plt.ylabel('Total Revenue')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

    # Plotting revenue by size
    plt.figure(figsize=(14, 6))
    size_revenue_data['revenue'].plot(kind='bar', color='lightgreen', label='Total Revenue')
    plt.title('Revenue Distribution by Size')
    plt.xlabel('Size')
    plt.ylabel('Total Revenue')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

# Uncomment the line below to run the analysis with your data path
# revenue_distribution_analysis('path_to_your_data.csv')
