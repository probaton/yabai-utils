from ..commandLine.yabaiUtil import query, runCommand
from .restoreWindowFocus import restoreWindowFocus

def killEmptySpaces():
  spaces = query("--spaces")
  spaces.sort(key = lambda space: -space["index"])

  resetFocus = False
  for space in spaces:
    if space["windows"] == []:
      if space["has-focus"] == True:
        resetFocus = True
      runCommand(f"space {space['index']} --destroy")

  if resetFocus:
    try:
      next(space for space in spaces if space["has-focus"] == True)
      restoreWindowFocus(space)
    except StopIteration:
      pass

if __name__ == "__main__":
  killEmptySpaces()
