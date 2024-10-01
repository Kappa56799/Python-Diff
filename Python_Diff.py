import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Python_Diff.py <file1> <file2>")
        sys.exit(1)

    files = sys.argv[1:]
    diff(files)

def diff(files):
    with open(files[0], 'r') as f1:
        with open(files[1], 'r') as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

    file1_length = len(file1_lines)
    file2_length = len(file2_lines)

    i, j = 0, 0

    while i < file1_length or j < file2_length:
        if i >= file1_length:
            print(f"{i}a{j+1},{file2_length}")
            for k in range(j, file2_length):
                print(f"> {file2_lines[k].strip()}")
            break
        elif j >= file2_length:
            print(f"{i+1},{file1_length}d{j}")
            for k in range(i, file1_length):
                print(f"< {file1_lines[k].strip()}")
            break
        elif file1_lines[i] != file2_lines[j]:
            if file1_lines[i:i+1] != file2_lines[j:j+1]:
                if file1_lines[i+1:i+2] == file2_lines[j:j+1]:
                    print(f"{i+1}d{j+1}")
                    print(f"< {file1_lines[i].strip()}")
                    i += 1
                elif file1_lines[i:i+1] == file2_lines[j+1:j+2]:
                    print(f"{i}a{j+1}")
                    print(f"> {file2_lines[j].strip()}")
                    j += 1
                else:
                    print(f"{i+1}c{j+1}")
                    print(f"< {file1_lines[i].strip()}")
                    print("---")
                    print(f"> {file2_lines[j].strip()}")
                    i += 1
                    j += 1
        else:
            i += 1
            j += 1

if __name__ == '__main__':
    main()
