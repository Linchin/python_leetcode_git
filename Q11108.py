"""
Q1108
Defanging an IP address
Easy

:string:

Given a valid (IPv4) IP address, return a defanged version
of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

address = "1.1.1.1"
sol = Solution()
print(sol.defangIPaddr(address))
