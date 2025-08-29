def increase_version(version, breaking_change, new_features):
    major, minor, patch = version
    if breaking_change:
        return (major + 1, 0, 0)
    elif new_features:
        return (major, minor + 1, 0)
    else:
        return (major, minor, patch + 1)

def is_more_recent(v1, v2):
    return v1 > v2

def is_older(v1, v2):
    return v2 > v1