from ..commandLine.yabaiUtil import query, runCommand

def moveWindowToDisplay(targetDisplayIndex):
  currentWindowId = query("--windows --window")["id"]
  runCommand(f"window --display {targetDisplayIndex}")
  runCommand(f"window --focus {currentWindowId}")
