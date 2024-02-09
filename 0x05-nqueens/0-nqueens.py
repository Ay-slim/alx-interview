#!/usr/bin/python3
"""Optimal N chess queens positioning"""
import sys


try:
    input_len = int(sys.argv[1])
except IndexError:
    print("Usage: nqueens N")
    sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)
else:
    if input_len and input_len < 4:
        print("N must be at least 4")
        sys.exit(1)


answers = []
squares = None


def belligerent(q1, q2):
    """
    Checks whether two queens are within
    each other's capturing range
    """
    if (q1[0] == q2[0]) or (q1[1] == q2[1]):
        return True
    return abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_cluster(cluster):
    """Checks whther a cluster belongs in the answers"""
    global answers
    for ans in answers:
        idx = 0
        for position in ans:
            for cluster_position in cluster:
                if (position[0]
                    == cluster_position[0]) and (position[1]
                                                 == cluster_position[1]):
                    idx += 1
        if idx == input_len:
            return True
    return False


def create_answers(rank, cluster):
    """Generates a potential anser"""
    global answers
    global input_len
    if rank == input_len:
        holder = cluster.copy()
        if not check_cluster(holder):
            answers.append(holder)
    else:
        for file in range(input_len):
            indx = (rank * input_len) + file
            hits = zip(list([squares[indx]]) * len(cluster), cluster)
            checked = map(lambda x: belligerent(x[0], x[1]), hits)
            cluster.append(squares[indx].copy())
            if not any(checked):
                create_answers(rank + 1, cluster)
            cluster.pop(len(cluster) - 1)


def fetch_answers():
    """Apply helper function to input args"""
    global squares, input_len
    squares = list(map(lambda x:
                       [x // input_len, x % input_len], range(input_len ** 2)))
    indx = 0
    cluster = []
    create_answers(indx, cluster)


fetch_answers()
for ans in answers:
    print(ans)
