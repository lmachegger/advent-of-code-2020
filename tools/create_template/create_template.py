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

# create input file
input_file = 'input' + args.foldername
file_path = os.path.join(path, input_file)
f = open(file_path, 'x')
f.close()


# create python files
def get_lines(index):
    return [
        "#Day " + args.foldername + "\n",
        "#Part " + index + "\n",
        "with open('" + args.foldername + "/input" +
        args.foldername + "', 'r') as f:"
    ]


for i in range(0, 2):
    file_name = 'day'+args.foldername+'_' + str(i+1) + '.py'
    file_path = os.path.join(path, file_name)
    f = open(file_path, 'x')
    f.writelines(get_lines(str(i + 1)))
    f.close()
