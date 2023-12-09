import sys


def tail(filename=None, n=10):
    """
    Print the last n lines of a file or stdin.
    """
    try:
        if filename:
            with open(filename, 'r') as f:
                lines = f.readlines()
        else:
            lines = sys.stdin.readlines()

        for line in lines[-n:]:
            print(line, end='')
    except Exception as e:
        print(f"Error reading file {filename}: {e}")


if __name__ == "__main__":
    num_lines = 10
    num_lines_stdin = 17

    if len(sys.argv) > 1:
        for index, filename in enumerate(sys.argv[1:], 1):
            if len(sys.argv) > 2:
                print(f"==> {filename} <==")
            tail(filename, num_lines)
            if index < len(sys.argv) - 1:
                print()
    else:
        tail(n=num_lines_stdin)
