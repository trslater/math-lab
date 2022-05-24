"""Number of Subsets [1, n] w/ Sums Divisible by k

This is a generalization of a problem discussed in ["The unreasonable
effectiveness of complex numbers in discrete math"](
    https://www.youtube.com/watch?v=bOXCLR3Wric&t=23s), a 3Blue1Brown video.

**WARNING**: Running time explodes for even fairly small n
"""


from itertools import chain, combinations
import sys


def main():
    n, k = map(int, sys.argv[1:3])

    s = set(range(1, n + 1))

    p = powerset(s)

    print(sum(1 for ss in p if sum(ss) % k == 0))


def powerset(s: set) -> set:
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


if __name__ == "__main__":
    main()
