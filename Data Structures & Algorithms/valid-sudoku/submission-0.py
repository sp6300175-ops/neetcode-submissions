class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for r in range(9)]
        col  = [set() for c in range(9)]
        boxes = [set() for b in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                box_id = (i // 3) * 3 + (j // 3)

                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in col[j]:
                    return False
                col[j].add(val)
                if val in boxes[box_id]:
                    return False
                boxes[box_id].add(val)

        return True

