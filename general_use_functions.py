import sys


def possible_score_standard():
    # list of possible score to get
    score = set(list(range(1, 21)) + [2 * i for i in range(1, 21)] + [3 * i for i in range(1, 21)])
    score = score | {25, 50}
    score = list(score)
    return score


def exit_protocol():
    # stops window closing after program execution ends
    input("\nWciśnij enter by zamknąć program.")
    sys.exit()
