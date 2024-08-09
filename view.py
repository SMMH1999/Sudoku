def show(sudoku):
    for row_i, row_v in enumerate(sudoku):
        if row_i % 3 == 0:
            template = f'{"-" * 9}'
            print(f"+{template}+{template}+{template}+")
        for col_i, col_v in enumerate(row_v):
            if col_i % 3 == 0:
                print(f"| {col_v} ", end="")
            else:
                print(f" {col_v} ", end="")
        print("|")
    template = f'{"-" * 9}'
    print(f"+{template}+{template}+{template}+")
