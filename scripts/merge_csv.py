import pandas as pd
import os

# Define a function that will merge all csv files in a given dir
def merge_csv(dir):
    all_dfs = []
    # Traverse all subfolders
    for root, dirs, files in os.walk(dir):
        # Ignore files in the actual root dir, only look in subfolders
        if root == dir:
            continue
        for file in files:
            # Only look for csv files
            if file.endswith('.csv'):
                path = os.path.join(root, file)
                df = pd.read_csv(path)
                # Drop all empty columns before merging
                df.dropna(axis=1, how='all',inplace=True)
                # Add the filename as a variable
                df['Variable'] = os.path.splitext(file)[0]
                all_dfs.append(df)
    # Return all concatenated data frames without repeating the header row
    return pd.concat(all_dfs,ignore_index=True)

# Run the function and merge the dfs
directory = os.path.join('pr2_32','results')
merged_df = merge_csv(directory)

# Save the merged dataframe to a new CSV file
merged_df.to_csv(os.path.join(directory,'merged_data.csv'),index=False)