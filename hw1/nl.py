import sys


def number_lines(file: str | None = None) -> None:
    """
    Print the lines of a file or stdin, each prefixed by its line number.
    """
    line_number: int = 1
    if file:
        with open(file, 'r') as f:
            for line in f:
                print(f"{line_number}\t{line}", end='')
                line_number += 1
    else:
        for line in sys.stdin:
            print(f"{line_number}\t{line}", end='')
            line_number += 1


if __name__ == "__main__":
    filename: str | None = sys.argv[1] if len(sys.argv) > 1 else None
    number_lines(filename)
