import argparse

parser = argparse.ArgumentParser(description= "Count the number of lines in a file.")
parser.add_argument("filename", help="The file to count lines in.")

# ✅ Fix: use parse_known_args() for Jupyter compatibility
args, _ = parser.parse_known_args()

try:
    with open(args.filename, "r") as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
    print(f"Error: File '{args.filename}' not found.")