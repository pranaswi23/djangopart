
# importing modules and packages

import librosa as lr
import parselmouth
from parselmouth.praat import call
# wildmark imports everything from a module

import glob
import numpy as np
import pandas as pd

def measurePitch(voiceID, f0min, f0max, unit):
    sound = parselmouth.Sound(voiceID) # read the sound
    duration = call(sound, "Get total duration") # duration
    pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    meanF0 = call(pitch, "Get mean", 0, 0, unit) # get mean pitch
    stdevF0 = call(pitch, "Get standard deviation", 0 ,0, unit) # get standard deviation

    return duration, meanF0, stdevF0

#calculating MFCCs (frame duration = 1 sec (16000) per frame)
def measureMFCC(x, sr):
    mfcc_f= lr.feature.mfcc(x, sr=sr, n_mfcc = 12, n_fft = 16000, hop_length = 16000, dct_type=2, norm='ortho', htk = True)

    return mfcc_f

# create lists to put the results
file_list = []
duration_list = []
mean_F0_list = []
sd_F0_list = []


#to store MFCCs for first 4 seconds of the signal (i.e. 4 frames of duration 1 sec = 4*12 = 48 features per audio file)
mfcc1_list = []
mfcc2_list = []
mfcc3_list = []
mfcc4_list = []
mfcc5_list = []
mfcc6_list = []
mfcc7_list = []
mfcc8_list = []
mfcc9_list = []
mfcc10_list = []
mfcc11_list = []
mfcc12_list = []
mfcc13_list = []
mfcc14_list = []
mfcc15_list = []
mfcc16_list = []
mfcc17_list = []
mfcc18_list = []
mfcc19_list = []
mfcc20_list = []
mfcc21_list = []
mfcc22_list = []
mfcc23_list = []
mfcc24_list = []
mfcc25_list = []
mfcc26_list = []
mfcc27_list = []
mfcc28_list = []
mfcc29_list = []
mfcc30_list = []
mfcc31_list = []
mfcc32_list = []
mfcc33_list = []
mfcc34_list = []
mfcc35_list = []
mfcc36_list = []
mfcc37_list = []
mfcc38_list = []
mfcc39_list = []
mfcc40_list = []
mfcc41_list = []
mfcc42_list = []
mfcc43_list = []
mfcc44_list = []
mfcc45_list = []
mfcc46_list = []
mfcc47_list = []
mfcc48_list = []

# data_dir = 'C:\\SPIRE Internship 2020\\Dataset-valid-dev\\upload_cv-valid-dev\\cv-valid-dev-clean'
# audio_path = glob(data_dir + '/*.mp3')
# print(len(audio_path))


