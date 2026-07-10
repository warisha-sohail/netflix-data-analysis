import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_data, clean_data, explode_column

def generate_plots():
    #Load and clean data stream
    df = clean_data(load_data('data/netflix_titles.csv'))
    sns.set_theme(style="darkgrid")

    #1. Most Common Genre
    plt.figure(figsize=(10, 5))
    genres_df = explode_column(df, 'listed_in')
    top_genres = genres_df['listed_in'].value_counts().head(10)
    sns.barplot(x=top_genres.values, y=top_genres.index, hue=top_genres.index, palette='magma', legend=False)
    plt.title('Top 10 COntent Genres on Netflix')
    plt.xlabel('Count')
    plt.tight_layout()
    plt.savefig('data/01_most_common_genres.png')
    plt.close()

    #2. Release Trends Over Time
    plt.figure(figsize=(10, 5))
    recent_content = df[df['release_year'] >= 2000]
    sns.histplot(data=recent_content, x='release_year', hue='type', multiple='stack', bins=25, palette='muted')
    plt.title('Content Release Trends (Since 2000)')
    plt.xlabel('Release Year')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('data/02_release_trends.png')
    plt.close()

    #3. Content Distribution by Rating
    plt.figure(figsize=(10, 5))
    rating_counts = df['rating'].value_counts().head(10)
    sns.barplot(x=rating_counts.index, y=rating_counts.values, hue=rating_counts.index, palette='viridis', legend=False)
    plt.title('Content Volume Across Top 10 Ratings Labels')
    plt.xlabel('Rating Category')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('data/03_ratings_distribution.png')
    plt.close()

    #4. Duration Distribution for Movies
    plt.figure(figsize=(10, 5))
    movies_df = df[df['type'] == 'Movie']
    sns.kdeplot(data=movies_df, x='duration_numeric', fill=True, color='crimson')
    plt.title('Movie Runtime Distribution Analysis')
    plt.xlabel('Duration (Minutes)')
    plt.ylabel('Density')
    plt.tight_layout()
    plt.savefig('data/04_movie_duration_analysis.png')
    plt.close()

if __name__ == "__main__":
    print("Generating statistical seaborn plots...")
    generate_plots()
    print("All plots saved directly to the /data directory!")


