"""A video playlist class."""

# from .video import Video
from .video_library import VideoLibrary
class Playlist:
    """A class used to represent a Playlist."""
    playlistItems=[]
    def __init__(self):
        self._video_library = VideoLibrary()

    def playlistItem(self,name,id):
        flag=0
        for list in self.playlistItems:
            if(id==list):
                print("Cannot add video to my_PLAYlist: Video already added")
                flag=1
                break
            else:
                flag=0
                continue
        if(flag==0):
            self.playlistItems.append(id)
            print("Added video to " + name + " : " + id)

    def getlength(self)->int:
        return len(self.playlistItems)

    def displayAllPlaylist(self):
        for line in self.playlistItems:
            
            movie=self._video_library.get_video(line)
            tag=str(movie.tags)[1:-1].replace(",","").replace("'","");
            print(movie.title +" "+  movie.video_id + " "+ tag)

    def removePlaylistItem(self,name,id):
       
        flag=0
        for list in self.playlistItems:

            if(id==list):
                flag=1
                break
            else:
                flag=0
                continue
        if(flag==0):
            print("Cannot remove video from my_playlist: Video is not in playlist")
        else:
            self.playlistItems.remove(id)
            print("Removed video from :" + name + " "+ id)
    
    def clearplayList(self,name):
        self.playlistItems.clear()
        