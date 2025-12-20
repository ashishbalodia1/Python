message="\nThis is an append message2"

with open("file.txt", "a") as f:
    f.write(message)
