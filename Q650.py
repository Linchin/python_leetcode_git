"""
Q650
2 Keys Keyboard
Medium

Initially on a notepad only one character 'A' is present.
You can perform two operations on this notepad for each
step:

Copy All: You can copy all the characters present on the
notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last
time.


Given a number n. You have to get exactly n 'A' on the
notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.

"""


class Solution:
    def minSteps(self, n: int) -> int:
