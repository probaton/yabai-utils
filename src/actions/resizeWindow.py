from ..commandLine.yabaiUtil import query, runCommand

class WindowResizer:
  def __init__(self):
    self.interval = 100
    self.window = query("--windows --window")
    self.spaceWindows = query(f"--windows --space {self.window['space']}")
  
  def isRightWindow(self):
    for window in self.spaceWindows:
      if window["frame"]["x"] > self.window["frame"]["x"]:
        return False
    return True
  
  def isLeftWindow(self):
    for window in self.spaceWindows:
      if window["frame"]["x"] < self.window["frame"]["x"]:
        return False
    return True

  def expand(self):
    if len(self.spaceWindows) == 1:
      return

    if self.isRightWindow():
      return runCommand(f"window --resize left:-{self.interval}:0")

    if self.isLeftWindow():
      return runCommand(f"window --resize right:{self.interval}:0")

    runCommand(f"window --resize right:{self.interval/2}:0")
    runCommand(f"window --resize left:-{self.interval/2}:0")

  def shrink(self):
    if len(self.spaceWindows) == 1:
      return

    if self.isRightWindow():
      return runCommand(f"window --resize left:{self.interval}:0")

    if self.isLeftWindow():
      return runCommand(f"window --resize right:-{self.interval}:0")
    
    runCommand(f"window --resize left:{self.interval/2}:0")
    runCommand(f"window --resize right:-{self.interval/2}:0")