# To load the audio files from the folder in system to the code environment and to measure acoustics
for audio_path in glob.glob("C:\\SPIRE Internship 2020\\Dataset-valid-dev\\upload_cv-valid-dev\\cv-valid-dev-clean\\*.mp3"):
    sound = parselmouth.Sound(audio_path)    # we open and read in the audio file
    (duration, meanF0, stdevF0) = measurePitch(sound, 75, 300, "Hertz")





    #loading file in librosa library
    x , sr = lr.load(audio_path, sr = 16000)

    mfccs = measureMFCC(x, sr)

    n, n_f = mfccs.shape
    if n_f == 2:
        mfcc25_list.append(0)
        mfcc26_list.append(0)
        mfcc27_list.append(0)
        mfcc28_list.append(0)
        mfcc29_list.append(0)
        mfcc30_list.append(0)
        mfcc31_list.append(0)
        mfcc32_list.append(0)
        mfcc33_list.append(0)
        mfcc34_list.append(0)
        mfcc35_list.append(0)
        mfcc36_list.append(0)
        mfcc37_list.append(0)
        mfcc38_list.append(0)
        mfcc39_list.append(0)
        mfcc40_list.append(0)
        mfcc41_list.append(0)
        mfcc42_list.append(0)
        mfcc43_list.append(0)
        mfcc44_list.append(0)
        mfcc45_list.append(0)
        mfcc46_list.append(0)
        mfcc47_list.append(0)
        mfcc48_list.append(0)
    elif n_f == 3:
        mfcc25_list.append(mfccs[0][2])
        mfcc26_list.append(mfccs[1][2])
        mfcc27_list.append(mfccs[2][2])
        mfcc28_list.append(mfccs[3][2])
        mfcc29_list.append(mfccs[4][2])
        mfcc30_list.append(mfccs[5][2])
        mfcc31_list.append(mfccs[6][2])
        mfcc32_list.append(mfccs[7][2])
        mfcc33_list.append(mfccs[8][2])
        mfcc34_list.append(mfccs[9][2])
        mfcc35_list.append(mfccs[10][2])
        mfcc36_list.append(mfccs[11][2])
        mfcc37_list.append(0)
        mfcc38_list.append(0)
        mfcc39_list.append(0)
        mfcc40_list.append(0)
        mfcc41_list.append(0)
        mfcc42_list.append(0)
        mfcc43_list.append(0)
        mfcc44_list.append(0)
        mfcc45_list.append(0)
        mfcc46_list.append(0)
        mfcc47_list.append(0)
        mfcc48_list.append(0)
    else:
        mfcc25_list.append(mfccs[0][2])
        mfcc26_list.append(mfccs[1][2])
        mfcc27_list.append(mfccs[2][2])
        mfcc28_list.append(mfccs[3][2])
        mfcc29_list.append(mfccs[4][2])
        mfcc30_list.append(mfccs[5][2])
        mfcc31_list.append(mfccs[6][2])
        mfcc32_list.append(mfccs[7][2])
        mfcc33_list.append(mfccs[8][2])
        mfcc34_list.append(mfccs[9][2])
        mfcc35_list.append(mfccs[10][2])
        mfcc36_list.append(mfccs[11][2])
        mfcc37_list.append(mfccs[0][3])
        mfcc38_list.append(mfccs[1][3])
        mfcc39_list.append(mfccs[2][3])
        mfcc40_list.append(mfccs[3][3])
        mfcc41_list.append(mfccs[4][3])
        mfcc42_list.append(mfccs[5][3])
        mfcc43_list.append(mfccs[6][3])
        mfcc44_list.append(mfccs[7][3])
        mfcc45_list.append(mfccs[8][3])
        mfcc46_list.append(mfccs[9][3])
        mfcc47_list.append(mfccs[10][3])
        mfcc48_list.append(mfccs[11][3])


    file_list.append(audio_path) # make an ID list
    duration_list.append(duration) # make duration list
    mean_F0_list.append(meanF0) # make a mean F0 list
    sd_F0_list.append(stdevF0) # make a sd F0 list


    #adding MFCCs to lists
    mfcc1_list.append(mfccs[0][0])
    mfcc2_list.append(mfccs[1][0])
    mfcc3_list.append(mfccs[2][0])
    mfcc4_list.append(mfccs[3][0])
    mfcc5_list.append(mfccs[4][0])
    mfcc6_list.append(mfccs[5][0])
    mfcc7_list.append(mfccs[6][0])
    mfcc8_list.append(mfccs[7][0])
    mfcc9_list.append(mfccs[8][0])
    mfcc10_list.append(mfccs[9][0])
    mfcc11_list.append(mfccs[10][0])
    mfcc12_list.append(mfccs[11][0])
    mfcc13_list.append(mfccs[0][1])
    mfcc14_list.append(mfccs[1][1])
    mfcc15_list.append(mfccs[2][1])
    mfcc16_list.append(mfccs[3][1])
    mfcc17_list.append(mfccs[4][1])
    mfcc18_list.append(mfccs[5][1])
    mfcc19_list.append(mfccs[6][1])
    mfcc20_list.append(mfccs[7][1])
    mfcc21_list.append(mfccs[8][1])
    mfcc22_list.append(mfccs[9][1])
    mfcc23_list.append(mfccs[10][1])
    mfcc24_list.append(mfccs[11][1])








# Add the data to Pandas
df = pd.DataFrame(np.column_stack([file_list, duration_list, mean_F0_list, sd_F0_list, mfcc1_list, mfcc2_list, mfcc3_list, mfcc4_list, mfcc5_list, mfcc6_list, mfcc7_list, mfcc8_list, mfcc9_list, mfcc10_list, mfcc11_list, mfcc12_list,
                                       mfcc13_list, mfcc14_list, mfcc15_list, mfcc16_list, mfcc17_list, mfcc18_list, mfcc19_list, mfcc20_list, mfcc21_list, mfcc22_list, mfcc23_list, mfcc24_list,
                                       mfcc25_list, mfcc26_list, mfcc27_list, mfcc28_list, mfcc29_list, mfcc30_list, mfcc31_list, mfcc32_list, mfcc33_list, mfcc34_list, mfcc35_list, mfcc36_list,
                                       mfcc37_list, mfcc38_list, mfcc39_list, mfcc40_list, mfcc41_list, mfcc42_list, mfcc43_list, mfcc44_list, mfcc45_list, mfcc46_list, mfcc47_list, mfcc48_list]),
                                       columns=['voiceID', 'duration', 'meanF0Hz', 'stdevF0Hz', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7','mfcc8','mfcc9', 'mfcc10', 'mfcc11', 'mfcc12',
                                                'mfcc13', 'mfcc14', 'mfcc15', 'mfcc16', 'mfcc17','mfcc18','mfcc19', 'mfcc20', 'mfcc21', 'mfcc22', 'mfcc23', 'mfcc24',
                                                'mfcc25', 'mfcc26', 'mfcc27','mfcc28','mfcc29', 'mfcc30', 'mfcc31', 'mfcc32', 'mfcc33', 'mfcc34', 'mfcc35', 'mfcc36',
                                                'mfcc37','mfcc38','mfcc39', 'mfcc40', 'mfcc41', 'mfcc42', 'mfcc43', 'mfcc44', 'mfcc45', 'mfcc46', 'mfcc47', 'mfcc48'])


df.to_csv("C:\\SPIRE Internship 2020\\age_features.csv", index=False)
df = pd.read_csv('C:\\SPIRE Internship 2020\\age_features.csv', header=0)
df.sort_values('voiceID')

# Write out the final dataframe
df.to_csv("C:\\SPIRE Internship 2020\\age_features1.csv", index=False)
