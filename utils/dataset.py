import os
import pandas as pd

class Dataset():
    
    def __init__(self, path):
        self.path = path
        
    def test_data(self):
        _path = os.path.join(self.path, 'test_data.ftr')
        return pd.read_feather(_path)
    
    def train_data(self):
        _path = os.path.join(self.path, 'train_data.ftr')
        return pd.read_feather(_path)