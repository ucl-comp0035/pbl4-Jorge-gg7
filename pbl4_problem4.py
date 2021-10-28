# Problem 4: Identify and address any missing values
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_raw.csv')
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)

    # 1. Find and count the number of missing values e.g., Null `isnull().sum().sum()` or NaN `isna().sum().sum()`
    # and print the result
    print(df.isna().sum().sum())
    # 2. Create a dataframe with the rows that contain missing values and print it
    print(df[df.isna().any(axis=1)])
    # 3. Drop rows where there is a na in the Participants M or F columns
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    print(df.isna().sum().sum())
    # 4. Replace the NaN in Type column with 'Winter'
    df.fillna({'Type': 'Winter'}, inplace=True)
    print(df.isna().sum().sum())