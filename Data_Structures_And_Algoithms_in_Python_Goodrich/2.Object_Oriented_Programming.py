# Ke Shi on Feb 4th, 2022
# 2.3 Class Definitions
# Example: CreditCard Class
class CreditCard:
    """
    A consumer credit card.
    """

    def __init__(self,customer,bank,acnt,limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        :param customer: the name of the customer (e.g.,'John Browman')
        :param bank: the name of the bank (e.g.,'California Savings')
        :param acnt: the account identifier (e.g., '5391 0375 9387 5309')
        :param limit: credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stroed as a string)"""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

# Example: Multidimensional Vector Class
class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self,d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0]*d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Return jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))   # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other   # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

# Example: Iterators
class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self,sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reeference to the underlying data
        self._k = -1          # will increament to 0 oon the first call to next

    def __next__(self):
        """Return the next element, or else raise StopItereration error."""
        self._k += 1          # advance to next index
        if self._k < len(self._seq):  # return the data element
            return (self._seq[self._k])
        else:
            raise StopIteration()     # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

# Example: Range Class
class Range:
    """A class that mimic's built-in range class."""

    def __init__(self,start, stop = None, step = 1):
        """
        Initialize a Range isntance.
        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0,(stop - start + step -1)//step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k(using standard interpretation if negative)."""
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

# 2.4 Inheritance
# Extending the CreditCard Class
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self,customer,bank,acnt,limit,apr):
        """
        Create a new predatory credit card instance
        The initial balance is zero.
        customer: the name of the customer (e.g., 'John Bowman')
        bank: the name of the bank (e.g., 'California Savings')
        acnt: the acount identifier (e.g., '5391 0375 9387 5309')
        limit: credit limit (measured in dollars)
        apr: annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer,bank,acnt,limit) # call super constructor
        self._apr = apr

    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5     # access penalty
        return success             # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

# Hierarchy of Numeric Progressions
class Progression:
    """
    Iterator producing a generic progression.
    Default iterator produces the whole numbers 0,1,2...
    """
    def __init__(self,start = 0):
        """
        Initialize current to the first value of the progression.
        """
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        """
        Return the next element, or else raise StopIteration error.
        """
        if self._current is None:  # our onvention to end a progression
            raise StopIteration()
        else:
            answer = self._current # record current value to return
            self._advance()        # advance to prepare for next time
            return answer          # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self,n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))

# Arithmetic Progression Class
class ArithmeticProgression(Progression):   # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self,increment=1, start = 0):
        """
        Create a new arithmetic progression.
        increment: the fixed constant to add to each term (default 1)
        start: the first term of the progression (default 0)
        """
        super().__init__(start)  # initialize base class
        self._increment = increment

    def _advance(self):  # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment

class GeometricProgression(Progression):  # inherit from Progression
    """Iterator producing a geometric progression."""
    def __init__(self,base = 2, start = 1):
        """
        Create a new geographic progression.
        base: the fixed constant multiplied to each term (default 2)
        start: the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):  # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self,first=0,second = 1):
        """
        Create a new fibonacci progression.
        first: the first term of the progression (default 0)
        second: the second term of the progression (default 1)
        """
        super().__init__(first) # start progression at first
        self._prev = second -first # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev,self._current = self._current, self._prev + self._current

"""
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings','5391 0375 9387 5309',2500))
    wallet.append(CreditCard('John Bowman','California Federal','3485 0399 3395 1954',3500))
    wallet.append(CreditCard('John Bowman','California Finance','5391 0375 9387 5309',5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =',wallet[c].get_customer())
        print('Bank =',wallet[c].get_bank())
        print('Account =',wallet[c].get_account())
        print('Limit =',wallet[c].get_limit())
        print('Balance =',wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()

    v = Vector(5)  # construct five-dimensional <0,0,0,0,0>
    v[1] = 23  # <0,23,0,0,0> (based on use of __setitem__)
    v[-1] = 45   # <0,23,0,0,45> (also via __setitem__)
    print(v[4])  #print 45 (via __getitem__)
    u = v + v  # <0,46,0,0,90> (via __add__)
    w = v + [1,2,3,4,5]
    print(w)
    print(u)  # print <0,46,0,0,90>
    total = 0
    for entry in v:  # implicit iteration via __len__ and __getitem__
        total += entry

"""

if __name__ == '__main__':
    print('Default Progression:')
    Progression().print_progression(10)

    print("Arithmetic progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic progression with increment 5 and start 2:")
    ArithmeticProgression(5,2).print_progression(10)

    print("Geometric progression with default base:")
    GeometricProgression().print_progression(10)

    print("Geomtric progression with base 3:")
    GeometricProgression().print_progression(10)

    print("Fibonacci progression with default start values:")
    FibonacciProgression().print_progression(10)

    print("Fibonacci progression with start values 4 and 6:")
    FibonacciProgression(4,6).print_progression(10)

