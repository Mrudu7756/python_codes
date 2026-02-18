import os 

path = "."
content = os.listdir(path)
print("Content of directory:")
for item in content:
    print(item)