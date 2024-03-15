import argparse
import pandas as pd
import subprocess
import logging
from model import perform_kmeans  
from vis import generate_visualization  

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        logging.error("File not found at %s", file_path)
        return None
    except Exception as e:
        logging.error("Error loading dataset: %s", e)
        return None

def preprocess_data(file_path):
    try:
        
        subprocess.run(["python3", "dpre.py", file_path])
        logging.info("Dataset transferred to dpre.py successfully.")
    except Exception as e:
        logging.error("Error while transferring dataset to dpre.py: %s", e)

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    parser = argparse.ArgumentParser(description="Load dataset from a file and transfer to dpre.py for preprocessing")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")
    args = parser.parse_args()

    dataset = load_dataset(args.file_path)
    if dataset is not None:
        logging.info("Dataset loaded successfully:")
        print(dataset.head())
        preprocess_data(args.file_path)

        perform_kmeans(dataset)  

        generate_visualization(dataset)  
        print("Visualization created and saved as vis.png")  

if __name__ == "__main__":
    main()
