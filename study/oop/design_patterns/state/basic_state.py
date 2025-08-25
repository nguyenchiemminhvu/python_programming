from abc import ABC, abstractmethod
import time

class media_state(ABC):
    def __init__(self, media_player):
        self.media_player = media_player
    
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def prev(self):
        pass

class playing_state(media_state):
    def __init__(self, media_player):
        super().__init__(media_player)

    def play(self):
        print("Already playing.")
    
    def pause(self):
        print("Pausing playback.")
        self.media_player.set_state(self.media_player.paused_state)
    
    def next(self):
        self.media_player.next_track()
        self.media_player.play_current_track()
    
    def prev(self):
        self.media_player.prev_track()
        self.media_player.play_current_track()

class paused_state(media_state):
    def __init__(self, media_player):
        super().__init__(media_player)
    
    def play(self):
        print("Resuming playback.")
        self.media_player.set_state(self.media_player.playing_state)
        self.media_player.play_current_track()
    
    def pause(self):
        print("Already paused.")
    
    def next(self):
        self.media_player.next_track()
        self.media_player.set_state(self.media_player.playing_state)
        self.media_player.play_current_track()
    
    def prev(self):
        self.media_player.prev_track()
        self.media_player.set_state(self.media_player.playing_state)
        self.media_player.play_current_track()

class media_player:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_index = 0
        
        self.playing_state = playing_state(self)
        self.paused_state = paused_state(self)
        
        self.state = self.paused_state
    
    def set_state(self, state):
        self.state = state
        print(f"State changed to: {type(self.state).__name__}")
    
    def current_track(self):
        return self.playlist[self.current_index]
    
    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
    
    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
    
    def play(self):
        self.state.play()
    
    def pause(self):
        self.state.pause()
    
    def next(self):
        self.state.next()
    
    def prev(self):
        self.state.prev()
    
    def play_current_track(self):
        print(f"Playing: {self.current_track()}")

if __name__ == "__main__":
    playlist = ["Song 1", "Song 2", "Song 3"]
    player = media_player(playlist)

    player.play()  # Should start playing Song 1
    time.sleep(1)
    player.next()  # Should go to Song 2
    time.sleep(1)
    player.pause() # Should pause playback
    time.sleep(1)
    player.play()  # Should resume playback
    time.sleep(1)
    player.prev()  # Should go back to Song 1
    time.sleep(1)
    player.pause() # Should pause playback
    time.sleep(1)
    player.next()  # Should go to Song 2 and play