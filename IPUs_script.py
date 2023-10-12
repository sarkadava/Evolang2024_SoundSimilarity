
# curfolder
import os
curfolder = os.getcwd()
IPU_anno = curfolder + '\\structure.csv'

# load the data
import pandas as pd
IPU_data = pd.read_csv(IPU_anno, sep = ',')
IPU_data

# make column IPU
IPU_data['IPUs'] = None

# take a look into column structure and count have many 's' strings are there separated by 'p' in first row
IPU_data['structure'][0].count('s')
IPU_data['structure'][2].count('s')

# add order number to each s in the string
IPU_data['structure'][0].replace('s', 's1')


IPU_try = IPU_data
# do it for every row, while the number for a row starts at 1 and continuously grow to the last s in the string within that row
for i in range(len(IPU_try)):
    for j in range(1, IPU_try['structure'][i].count('s')):
        if j == 
IPU_try.head()


import pandas as pd

# Sample DataFrame with the 'string' column
data = {'string': ['ssssps', 'spspsps']}
df = pd.DataFrame(data)

# Define a function to number 's' characters
def number_s(s):
    s_count = 0
    result = []
    for char in s:
        if char == 's':
            s_count += 1
            result.append(f's{s_count}')
        else:
            result.append(char)

    return ''.join(result)

# apply on column
IPU_try['IPUs'] = IPU_try['structure'].apply(number_s)
IPU_try

# for each s 


# Create an empty DataFrame with the 'file' column
new_df = pd.DataFrame(columns=['file', 'split_string'])

# Function to split the numbered string by 'p' and add to new_df
def split_and_add(row):
    file = row['file']
    numbered_string = row['IPUs']
    split_strings = numbered_string.split('p')
    
    for s in split_strings:
        new_df.loc[len(new_df)] = [file, s]

# Apply the function to each row in the original DataFrame
IPU_try.apply(split_and_add, axis=1)

# show me 10 rows of new_df
new_df.head(10)
IPU_try

# now create a column 'IPU_count
new_df['IPU_count'] = None

# group by file and add a value for IPU_count, such that it starts from 1 and counts +1
for file in new_df['file'].unique():
    new_df.loc[new_df['file'] == file, 'IPU_count'] = range(1, len(new_df.loc[new_df['file'] == file]) + 1)

# add string IPU_ to the IPU_count in each row, where the number follows
new_df['IPU_count'] = 'IPU_' + new_df['IPU_count'].astype(str)

new_df.head(10)

# Create an empty DataFrame to store the split segments
IPU_data = pd.DataFrame(columns=['file', 'split_string', 'IPU_count'])

# Function to split the 'split_string' and create new rows
def split_segments(row):
    file = row['file']
    ipu_count = row['IPU_count']
    segments = row['split_string'].split('s')
    
    for segment in segments:
        if segment:  # Skip empty segments
            IPU_data.loc[len(IPU_data)] = [file, segment, ipu_count]

# Apply the function to each row in the original DataFrame
new_df.apply(split_segments, axis=1)

# Display the resulting DataFrame with split segments
IPU_data.head(20)

# add string IPU_ to the IPU_count in each row, where the number follows
IPU_data['split_string'] = 's' + IPU_data['split_string'].astype(str)

# make a column ID
IPU_data['ID'] = None

# from file, take the first to string separated by _ and ad a split_string to it, and save it to ID, again separated by _
for i in range(len(IPU_data)):
    IPU_data['ID'][i] = IPU_data['file'][i].split('_')[0] + '_' + IPU_data['file'][i].split('_')[1] + '_' + IPU_data['split_string'][i]

IPU_data

IPU_data['ID_IPU'] = None
for i in range(len(IPU_data)):
    IPU_data['ID_IPU'][i] = IPU_data['file'][i].split('_')[0] + '_' + IPU_data['file'][i].split('_')[1] + '_' + IPU_data['IPU_count'][i]


# save this to a csv file
IPU_data.to_csv('IPU_data.csv', sep = ',', index = False)