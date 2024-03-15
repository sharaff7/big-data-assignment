import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer, StandardScaler
import subprocess

df = pd.read_csv("Israel-Palestine.csv")

df = df.dropna(subset=['Active Military Personnel',
                       'Reserve Military Personnel',
                       'Literacy Rate (%)',
                       'IT Output (in USD)',
                       'Number of Tanks',
                       'Number of Submarines',
                       'Number of Armoured Vehicles'])

df['GDP (in USD)'] = df['GDP (in USD)'].str.replace(' billion', '').str.replace(',', '').astype(float)
df['Population'] = df['Population'].str.replace(',', '').astype(int)
df['Active Military Personnel'] = df['Active Military Personnel'].str.replace(',', '').astype(int)
df['Reserve Military Personnel'] = df['Reserve Military Personnel'].str.replace(',', '').astype(int)
df['Number of Tanks'] = df['Number of Tanks'].str.replace(',', '').astype(int)
df['Number of Armoured Vehicles'] = df['Number of Armoured Vehicles'].str.replace(',', '').astype(int)
df['Agricultural Output (in USD)'] = df['Agricultural Output (in USD)'].apply(lambda x: float(x.replace(' billion', '').replace(',', '')) * 1e9 if ' billion' in x else float(x.replace(' million', '').replace(',', '')) * 1e6 if ' million' in x else float(x.replace(',', '')))
df['IT Output (in USD)'] = df['IT Output (in USD)'].str.replace(' billion', '').str.replace(',', '').astype(float)

def data_reduction(df):
    return df

def data_discretization(df):
    discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform', subsample=None)  
    df_discretized = df.copy()  
    df_discretized['GDP (in USD)'] = discretizer.fit_transform(df[['GDP (in USD)']])  
    return df_discretized

def data_normalization(df):
    scaler = StandardScaler()
    numeric_columns = ['GDP (in USD)']  # Assuming only GDP (in USD) is to be normalized
    df_normalized = df.copy()  
    df_normalized[numeric_columns] = scaler.fit_transform(df_normalized[numeric_columns])
    return df_normalized

df = data_reduction(df)
df = data_discretization(df)
df = data_normalization(df)

df.to_csv("res_dpre.csv", index=False)

print("Data preprocessing completed. Result saved as res_dpre.csv")

try:
    subprocess.run(["python3", "eda.py", "res_dpre.csv"], check=True)
    print("Exploratory Data Analysis completed.")
except subprocess.CalledProcessError as e:
    print("Error executing EDA script:", e)
