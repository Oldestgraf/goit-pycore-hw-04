import sys
from colorama import Fore, Style
import pathlib

def visualize_directory_structure(directory_path, indent=''):
    directory = pathlib.Path(directory_path)
    for item in directory.iterdir():
        if item.is_file():
            # File name with green color
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)
        elif item.is_dir():
            # Directory name with blue color
            print(indent + Fore.BLUE + item.name + Style.RESET_ALL)
            # Display nested directories
            visualize_directory_structure(item, indent + '  ')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not pathlib.Path(directory_path).is_dir():
        print("Error: Provided path is not a directory.")
        sys.exit(1)

    visualize_directory_structure(directory_path)