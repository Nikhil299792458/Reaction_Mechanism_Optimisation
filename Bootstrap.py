# -*- coding: utf-8 -*-
"""
Author: Nikhil Verma
Code:
Bootstrap Analsis
"""

import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import glob
import numpy as np


# Change the Directory Name
excel_files = glob.glob(r'C:\Users\Nikhil Verma\Downloads\LR_0.0001\LR_0.0001\*.xlsx')


# Function to read an Excel file
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df


# T: Array containing maximum fitness from all the files. 
T=[]

# Read data from the excel file using multithredding using Max_Workers

if __name__ == '__main__':
    # List of Excel file paths to read
    # Create a thread pool with 3 threads
    with ThreadPoolExecutor(max_workers=20) as executor:
        # Submit each Excel file to a thread in the pool
        future_to_file = {executor.submit(read_excel, file): file for file in excel_files}
        for future in future_to_file:
            file = future_to_file[future]
        
            # Retrieve the Excel file result from the future
            result = future.result()
            T.append(result.loc[:,"fitness"][999])
                
           
T=np.array(T)

r=np.shape(T)[0]

# N: Number of Samples
N=1000

# Cutoff criteria
Cutoff=0.4

# Find number of files to be read
R=int(r*Cutoff)

Median=[]
for i in range(N):
    
    # Random number of files index, from 20 files
    A=np.random.choice(np.arange(r), size=R, replace=False)
    
    # Contains data from different files. 
    Data=[]
    
    for j in A:
        Data.append(T[j])
        
    # Calculate median based on Data 
    Median.append(np.median(Data))

# Calcualte standard deviation based on Median
Error=np.std(Median)





        
    
    
        
        


