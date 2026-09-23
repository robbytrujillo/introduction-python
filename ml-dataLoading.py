# dataLoading
# from google.colab import files
import pandas as pd

# uploaded = files.upload()

# Langsung baca file test.csv
test = pd.read_csv("content/test.csv")
test.head()