""" Count the number of prime numbers less than
    two million and time how long it takes
    Compares the performance of two different
    algorithms.
"""
from stopwatch import Stopwatch
from math import sqrt

def count_primes(n):
    """ Generates all the prime numbers from 2 to n - 1.
    n - 1 is the largest potential prime considered.
    """
    timer = Stopwatch()
    timer.start()

    count = 0
    for val in range(2, n):
        root = round(sqrt(val)) + 1
        # Try all potential factors from 2 to the square root of n
        for trial_factor in range(2, root):
            if val % trial_factor == 0:
                break
            else:
                count +=1
    timer.stop()
    print('Count =', count, 'Elapsed time: ', timer.elapsed(), 'seconds')

def sieve(n):

    """ Generates all the prime numbers from 2 to n - 1.
        n - 1 is the largest potential prime considered.
        Algorithm originally developed by Eratosthenes.
    """
    timer = Stopwatch()
    # Record start time
    timer.start()

    # Each position in the Boolean list indicates
    # if the number of that position is not prime:
    # false means "prime," and true means "composite."
    # Initially all numbers are prime until proven otherwise

    nonprimes = n * [False]

    count = 0

    nonprimes[0] = nonprimes[1] = True

    # Start at the first prime number, 2.
    for i in range(2, n):
        if not nonprimes[i]:
            count += 1

            for j in range(2*i, n, i):
                nonprimes[j] = True
    timer.slop()
    print('Count =', count, 'Elapsed time', timer.elapsed(), 'seconds')

def main():
    count_primes(2000000)
    sieve(2000000)

main()
