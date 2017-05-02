#!/usr/bin/env python

"""
@author: Justice Amoh
@description: Script for building a pandas dataframe database for spoken digit data
@date: 02/05/2017
"""

# All Necessary Imports
## Basic imports
import os
import re
import sys
import gzip
import librosa
import pandas as pd
import cPickle as pickle


#####################################
############  LOAD DATA  ############
#####################################

# Load Wav File Paths
wavfiles=[]

root='recordings/'
exclude = set(['others', 'breath', 'wheeze'])
for path, dirs, files in os.walk(root, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            wavfiles.append(os.path.join(path, file))

# STFT Computation
Fs   = 8000
nfft = 128
hop  = nfft/2


## Initialize Variables
Wave      = []
Magnitude = []
Phase     = []
SIndex    = []
Class     = []

    

for wavfile in wavfiles:
    # Open audio file
    y, sr = librosa.load(wavfile,sr=8000)
    
    # # Normalize by RMSE
    # rmse = librosa.feature.rmse(y,hop_length=len(y)+1)[0][0]
    # y = y/rmse
    
    ## Compute STFT
    nfft = 128
    hop  = nfft/2
    s = librosa.stft(y,n_fft=nfft-1,hop_length=hop)
    magnitude, phase = librosa.magphase(s) 

    magnitude = librosa.amplitude_to_db(magnitude)
    phase     = np.angle(phase)

    # f = librosa.fft_frequencies(sr=sr,n_fft=nfft)
    # t = librosa.frames_to_time(np.arange(0,S.shape[1]),sr=sr,hop_length=hop)
    

    svar = re.split('[_/.]',wavfile)

    Wave.append(y)
    Magnitude.append(magnitude)
    Phase.append(phase)
    SIndex.append(int(svar[-2]))
    Class.append(svar[-4])
    
df =      pd.DataFrame({ 'Wave'         : pd.Series(Wave),
                         'Magnitude'    : pd.Series(Magnitude),
                         'Phase'        : pd.Series(Phase),
                         'SIndex'       : pd.Series(SIndex),
                         'Class'        : pd.Categorical(Class) })


#####################################
############  SAVE DATA  ############
#####################################
save_on=True  # save or load file

dbfile ='SpokenDigitDB.pkl.gz'
if save_on:
    with gzip.open(dbfile, 'wb') as ifile:
        pickle.dump(df, ifile, 2)
        print('File saved as '+ dbfile)
