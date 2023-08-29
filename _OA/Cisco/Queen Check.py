def can_queen_attack(qR, qC, oR, oC):
    # If queen and the opponent
    # are in the same row
    if qR == oR:
        return True

    # If queen and the opponent
    # are in the same column
    if qC == oC:
        return True

    # If queen can attack diagonally
    if abs(qR - oR) == abs(qC - oC):
        return True

    # Opponent is safe
    return False

# Driver code
def main():
    qR, qC = 1, 1
    oR, oC = 3, 2
    if can_queen_attack(qR, qC, oR, oC):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
