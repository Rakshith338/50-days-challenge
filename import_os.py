import os
from pathlib import Path

print("current working directory:")
print(os.getcwd())

print("\nFiles and Folders:")
for item in os.listdir():
    print(item)

devops_dir = Path("devops")

if not devops_dir.exists():
    devops_dir.mkdir()
    print("\n 'backup' folder created.")
else:
    print("\n'backup' folder already exists.")
