import re

from models import Rule

def rate(title, rules):
    score = 1.0
    matches = []

    for rule in rules:
        if re.search(rule.regex, title, re.IGNORECASE|re.UNICODE):
            score *= rule.multiplier
            matches.append(rule)

    return score, matches
