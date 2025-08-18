from abc import ABC, abstractmethod

class device(ABC):
    def turn_on(self):
        print("Device is now ON")

    def turn_off(self):
        print("Device is now OFF")

class sound_device(device):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def volume_change(self, volume):
        raise NotImplementedError("This method should be overridden by subclasses")

class video_device(device):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def render(self, content):
        raise NotImplementedError("This method should be overridden by subclasses")

class multi_channel_device(device):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def channel_change(self, channel):
        raise NotImplementedError("This method should be overridden by subclasses")

class radio(sound_device, multi_channel_device):
    def __init__(self):
        super().__init__("Radio")
    
    def volume_change(self, volume):
        print(f"Radio volume set to {volume}")
    
    def channel_change(self, channel):
        print(f"Radio channel set to {channel}")

class television(sound_device, video_device, multi_channel_device):
    def __init__(self):
        super().__init__("Television")
    
    def volume_change(self, volume):
        print(f"Television volume set to {volume}")
    
    def render(self, content):
        print(f"Television displaying: {content}")
    
    def channel_change(self, channel):
        print(f"Television channel set to {channel}")
        render_content = f"Content for channel {channel}"
        self.render(render_content)

class i_remote_on_off(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def power_on(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    @abstractmethod
    def power_off(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class i_remote_volume(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def volume_change(self, volume):
        raise NotImplementedError("This method should be overridden by subclasses")

class i_remote_channel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def channel_change(self, channel):
        raise NotImplementedError("This method should be overridden by subclasses")

class remote_control(i_remote_on_off, i_remote_volume, i_remote_channel):
    def __init__(self, device):
        self.device = device
        self.volume = 0
        self.channel = 1

    def press_power_on(self):
        self.device.turn_on()

    def press_power_off(self):
        self.device.turn_off()

    def press_volume_change(self, volume):
        self.volume = volume
        print(f"Volume set to {self.volume}")
        self.device.volume_change(self.volume)

    def press_channel_change(self, channel):
        self.channel = channel
        print(f"Channel set to {self.channel}")
        self.device.channel_change(self.channel)

class upgraded_remote_control(remote_control):
    def __init__(self, device):
        super().__init__(device)

    def press_mute(self):
        print("Device is muted")
        self.device.volume_change(0)

    def press_unmute(self):
        print("Device is unmuted")
        self.device.volume_change(self.volume)

# Example usage of the bridge pattern
if __name__ == "__main__":
    radio_device = radio()
    tv_device = television()

    radio_remote = upgraded_remote_control(radio_device)
    tv_remote = upgraded_remote_control(tv_device)

    # Using the radio remote
    radio_remote.power_on()
    radio_remote.volume_change(10)
    radio_remote.channel_change(5)
    radio_remote.mute()
    radio_remote.unmute()
    radio_remote.power_off()

    print("\n")

    # Using the television remote
    tv_remote.power_on()
    tv_remote.channel_change(3)
    tv_remote.volume_change(15)
    tv_remote.power_off()