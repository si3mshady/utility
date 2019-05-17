import moviepy.editor  as me


class Extract_Audio:
    def __init__ (self,video_file,save_as):
        self.video = video_file
        self.save_file = save_as


    def extract_sound(self):
        videoclip = me.VideoFileClip(self.video)
        videoclip.audio.write_audiofile(self.save_file)

 
vid = input("Video file: ")
save_as = input("Save file as: ")

source = Extract_Audio(vid,save_as)
source.extract_sound()


#created a small python script from the moviepy lib  for extracting and saving audio from video source 5-17-19
