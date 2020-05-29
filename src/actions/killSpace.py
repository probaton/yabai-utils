from ..commandLine.yabaiUtil import query, runCommand

def killSpace():
  currentSpace = query("--spaces --space")["index"]

  winIds = map(lambda win: win["id"], query("--windows --space"))
  for winId in winIds:
    runCommand(f"window {winId} --close")
  
  runCommand(f"space --destroy {currentSpace}")

if __name__ == "__main__":
  killSpace()
