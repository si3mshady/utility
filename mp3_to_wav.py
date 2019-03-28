import glob
from pydub import AudioSegment #library for converting audio mp3 to wav
from pathlib import Path

def find_files(pattern):
    pattern='*' + pattern
    matching=glob.glob(pattern)
    return matching

#convert mp3 files to wav
def mp3_to_wave(file_dictionary):
    for src, dest in file_dictionary.items():
        sound=AudioSegment.from_mp3(src)
        sound.export(dest, format="wav")
        print('Converted {} into {}'.format(src,dest))

#check if wav files have already been created
def check_wave_files_exist(file_dictionary):
    status=all([Path(str(file)).exists() for file in file_dictionary.values()]) #test for true 
    return status

pattern='mp3'
matching=find_files(pattern)
change_extension=[file.replace('mp3','wav') for file in matching]
before_after=dict(zip(matching,change_extension))
if check_wave_files_exist(before_after) == True:
    print('All .mp3 files have been convereted to .wav in this directory ')
    exit()
mp3_to_wave(before_after)










