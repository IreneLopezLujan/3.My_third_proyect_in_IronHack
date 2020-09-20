import pandas as pd
from pandas import Series
import numpy as np
import re
import os



def transf2(row):
    return row['category_food'] if row['check'] ==True else 'unmatch'

def transf3(row):
    return row['wine_name'] if row['check'] ==True else 'unmatch'