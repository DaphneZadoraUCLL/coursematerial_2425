def count_lines_in_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)
