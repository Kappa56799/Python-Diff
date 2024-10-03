import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Python_Diff.py <file1> <file2>")
        sys.exit(1)

    files = sys.argv[1:]
    diff(files)

def diff(files):
    with open(files[0], 'r') as f1:
        file1_lines = f1.readlines()
    with open(files[1], 'r') as f2:
        file2_lines = f2.readlines()

    file1_length = len(file1_lines)
    file2_length = len(file2_lines)

    i, j = 0, 0

    file1_buffer = []
    file2_buffer = []
    change_start_i = change_start_j = None

    while i < file1_length or j < file2_length:
        if i < file1_length and j < file2_length:
            if file1_lines[i] != file2_lines[j]:
                if change_start_i is None:
                    change_start_i = i
                    change_start_j = j
                file1_buffer.append(f"< {file1_lines[i]}")
                file2_buffer.append(f"> {file2_lines[j]}")
            else:
                if file1_buffer or file2_buffer:
                    print_changes(change_start_i, i, change_start_j, j, file1_buffer, file2_buffer)
                    file1_buffer = []
                    file2_buffer = []
                    change_start_i = change_start_j = None
            i += 1
            j += 1
        elif i < file1_length:
            if change_start_i is None:
                change_start_i = i
                change_start_j = j
            file1_buffer.append(f"< {file1_lines[i]}")
            file2_buffer.append("> ")
            i += 1
        elif j < file2_length:
            if change_start_i is None:
                change_start_i = i
                change_start_j = j
            file1_buffer.append("< ")
            file2_buffer.append(f"> {file2_lines[j]}")
            j += 1

    if file1_buffer or file2_buffer:
        print_changes(change_start_i, i, change_start_j, j, file1_buffer, file2_buffer)

def print_changes(start_i, end_i, start_j, end_j, file1_buffer, file2_buffer):
    if end_i - start_i == 1 and end_j - start_j == 1:
        print(f"{start_i+1}c{start_j+1}")
    else:
        print(f"{start_i+1},{end_i}c{start_j+1},{end_j}")
    
    print("".join(file1_buffer), end="")
    print("---")
    print("".join(file2_buffer), end="")

if __name__ == '__main__':
    main()
