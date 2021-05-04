import os
import sys

def main():
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".xml"): 
            original = filename
            new = sys.argv[2] + filename
            os.rename(original, new)
            continue
        else:
            continue

if __name__ == "__main__":
    main()