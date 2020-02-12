"""
Q819
Easy
Most Common Word

Given a paragraph and a list of banned words, return the most
frequent word that is not in the list of banned words.  It is
guaranteed there is at least one word that isn't banned, and
that the answer is unique.

Words in the list of banned words are given in lowercase, and
free of punctuation.  Words in the paragraph are not case
sensitive.  The answer is in lowercase.

Note:

- 1 <= paragraph.length <= 1000.
- 0 <= banned.length <= 100.
- 1 <= banned[i].length <= 10.
- The answer is unique, and written in lowercase (even if its
  occurrences in paragraph may have uppercase symbols, and
  even if it is a proper noun.)
- paragraph only consists of letters, spaces, or the punctuation
  symbols !?',;.
- There are no hyphens or hyphenated words.
- Words only consist of letters, never apostrophes or other
  punctuation symbols.
"""

from typing import List

class Solution:
    def mostCommonWord(self,
                       paragraph: str,
                       banned: List[str]) -> str:






