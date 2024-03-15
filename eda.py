import pandas as pd
import sys

def generate_insights(df):
    insights = []

    numeric_df = df.select_dtypes(include=['number'])

    summary_stats = numeric_df.describe()
    insights.append("Insight 1: Summary statistics\n")
    insights.append(summary_stats.to_string())

    unique_values = numeric_df.nunique()
    insights.append("\nInsight 2: Unique values\n")
    insights.append(unique_values.to_string())

    correlation_matrix = numeric_df.corr()
    insights.append("\nInsight 3: Correlation matrix\n")
    insights.append(correlation_matrix.to_string())

    return insights

def save_insights(insights):
    for i, insight in enumerate(insights, start=1):
        filename = f"eda-in-{i}.txt"
        with open(filename, "w") as f:
            f.write(insight)

def main():
    if len(sys.argv) < 2:
        print("Error: No file path provided.")
        print("Usage: python3 eda.py <file_path>")
        return

    file_path = sys.argv[1]

    try:
        df = pd.read_csv(file_path)

        insights = generate_insights(df)

        save_insights(insights)
        print("Exploratory Data Analysis completed. Insights saved as text files.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
