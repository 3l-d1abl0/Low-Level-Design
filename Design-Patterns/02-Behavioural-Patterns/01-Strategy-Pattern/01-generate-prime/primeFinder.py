'''
    Define a family of algorithms, encapsulate each one, and
    make them interchangable. Strategy lets the algorithm vary
    independently from the client that use it.

    Open Closed Principle
'''

class PrimeFinder(object):
    """docstring for PrimeFinder."""
    def __init__(self):
        self.primes = []

    def calculate(self, limit):
        """Will calculate all the primes below a limit. """
        pass
    def out(self):
        """Prints the list of primes """
        print(self.__class__.__name__)
        for prime in self.primes:
            print(prime)


class HardCodedPrimeFinder(PrimeFinder):

    def calculate(self, limit):
        hardcoded_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        primes = []
        for prime in hardcoded_primes:
            if prime<limit:
                self.primes.append(prime)

class StandardPrimeFinder(PrimeFinder):

    def calculate(self, limit):
        self.primes = [2]

        for number in range(3, limit, 2):
            is_prime = True
            for prime in self.primes:
                if number%prime ==0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(number)



class PrimeFinderClient:

    def __init__(self, limit):
        self.limit = limit
        if limit <=50:
            self.finder = HardCodedPrimeFinder()
        else:
            self.finder = StandardPrimeFinder()


    def get_primes(self):
        self.finder.calculate(self.limit)
        self.finder.out()
