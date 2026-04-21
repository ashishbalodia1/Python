from pathlib import Path

# Absolute path - from the root of directory
# Windows-  C:\Program Files\Microsoft\Main
# MacBook-  /user/local/bin

# Relative path

# path= Path("ecommerce")
# print(path.exists())

# Make directory
# path1= Path("emails")
# print(path1.mkdir())

# To remove directory
# print(path1.rmdir())

# glob method
path= Path()
for file in path.glob("*.py"):
    print(file)

