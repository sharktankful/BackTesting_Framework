import pandas as pd

# Downloads dataframe to CSV file
def download_csv(df: pd.DataFrame, title: str):
    df.to_csv(f'data/{title}.csv')



'''
if __name__ == "__main__":
    clean_csv()   
'''


    
