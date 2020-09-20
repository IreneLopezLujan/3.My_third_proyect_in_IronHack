
import os
from dotenv import load_dotenv
import json
import requests
import pandas as pd
import re




def filter_dataset(x,y):
    """
    Filters the dataset with the colors and dishes
    """
    result = pd.read_csv("Data/dataset_final.csv",index_col=0)
    filtered = result[(result["Colors"].str.contains(f"{x}",regex=True,flags= re.IGNORECASE)) & (result["dishes"].str.contains(f"{y}",regex=True,flags= re.IGNORECASE))].sort_values(by="Colors",ascending=False).head(1)
    return filtered


def search(city):  
    apiKey = os.getenv("apikey")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url + 'query=' +'Tienda de vinos '+city +'&key=' + apiKey) 
    x = r.json() 
    y = x['results'] 
    
    return [y[i]['name'] for i in range(len(y))]

