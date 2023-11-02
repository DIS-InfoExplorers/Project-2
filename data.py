import os
import numpy as np
import pandas as pd

import torch
from torch.utils.data import TensorDataset
from torchvision.datasets.utils import download_and_extract_archive

class RatingsData(TensorDataset):
    # Define the filename for the CSV file containing ratings data
    zip_filename = 'train_ratings.csv'
    
    def __init__(self, root, train=True):
        # Define the number of users and items in the dataset
        self.n_users = 943
        self.n_items = 1682
        
        filename = 'train_ratings.csv'

        # Read the CSV file containing ratings data into a DataFrame
        df = pd.read_csv(filename)
        
        if train:
            # If the dataset is for training, use the entire DataFrame
            df = df
        else:
            # If the dataset is for testing, use a portion (2/3 of the DataFrame)
            df = df.iloc[int(len(df) * 2 / 3):]

        # Mapping for movie ids based on movies.csv dataset
        sorted_unique_ids = sorted(pd.read_csv('movies.csv')['movieId'].unique())
        id_to_index_mapping = {id: idx for idx, id in enumerate(sorted_unique_ids)}
        # Replace values in the 'movieId' column with the corresponding indices
        df['movieId'] = df['movieId'].map(id_to_index_mapping)

        # Mapping for user ids
        sorted_unique_ids = sorted(df['userId'].unique())
        id_to_index_mapping = {id: idx for idx, id in enumerate(sorted_unique_ids)}
        # Replace values in the 'userId' column with the corresponding indices
        df['userId'] = df['userId'].map(id_to_index_mapping)
        
        # Convert user ids, item ids, and ratings to PyTorch tensors
        user_ids = torch.LongTensor(df.userId.values)
        item_ids = torch.LongTensor(df.movieId.values)
        ratings = torch.Tensor(df.rating.values)

        super(RatingsData, self).__init__(user_ids, item_ids, ratings)
