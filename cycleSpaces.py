import subprocess
import json

def runCommand(command):
  process = subprocess.run(command.split(),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    universal_newlines=True)
  
  if process.stderr:
    raise Exception(f"Command <{command}> failed:\n{process.stderr}")

  return process.stdout

def runYabaiCommand(command):
  yabaiCommand = "yabai -m " + command
  return runCommand(yabaiCommand)

def queryYabai(toQuery):
  rawResult = runYabaiCommand("query " + toQuery)
  return json.loads(rawResult)

def queryYabaiIds(toQuery):
  queryResult = queryYabai(toQuery)
  if isinstance(queryResult, dict):
    return queryResult["id"]
  else: 
    return list(map(lambda i: i["id"], queryResult))

def cycleSpaces():
  currentSpace = queryYabai("--spaces --space")
  displaySpaces = queryYabai("--spaces --display")
  currentIndex = displaySpaces.index(currentSpace)

  if currentIndex >= len(displaySpaces) - 1:
    nextIndex = 0
  else:
    nextIndex = currentIndex + 1

  runYabaiCommand(f"space --focus {displaySpaces[nextIndex]['index']}")

cycleSpaces()