import collections
class TicTacToe(object):
    def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move

count = collections.Counter()
count[0,1,3] = 1

for i, x in enumerate((1,2,3,4)):
    print(x)

print(enumerate((1,2,3,4)))