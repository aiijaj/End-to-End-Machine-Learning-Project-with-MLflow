import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig  # This is a dataclass or config holder
from mlProject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        os.makedirs(self.config.root_dir, exist_ok=True)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(" Splitted data into training and test sets.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print(train.shape)
        print(test.shape)
