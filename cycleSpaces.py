import subprocess
import json

def runCommand(command):
  process = subprocess.run(command.split(),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    universal_newlines=True)
  
  if (process.stderr):
    raise Exception(f"Command <{command}> failed:\n{process.stderr}")

  return process.stdout

def runYabaiCommand(command):
  yabaiCommand = "yabai -m " + command
  return runCommand(yabaiCommand)

def queryYabai(toQuery):
  rawResult = runYabaiCommand("query " + toQuery)
  return json.loads(rawResult)


print(queryYabai("--displays"))
