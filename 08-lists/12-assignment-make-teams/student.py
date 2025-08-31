def make_teams(participants, team_size):
    if team_size <= 0:
        return []

    teams = []

    i = 0
    while i < len(participants):
        team = []
        for j in range(team_size):
            if i < len(participants):
                team.append(participants[i])
                i += 1
        teams.append(team)

    if len(teams) > 1:
        last_team = teams[-1]
        if len(last_team) < team_size:
            leftovers = teams.pop()
            index = 0
            for name in leftovers:
                teams[index].append(name)
                index += 1
                if index >= len(teams):
                    index = 0

    return teams
