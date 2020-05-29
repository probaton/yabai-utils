import subprocess
import json

def __runCommand(command):
  process = subprocess.run(command.split(),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    universal_newlines=True)
  
  if process.stderr:
    raise Exception(f"Command <{command}> failed:\n{process.stderr}")

  return process.stdout

def runCommand(command):
  yabaiCommand = "yabai -m " + command
  return __runCommand(yabaiCommand)

def query(toQuery):
  rawResult = runCommand("query " + toQuery)
  return json.loads(rawResult)
