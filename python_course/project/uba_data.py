
from urllib.request import urlretrieve, urlopen
import csv
import pandas as pd
from six.moves import urllib
import os


DOWNLOAD_ROOT = 'https://www.umweltbundesamt.de/uaq/csv/stations/data?'
DATA_PATH = 'data'
station = 'station[]=' + 'DEBW118'
pollutant = '&pollutant[]=' + 'NO2'
scope = '&scope[]=' + '1SMW'
group = '&group[]=' + 'pollutant'
range = '&range[]=' + '1538690408' + ',' + '1539640748'
DATA_URL = DOWNLOAD_ROOT + station + pollutant + scope + group + range


# link = 'https://www.umweltbundesamt.de/uaq/csv/stations/data?station[]=DEBW118&pollutant[]=NO2&scope[]=1SMW&group[]=pollutant&range[]=1538690408,1539640748'


def fetch_airq_data(data_url=DATA_URL, data_path=DATA_PATH):
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    csv_path = os.path.join(data_path, 'airq_data.csv')
    urlretrieve(data_url, csv_path)
    raw_data = open(csv_path)
    print(raw_data)
    return

fetch_airq_data()


def load_airq_data(data_path=DATA_PATH):
    csv_path = os.path.join(data_path, 'airq_data.csv')
    # with open(csv_path, 'rb') as f:
        # lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
    pandas_data = pd.read_csv(csv_path, error_bad_lines=False)

    return pandas_data

airq = load_airq_data()
airq.head()


# raw_data = response.read().decode("utf-8")

# with open(raw_data, 'rb') as f:
#    data_import = pd.read_csv(f)


# csv_data = pd.read_csv(new_raw_data)
# print(csv_data.head())


# data_import = pandas.read_csv(raw_data)

# print(data_import)