import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

if not os.path.exists(args.filename):
    print(f"{args.filename}: no such file or directory")
    exit(1)
replace = {}
temp = ""
with open(args.filename) as f:
    for line in f.readlines():
        if line.startswith('.include'):
            filename = line.split(' ')[1].rstrip()
            with open(filename) as f:
                temp += f.read()
        elif line.startswith('.define'):
            args = line.rstrip().split(' ')
            replace[args[1]] = args[2]
        else:
            temp+=line

for find, r in replace.items():
    temp.replace(find, r)
print(temp)
