' This module imports IR .dpt files'
import os
import glob
import numpy as np
import pandas as pd
from tqdm import tqdm

pattern = input('Enter the file path and the extensions:...')
final_filename = input('Enter dataset file name:...')

file_list = [os.path.basename(x) for x in glob.glob(pattern)]
filepath = glob.glob(pattern)

# read the first element of the list to extract wavenumbers (wavelength range)
data_file = np.loadtxt(filepath[1], delimiter='\t')
w = data_file[:, 0]  # wavenumbers (wavelength range)

print("Loading files...")
dfList = []
for filename in tqdm(filepath):
#print(filename)
    df = pd.read_csv(filename, header=None, delimiter='\t', usecols=[1])
    dfList.append(df)
concatanedDf = pd.concat(dfList, axis=1)
print('Creating dataframe...')
# Extract the species and age from the name's files
species_list = []    # species
age_list = []        # age
id_list = []         # mosquito ID
mozziepart = []     # mosquito part
mozziespec = []     # mosquito specific part
for filename in file_list:
    sp = filename[4:6]
    ag = filename[7:10]
    idn = filename[0:3]
    mp = filename[11:13]
    ms = filename[14:16]
    species_list.append(sp)
    age_list.append(ag)
    id_list.append(idn)
    mozziepart.append(mp)
    mozziespec.append(ms)

# build the data frame for Orange or Machine learning uses

w_round = np.ceil(w).astype(int) # round wavenumbers
index_df = concatanedDf.set_index(w_round)
trans_df = index_df.T

# Add columns of species, age, id, part and specific part
trans_df['Species'] = species_list
trans_df['Age'] = age_list
trans_df['ID'] = id_list
trans_df['Part'] = mozziepart
trans_df['Sp Part'] = mozziespec


# Export data frame to work in Orange or whatever

export_csv = trans_df.to_csv('/Users/mauro/Documents/Data Visualization/Data_viz/NIRS/Datasets/%s.csv'%final_filename,index=False) 
