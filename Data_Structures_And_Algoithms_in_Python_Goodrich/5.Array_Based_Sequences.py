# Ke Shi on Mar 18st, 2022
# 5.1 Python's Sequence Types
# 5.2 Low-Level Arrays
# 5.3 Dynamic Arrays and Amortization
import sys
data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)

# 5.3.1 Implementing a Dynamic Array
import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self,obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self,c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self,k,value):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self,value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('Value not found')

# 5.3.3 Python's List Class
from time import time
def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

# 5.4 Efficiency of Python's Sequence Types
# 5.4.2 Python's String Class
letters = ''
file = "abc"
for c in file:
    if c.isalpha():
        letters += c

temp = []
for c in file:
    if c.isalpha():
        temp.append(c)
    letters = ''.join(temp)

letters = ''.join(c for c in file if c.isalpha())

# 5.5 Using Array-Based Sequences
class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self,name,score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        # e.g. '(Bob, 98)'
        return '({0}, {1})'.format(self._name,self._score)

class Scoreboard:
    """Fixed-length sequence of high scores in nondecresasing order."""

    def __init__(self,capacity = 10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self,entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):     # no score drops from list
                self._n += 1                   # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]   # shift entry from j-1 to j
                j -= 1    # and decrement j
            self._board[j] = entry  # well done, add new entry

# 5.5.2 Sorting a Sequence
def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

# 5.5.3 Simple Cryptography
class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26  # temp array for encryption
        decoder = [None] * 26  # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)  # will stroe as string
        self._backward = ''.join(decoder)  # since fixed

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self,original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

# 5.6 Multidimensional Data Sets
class TicTacToe:
    """Management of a Tic-Tac-Toe game (does not do strategy)"""

    def __init__(self):
        """Start a new game."""
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player's turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self._board[i][j] != ' ':
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self,mark):
        """Check whether the board configuration is a win for the given player."""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """Return string representation of ccurrent game board."""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)

    game = TicTacToe()
    # X moves:                 # O moves:
    game.mark(1,1);            game.mark(0,2)
    game.mark(2,2);            game.mark(0,0)
    game.mark(0,1);            game.mark(2,1)
    game.mark(1,2);            game.mark(1,0)
    game.mark(2,0)

    print(game)
    winner = game.winner()
    if winner is None:
        print("Tie")
    else:
        print(winner,'wins')








