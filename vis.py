import matplotlib.pyplot as plt
import pandas as pd

def generate_visualization(df):
    df['Fertility Rate'] = pd.to_numeric(df['Fertility Rate'], errors='coerce')
    df['Maternal Mortality Rate (per 100,000 live births)'] = pd.to_numeric(df['Maternal Mortality Rate (per 100,000 live births)'], errors='coerce')
    df = df.dropna(subset=['Fertility Rate', 'Maternal Mortality Rate (per 100,000 live births)'])

    column1 = 'Fertility Rate'
    column2 = 'Maternal Mortality Rate (per 100,000 live births)'

    plt.figure(figsize=(10, 6))
    plt.scatter(df[column1], df[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title('Scatter Plot of Fertility Rate vs Maternal Mortality Rate')
    plt.grid(True)
    plt.savefig('vis.png')  
    plt.show()

df = pd.read_csv('res_dpre.csv')

generate_visualization(df)
