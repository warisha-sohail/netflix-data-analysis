import pandas as pd
import os

def load_data(filepath):
    #Loads the netflix dataset from a specified path
    if not os.path.exists(filepath):
        raise FileNotFoundError("Dataset not found at: {filepath}")
    return pd.read_csv(filepath)

def clean_data(df):
    #Cleans null values, parses dates, and extracts numeric durations
    df = df.copy()

    #Handle structural missing values across columns
    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('UR') #Unrated
    df['description'] = df['description'].fillna('')

    #Drop rows missing critical timeline data
    df = df.dropna(subset=['date_added', 'duration'])

    #Standardize 'date_added' and extract calendar year
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
    df['year_added'] = df['date_added'].dt.year.astype('Int64')

    #Duration Analysis: Extract numeric values (e.g., '90 min --> 90')
    df['diration_numeric'] = df['duration'].str.extract(r'(\d+)').astype(float)
    df['duration_unit'] = df['duration'].str.extract('([a-zA-Z]+)')

    return df

def explode_column(df, column_name):
    #Splits comma-operated strings (like listed_in or country) into distinct rows
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].str.split(', ')
    return df_copy.explode(column_name)

if __name__ == "__main__":
    #Pipline execution tracking
    raw_data_path = 'data/netflix_titles.csv'
    output_clean_path = 'data/cleaned_netflix_titles.csv'

    print("Starting Data Pipeline...")
    raw_df = load_data(raw_data_path)
    cleaned_df = clean_data(raw_df)

    #Save primaary clean dataset
    cleaned_df.to_csv(output_clean_path, index=False)
    print(f"Data pipeline complete. Cleaned file saved to {output_clean_path}")


