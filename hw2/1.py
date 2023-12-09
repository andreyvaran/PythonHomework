def generate_latex_table(data: list[list[str]]) -> str:
    format_row = lambda row: " & ".join(row) + " \\\\\n\\hline\n"

    rows = map(format_row, data)

    return "\\begin{tabular}{|" + " | ".join(["l"] * len(data[0])) + "|}\n\\hline\n" + "".join(rows) + "\\end{tabular}"


def save_latex_to_file(latex_code: str, file_path: str) -> None:
    with open(file_path, 'w') as file:
        file.write(latex_code)


def main() -> None:
    data: list[list[str]] = [
        ["Header1", "Header2", "Header3"],
        ["asd", "asd", "czxcz"],
        ["ads", "Row2Col2", "aasdf"],
        ["Row3Col1", "asv", "sdnajk"]
    ]

    file_path: str = 'result.tex'

    save_latex_to_file(generate_latex_table(data), file_path)
    print(f"Table saved to {file_path}")


if __name__ == "__main__":
    main()
