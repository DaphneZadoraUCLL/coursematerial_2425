def ranking_table(ranking):
    max_rank_width = len(str(len(ranking)))
    max_name_width = max(len(name) for name, _ in ranking)

    lines = []

    for i, (name, time) in enumerate(ranking, start=1):
        line = str(i).rjust(max_rank_width) + " " + \
            name.ljust(max_name_width) + " " + f"{time:.2f}"
        lines.append(line)

    return "\n".join(lines)
