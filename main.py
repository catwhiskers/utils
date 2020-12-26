from dataframe.df import reduce_mem_usage
import pandas as pd


df = pd.read_csv('./data/abalone_csv.csv')

reduce_mem_usage(df)