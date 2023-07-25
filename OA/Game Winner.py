# Two players are playing a game where white or black pieces are represented by a string, colors.
# The game rules are as Wendy moves first and then they take alternate turns.
# With each move, Wendy may remove a white piece that has adjacent white pieces
# on both sides.Likewise, with each move, Bob may remove any black piece that has
# adiacent black pieces on both sidesAfter a piece is removed, the string is reduced
# in size by one piece. For instance, removing 'from 'XYZ' results in 'XzWhen a plaver can
# no longer move, they have lost the game.
# 类似LC2038直接跳转2038
class Solution(object):
    def winnerOfGame(self, colors):
        a, b = 0, 0
        a_chances, b_chances = 0, 0
        if colors[0] == "A":
            a += 1
        else:
            b += 1
        for i in range(1, len(colors)):
            if colors[i] == "A":
                if colors[i] == colors[i-1]:
                    a += 1
                else:
                    if b > 2:
                        b_chances += (b-2)
                    a, b = 1, 0
            if colors[i] == "B":
                if colors[i] == colors[i-1]:
                    b += 1
                else:
                    if a > 2:
                        a_chances += (a-2)
                    a, b = 0, 1
        if a > 2:
            a_chances += a-2
        if b > 2:
            b_chances += b - 2

        if a_chances <= b_chances:
            return False
        else:
            return True
