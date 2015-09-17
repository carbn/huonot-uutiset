import re

from models import Rule

def rate(title, rules):
    score = 1.0
    matches = []

    for rule in rules:
        m = re.search(rule.regex, title, re.IGNORECASE|re.UNICODE)

        if m and m.group(0):
            score *= rule.multiplier
            matches.append(rule)

    return score, matches
