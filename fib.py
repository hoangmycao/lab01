'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    pass


def main():
    n=int(input("Enter the length of Fibonacci numbers: "))
    print(produceFibsList(n))

def produceFibsList(n):
    i = 0
    for i in range(n):
        if (n<=1):
            return n
        else:
            produceFibsList[i]=(produceFibsList[i-1]+produceFibsList[i-2])
            return produceFibsList[i]
            i=+1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
pass