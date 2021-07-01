"""A video player class."""
import random
from .video_library import VideoLibrary
from .video import Video
from .video_playlist import Playlist
class VideoPlayer:
    """A class used to represent a Video Player."""
    current_video_title="NULL"
    current_video="NULL"
    all_videos=[]
    random_movie=[]
    playingFlag=0
    stopFlag=0
    pauseFlag=0
    playlistIndex=0
    #For playlist PART -2
    playlistNames=[]
    def __init__(self):
        
        self._video_library = VideoLibrary()
        self._video_playlist=Playlist()
        self.all_videos=sorted(self._video_library.get_all_videos(),key=lambda x: x.title)

    def number_of_videos(self): #working
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):  
        """Returns all videos."""

        print("Here's a list of all avaiable videos:\n ")
        for v in self.all_videos:
            tag=str(v.tags)[1:-1].replace(",","").replace("'","");
            print(v.title +" " + "(" + v.video_id + ")" + " " +"["+tag+"]");
       
      

    def play_video(self, video_id): #it hss some missing parts check it again.
        """Plays the respective video. """
        
    # if(video_id != ( "amazing_cats_video_id" or "funny_dogs_video_id" or "another_cat_video_id " or "life_at_google_video_id  " or "nothing_video_id " )):
    #     exit()
    # else:
        if(self.playingFlag==1):
            self.stop_video()
            self.playingFlag=0

        current_video=self._video_library.get_video(video_id)
        self.current_video_title=current_video.title
        print("Playing video : " + self.current_video_title)
        self.playingFlag=1
        
            

    def stop_video(self):   #working
        """Stops the current video."""
        if(self.playingFlag==0):
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping Video: " + self.current_video_title)
            self.stopFlag=1 #Video is stopped
            self.playingFlag=0

    def play_random_video(self):    #WORKING
        """Plays a random video from the video library."""
        if(self.playingFlag==1 ):
            self.stop_video()
            self.playingFlag=0
        random_movie=random.choice(self.all_videos)
        self.play_video(random_movie.video_id)
        self.playingFlag=1

    def pause_video(self):
        """Pauses the current video."""
        if(self.playingFlag==1 and self.pauseFlag==0):  #AND PAUSE FLAG DEKHLO
            print("Pausing video :" + self.current_video_title)
            self.pauseFlag=1
        elif(self.pauseFlag==1 and self.stopFlag==0):
            print("Video already paused: " + self.current_video_title) 
        else:
            print("Cannot pause video: No video is currently playing" )

    def continue_video(self):   #Works only  on
        """Resumes playing the current video."""
        if(self.pauseFlag==1 ):
            print("Continuing video: " + self.current_video_title)
            self.playingFlag=1
            self.pauseFlag=0
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if(self.playingFlag==0):
            print("No video is currently playing")
        else:
            self.playingFlag=1
            # print(self.current_video.title() + "(" + self.current_video.video_id() + ")" +"["+self.current_video.tags()+"]");
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        flag=0
        i=0
        for list in self.playlistNames:
            print(i)
            if(playlist_name.casefold()==list.casefold()):
                flag=1
        if(flag==0):
            self.playlistNames.append(playlist_name)
            print('Successfully created new playlist: '+ playlist_name)
            flag=0
        elif(flag==1):
            print('Cannot create playlist: A playlist with the same name already exists')
            flag=0
            
        
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        a=playlist_name
        flag2=0
        for list in self.playlistNames:
            if(playlist_name.casefold()==list.casefold()):
                flag2=0
                break
            else:
               
                flag2=1
                continue

        flag1=1
        if(self._video_library.get_video(video_id)):
            flag1=0 #if found
    
        else:
            flag1=1 #if not found

        if(flag2==1):
            print("Cannot add video to :" + playlist_name +  "Playlist does not exist")
        elif(flag1==1):
            print("Cannot add video to my_playlist: Video does not exist")
        elif(flag2==1 and flag1==1):
            print("Cannot add video to :" + playlist_name +  "Playlist does not exist")
        else:
            self._video_playlist.playlistItem(a,video_id)
       

    def show_all_playlists(self):
        """Display all playlists."""
        
        print("Showing all playlists:")
        for line in self.playlistNames:
            if not line:
                print("No playlists exist yet")
            else:
                print(line)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        flag=0
        for line in self.playlistNames:
            if(line==playlist_name):
                flag=1 #found
            else:
                flag=0#not found
                continue
        if(flag==0):
            print("Cannot show playlist another_playlist: Playlist does not exist")
        else:
            print("Showing playlist : " + playlist_name)
            a=self._video_playlist.getlength()
            if(a):
                self._video_playlist.displayAllPlaylist()
            else:
                print("No videos here yet")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        flag2=0
        for list in self.playlistNames:
            if(playlist_name.casefold()==list.casefold()):
                flag2=0 #found
                break
            else:
               
                flag2=1 #not found
                continue
        if(flag2==1):
            print("Cannot remove video from" + playlist_name +  " : Playlist does not exist")
        else:
            self._video_playlist.removePlaylistItem(playlist_name,video_id)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        flag2=0
        for list in self.playlistNames:
            if(playlist_name.casefold()==list.casefold()):
                flag2=0 #found
                break
            else:
               
                flag2=1 #not found
                continue
        if(flag2==1):
            print("Cannot clear playlist " + playlist_name +  " : Playlist does not exist")
        else:
            self._video_playlist.clearplayList(playlist_name)
            print("Successfully removed all videos from "+ playlist_name )

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        flag2=0
        for list in self.playlistNames:
            if(playlist_name.casefold()==list.casefold()):
                flag2=0 #found
                break
            else:
               
                flag2=1 #not found
                continue
        if(flag2==1):
            print("Cannot delete playlist " + playlist_name +  " : Playlist does not exist")
        else:
            self.playlistNames.remove(playlist_name)
            print("Deleted playlist: "+ playlist_name)
            self._video_playlist.clearplayList(playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
