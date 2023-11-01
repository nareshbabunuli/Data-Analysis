
import pandas as pd
import matplotlib.pyplot as plt

def sales_over_time_analysis(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    data['order_date'] = pd.to_datetime(data['order_date'])

    # Group data by order date and sum the quantity and revenue
    daily_sales_data = data.groupby(data['order_date'].dt.date).agg({'quantity': 'sum', 'revenue': 'sum'})

    plt.figure(figsize=(14, 6))

    # Plotting quantity sold over time
    ax1 = daily_sales_data['quantity'].plot(color='blue', grid=True, label='Quantity Sold')
    ax2 = daily_sales_data['revenue'].plot(color='red', grid=True, secondary_y=True, label='Total Revenue')

    ax1.set_ylabel('Quantity Sold', color='blue')
    ax2.set_ylabel('Total Revenue', color='red')
    ax1.set_xlabel('Date')
    ax1.set_title('Sales Over Time')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.show()

# Uncomment the line below to run the analysis with your data path
# sales_over_time_analysis('path_to_your_data.csv')
