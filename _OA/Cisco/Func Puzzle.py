"""
You are given a grid of letters, followed by some words. The words can occur anywhere in the grid on a row or a column, forward or backwards. However, there are no diagonal words.Write an algorithm to find if the given word occurs in the grid on a row or a column, forward or backwards.
Input
The first line of input consists of two integers- grid_row and grid_col,representing the number of rows (N) and the number of columns (M) of the letter grid, respectively. The next M lines consist of N spaceseparated characters representing the letters of the grid. The next line consists of an integerword_size, representing the number of words to be searched from the given grid (K).The last line consists of K spaceseparated strings representing the words to search for in the grid.
Output
Print K space-separated strings consisting of "Yes" if the word is present in the grid or "No" if the word is not present in the grid.
Note
All the inputs are case-sensitive, meaning "a" and "A" are considered as two different characters.
Example
Input:
3 3
С А Т
I D O
N O M
4
CAT TOM ADO MOM
Output:
Yes Yes Yes No
Explanation:
From the given words "CAT" is found at the first row, "TOM" is found at last column, "ADO" is found at the middle column, but "MOM" is not found anywhere in the grid.So, the output is ["Yes", "Yes", "Yes", "No"].
"""
# LC 212
# [['С', 'А', 'Т'], ['I', 'D', 'O'], ['N', 'O', 'M']]
# ['CAT', 'TOM', 'ADO', 'MOM']
def funcPuzzle(grid, word):
    print(grid)
    print(word)

def main():
    grid = []
    grid_rows, grid_cols  = map(int, input().split())
    for idx in range(grid_rows):
      grid.append(list(map(str, input().split())))
    word = []
    word_size  = int(input())
    word = list(map(str,input().split()))
    result = funcPuzzle(grid, word)
    print(result)
if __name__ == "__main__":
    main()