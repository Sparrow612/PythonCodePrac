from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]: return False
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check(i, j, k):
        if word[k] != board[i][j]: return False
        if k == len(word) - 1: return True

        visited.add((i, j))
        result = False
        for di, dj in directions:
            newi = i + di
            newj = j + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if check(newi, newj, k + 1) and (newi, newj) not in visited:
                    result = True
                    break
        visited.remove((i, j))
        return result

    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if check(i, j, 0): return True
    return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(exist(board, "ABCCED"))
