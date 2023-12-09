import sys


def count_stats(filename: str = None) -> tuple[int, int, int]:
    """
    Count the number of lines, words, and characters in a file or stdin.
    """
    num_lines: int = 0
    num_words: int = 0
    num_chars: int = 0

    try:
        if filename:
            with open(filename, 'r') as f:
                for line in f:
                    num_lines += 1
                    num_words += len(line.split())
                    num_chars += len(line)
        else:
            for line in sys.stdin:
                num_lines += 1
                num_words += len(line.split())
                num_chars += len(line)

        return num_lines, num_words, num_chars
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return 0, 0, 0


if __name__ == "__main__":
    total_lines: int = 0
    total_words: int = 0
    total_chars: int = 0

    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            lines, words, chars = count_stats(filename)
            print(f"{lines} {words} {chars} {filename}")
            total_lines += lines
            total_words += words
            total_chars += chars

        if len(sys.argv) > 2:
            print(f"{total_lines} {total_words} {total_chars} total")
    else:
        lines, words, chars = count_stats()
        print(f"{lines} {words} {chars}")
