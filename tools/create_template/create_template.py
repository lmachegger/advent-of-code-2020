import argparse
import os

# parse args
parser = argparse.ArgumentParser()
parser.add_argument("foldername", help="name of folder")
parser.add_argument("location", help="where to create the template")
args = parser.parse_args()

# create dir
path = os.path.join(args.location, args.foldername)
os.mkdir(path)
print('created directory ' + args.foldername)

# create input files
input_files = ["input1", "input2"]
for inputf in input_files:
    file_path = os.path.join(path, inputf)
    f = open(file_path, 'x')
    f.close()


# create python files
def get_lines(index):
    return [
        "#Day " + args.foldername + "\n",
        "#Part " + index + "\n",
        "f = open('input" + index + "', 'r')"
    ]


python_files = ["part1.py", "part2.py"]
for i in range(len(python_files)):
    file_path = os.path.join(path, python_files[i])
    f = open(file_path, 'x')
    f.writelines(get_lines(str(i + 1)))
    f.close()
