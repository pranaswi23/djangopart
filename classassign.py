import glob
#import os
import pandas as pd
#import librosa
import numpy as np

# chunk_index = []
age_list= []
file_list = []

data = pd.read_csv('C:\\SPIRE Internship 2020\\Dataset-valid-dev\\age_features1.csv')
df = data.values

# print(df)
# print(df.shape[0])
for i in range(df.shape[0]):
    if df[i,-1] == 'teens':
        df[i,-1] = 0
    elif df[i,-1] == 'twenties':
        df[i,-1] = 1
    elif df[i,-1] == 'thirties':
        df[i,-1] = 2
    elif df[i,-1] == 'fourties':
        df[i,-1] = 3
    elif df[i,-1] == 'fifties':
        df[i,-1] = 4
    elif df[i,-1] == 'sixties':
        df[i,-1] = 5
    elif df[i,-1] == 'seventies':
        df[i,-1] = 6
    elif df[i,-1] == 'eighties':
        df[i,-1] = 7

X = df[0:,0]
file_main = []
for i in range(X.shape[0]):
    file_main.append(int(X[i][-10:-4]))

# print(file_main)


for audio_path in glob.glob("C:\\SPIRE Internship 2020\\Dataset-valid-dev\\chunks_cv_valid_dev\\*.wav"):
    string = str(audio_path)
    a = string.find('m')
    file_num = int(string[a+7:a+11])
    # print(file_num)
    # chunk_num =  int(string[a+12])
    for i in range(X.shape[0]):
        if file_main[i] == file_num:
            age = df[i,-1]
    print('working1...')
    # print(age)
# '''
    file_list.append(audio_path) # make an ID list
    # chunk_index.append(chunk_num)
    age_list.append(age)

    # print(age_list)
    
print('working2...')

df = pd.DataFrame(np.column_stack([file_list, age_list]),columns=['voiceID','age'])

print('done...')

df.to_csv("C:\\SPIRE Internship 2020\\Dataset-valid-dev\\assignlabel.csv", index=False)

# '''
