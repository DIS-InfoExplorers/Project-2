import os
import numpy as np
import pandas as pd

import torch
from torch.utils.data import TensorDataset
from torchvision.datasets.utils import download_and_extract_archive


class RatingsData(TensorDataset):
    zip_filename = 'train_ratings.csv'
    
    def __init__(self, root, train=True):

        self.n_users = 943
        self.n_items = 1682

        
        filename = 'train_ratings.csv'

        df = pd.read_csv(filename)
        
        if train:
            df = df
        else:
            df = df.iloc[int(len(df)*2/3):]

        sorted_unique_ids = sorted(pd.read_csv('movies.csv')['movieId'].unique())

        # Step 2: Create a mapping of IDs to indices based on the sorted order
        id_to_index_mapping = {id: idx for idx, id in enumerate(sorted_unique_ids)}

        # Step 3: Replace values in column A with the corresponding indices
        df['movieId'] = df['movieId'].map(id_to_index_mapping)

        sorted_unique_ids = sorted(df['userId'].unique())

        # Step 2: Create a mapping of IDs to indices based on the sorted order
        id_to_index_mapping = {id: idx for idx, id in enumerate(sorted_unique_ids)}
        df['userId'] = df['userId'].map(id_to_index_mapping)
        user_ids = torch.LongTensor(df.userId.values)
        item_ids = torch.LongTensor(df.movieId.values)
        ratings = torch.Tensor(df.rating.values)

        super(RatingsData, self).__init__(user_ids, item_ids, ratings)
    



    