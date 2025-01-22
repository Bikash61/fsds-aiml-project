from src.DimondPricePrediction.components.data_ingestion import DataIngestion
import pandas as pd
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception


obj = DataIngestion()
obj.initiate_data_ingestion()