"""
Q1025
Divisor Game
Easy

:Dynamic Programming:

Alice and Bob take turns playing a game, with Alice starting
first.

Initially, there is a number N on the chalkboard.  On each
player's turn, that player makes a move consisting of:

* Choosing any x with 0 < x < N and N % x == 0.
* Replacing the number N on the chalkboard with N - x.
* Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both
players play optimally.

"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        hist = {1: False, 2: True}

        def dp(n: int):
            if n in hist:
                return hist[n]
            else:
                for i in range(1, n):
                    if not (n%i) and dp(i):
                        hist[i] = True
                        return True
                return False

        return dp(N)

sol = Solution()
print(sol.divisorGame(11))

for i in range(0, 100):
    print(i, ": ", sol.divisorGame(i))





