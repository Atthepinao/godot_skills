import os
import sys

def print_tree(startpath):
    if not os.path.exists(startpath):
        print(f"Path not found: {startpath}")
        return

    startpath = os.path.abspath(startpath)

    for root, dirs, files in os.walk(startpath):
        # Filter hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        dirs.sort()
        files.sort()
        
        # Calculate level
        relpath = os.path.relpath(root, startpath)
        if relpath == '.':
            level = 0
            curr_name = os.path.basename(startpath)
        else:
            level = relpath.count(os.sep) + 1
            curr_name = os.path.basename(root)

        indent = '    ' * level
        print(f'{indent}{curr_name}/')
        
        subindent = '    ' * (level + 1)
        for f in files:
            if f.endswith('.import'):
                continue
            print(f'{subindent}{f}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "."
    print_tree(target)