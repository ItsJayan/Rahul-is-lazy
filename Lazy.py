import os
if os.path.exists("Rahul is lazy.txt"):
  os.remove("Rahul is lazy.txt")
else:
  print("The file does not exist")