"""
Q735
Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a
row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

Note:
* The length of asteroids will be at most 10000.
* Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        temp = asteroids.copy()

        while True:
            L = len(temp)
            next_iter = []
            i = 0
            count = 0
            pos = []           # positive speed
            neg = []          # negative speed
            state = -1
            # -1: begin
            #  0: leftmost neg that can be kept as is
            #  1: a collision interval - pos
            #  2: a collision interval - neg

            while i < L:
                if state == -1 and temp[i] < 0:
                    next_iter.append(temp[i])
                    state = 0
                elif state == -1 and temp[i] > 0:
                    state = 1
                    pos.append(temp[i])

                elif state == 0 and temp[i] < 0:
                    next_iter.append(temp[i])
                elif state == 0 and temp[i] > 0:
                    state = 1
                    pos.append(temp[i])

                elif state == 1 and temp[i] > 0:
                    pos.append(temp[i])
                elif state == 1 and temp[i] < 0:
                    state = 2
                    neg.append(temp[i])

                elif state == 2 and temp[i] < 0:
                    neg.append(temp[i])
                elif state == 2 and temp[i] > 0:
                    state = 1
                    pos_abs = [abs(item) for item in pos]
                    pos_max = max(pos_abs)
                    neg_abs = [abs(item) for item in neg]
                    neg_max = max(neg_abs)
                    if pos_max > neg_max:
                        for item in pos:
                            if item < pos_max:
                                next_iter.append(item)
                            elif item == pos_max:
                                next_iter.append(item)
                                break
                    elif pos_max < neg_max:
                        flag = 0
                        for item in neg:
                            if item > -neg_max and flag == 0:
                                continue
                            elif flag == 0 and item == -neg_max:
                                next_iter.append(item)
                                flag = 1
                            elif flag == 1:
                                next_iter.append(item)
                    else:
                        for item in pos:
                            if item < pos_max:
                                next_iter.append(item)
                            elif item == pos_max:
                                next_iter.append(item)
                                break
                        flag = 0
                        for item in neg:
                            if item > -neg_max and flag == 0:
                                continue
                            elif flag == 0 and item == -neg_max:
                                next_iter.append(item)
                                flag = 1
                            elif flag == 1:
                                next_iter.append(item)

                    pos = [temp[i]]
                    neg = []
                    count += 1

                i += 1

            if state == 2:
                pos_abs = [abs(item) for item in pos]
                pos_max = max(pos_abs)
                neg_abs = [abs(item) for item in neg]
                neg_max = max(neg_abs)
                if pos_max > neg_max:
                    for item in pos:
                            next_iter.append(item)
                    while next_iter[-1] <= neg_max:
                        next_iter.pop()

                elif pos_max < neg_max:
                    flag = 0
                    for item in neg:
                        if item > -neg_max and flag == 0:
                            continue
                        elif flag == 0 and item == -neg_max:
                            next_iter.append(item)
                            flag = 1
                        elif flag == 1:
                            next_iter.append(item)

                else:
                    for item in pos_abs:
                        if item < pos_max:
                            next_iter.append(item)
                        elif item == pos_max:
                            next_iter.append(item)
                            break
                    flag = 0
                    for item in neg:
                        if item > -neg_max and flag == 0:
                            continue
                        elif flag == 0 and item == -neg_max:
                            next_iter.append(item)
                            flag = 1
                        elif flag == 1:
                            next_iter.append(item)

                count += 1

            elif state == 1:
                next_iter.extend(pos)

            if count == 0:
                return next_iter

            temp = next_iter.copy()


sol = Solution()
a = asteroids = [-2,1]
print(sol.asteroidCollision(a))

