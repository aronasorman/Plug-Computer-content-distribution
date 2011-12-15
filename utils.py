import os
import os.path

VIDEO_PATH = 'static/videos'

IGNORED_FILES = ['.DS_Store']

def list_videos():
    '''
    returns a list of tuples containing the name of the video,
    and the url to it
    '''
    videos = [vid for vid in os.listdir(VIDEO_PATH)
              if vid not in IGNORED_FILES]
    return videos
