# Category B Jokes

This repo contains a Jupyter Notebook showing how to cluster  posts in VK group ["Category B Jokes"](https://vk.com/baneks) (рус. "Анекдоты категории Б") using agglomerative clustering, snowball stemmer and TF-IDF vectorizer.

## Project structure

    .
    ├── clustered_posts.csv        # Posts with cluster tags
    ├── clustering.ipynb           # Main jupyter notebook file
    ├── download.py                # Script to download posts
    ├── posts.csv                  # Downloaded posts
    ├── .gitignore                 # Git ignore source file
    └── README.md

## To do
1. TSNE or PCA
2. Visualization of clusters