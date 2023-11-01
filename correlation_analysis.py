
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlation_analysis(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)

    # Correlation heatmap
    plt.figure(figsize=(10, 7))
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    plt.show()

# Uncomment the line below to run the analysis with your data path
# correlation_analysis('path_to_your_data.csv')
