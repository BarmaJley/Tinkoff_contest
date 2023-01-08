import ast
import numpy as np
import sys


def metr(c1, c2):
    return 0 if c1 == c2 else 1


def levenstein(str1, str2) -> float:
    n, m = len(str1), len(str2)
    D = np.empty((n + 1, m + 1))

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                D[i][j] = 0
            elif i > 0 and j == 0:
                D[i][j] = i
            elif i == 0 and j > 0:
                D[i][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(
                D[i - 1][j - 1] + metr(str1[i - 1], str2[j - 1]),
                D[i - 1][j] + 1,
                D[i][j - 1] + 1)

    return D[-1][-1] / n


def normalise(text) -> str:
    astree = ast.parse(text)
    return ast.unparse(astree)


def get_text(filename) -> str:
    text = ""
    file = open(filename, "r")
    for line in file.read():
        text += line
    return text


def parse_input(argv) -> str:
    with open(sys.argv[1], "r") as file:
        text = file.read()
    return text


if __name__ == "__main__":
    result = []
    input = parse_input(sys.argv).split("\n")
    for line in input:
        l = line.split(" ")
        text1 = get_text(l[0])
        text2 = get_text(l[1])

        text1 = normalise(text1)
        text2 = normalise(text2)

        result.append(round(levenstein(text1, text2), 2))

    with open("score.txt", "w") as f:
        for line in result:
            f.write(str(line) + '\n')
