import moviepy.editor  as me
import sys


class Extract_Audio:        
    def __init__ (self):
        self.video = sys.argv[1]
        self.save_file = sys.argv[2]
        

    def extract_sound(self):
        try:
            videoclip = me.VideoFileClip(self.video)
            videoclip.audio.write_audiofile(self.save_file)
        except OSError:
            print('Unable to locate file!')
    
go = Extract_Audio()
go.extract_sound()



#created a small python script from the moviepy lib  for extracting and saving audio from video source 5-17-19
#Elliott Arnold 
