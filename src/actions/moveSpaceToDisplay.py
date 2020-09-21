from ..commandLine.yabaiUtil import query, runCommand

def moveSpaceToDisplay(targetDisplayIndex):
  allSpaces = query("--spaces")
  try:
    currentSpace = next(space for space in allSpaces if space["focused"] == 1)
  except StopIteration:
    return

  spacesOnCurrentDisplay = list(filter(lambda s: s["display"] == currentSpace["display"], allSpaces))
  if len(spacesOnCurrentDisplay) <= 1:
    runCommand("space --create")

  runCommand(f"space --display {targetDisplayIndex}")
  
if __name__ == "__main__":
  from sys import argv
  moveSpaceToDisplay(argv[1])
