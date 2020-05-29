import os

def getId(parentId, type):
  try:
    file = open(f"db/{type}/{parentId}")
    return file.read()
  except FileNotFoundError:
    return None

if __name__ == "__main__":
  from sys import argv
  print(getId(argv[1], argv[2]))
