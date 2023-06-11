import sys, platform

class Config:
    def __init__(self, path, platform) -> None:
        self.path = path
        self.platform = platform
        pass

def setConfig():
    return Config(sys.argv[0], platform.system())