import glob

files = glob.glob('*.py')  # Get all Python files in the current directory
for file in files:
    print(file)