import json

with open("partB/task_3_1.ipynb", "r") as f:
    text = f.read()

# I accidentally added an extra comma or malformed json via my multi_replace_file line replacement.
# Re-writing the file cleanly is the fastest fix.
