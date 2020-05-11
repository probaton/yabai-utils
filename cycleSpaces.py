import subprocess

def runCommand(command):
  process = subprocess.run(command.split(),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    universal_newlines=True)
  return process.stdout


print(runCommand('yabai -m query --displays'))