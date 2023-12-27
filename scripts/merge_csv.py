import pandas as pd
import os

# Define a function that will merge all csv files in a given dir
def merge_csv(dir):
    all_dfs = []
    # Traverse all subfolders
    for root, dirs, files in os.walk(dir):
        for file in files:
            # Only look for csv files
            if file.endswith('.csv'):
                path = os.path.join(root, file)
                df = pd.read_csv(path)
                # Drop all empty columns before merging
                df.dropna(axis=1, how='all', inplace=True)
                # Add the filename as a variable
                df['Variable'] = os.path.splitext(file)[0]
                all_dfs.append(df)
    # Return all concatenated data frames without repeating the header row
    return pd.concat(all_dfs, ignore_index=True)

# Save the path of pr2_32 so that the script works on all machines
pr2_32 = os.path.join(os.path.dirname(__file__),'..')

# Run the function and merge the dfs
merged_df = merge_csv(os.path.join(pr2_32,'data'))

# Save the merged dataframe to a new CSV file
merged_df.to_csv(os.path.join(pr2_32,'results','merged_data.csv'), index=False)