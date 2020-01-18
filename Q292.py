"""
Q292
Nim Game
Easy

:brain teaser:

You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of
you take turns to remove 1 TO 3 stones. The one who removes
the last stone will be the winner. You will take the first
turn to remove the stones.

Both of you are very clever and have optimal strategies
for the game. Write a function to determine whether you
can win the game given the number of stones in the heap.

notes:
math induction
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
