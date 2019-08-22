class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = len(matrix)
        w = len(matrix[0])


        List = []

        min_i = 0
        max_i = l-1
        min_j = 0
        max_j = w-1



        while(1):

            i = min_i  # index within rows
            j = min_j  # index with columns

            # first line

            while min_j <= j <= max_j and min_j <= i <= max_i:

                List.append(matrix[i][j])
                j += 1

            min_i += 1
            i = min_i
            j = max_j

            # second line
            while min_j <= j <= max_j and min_j <= i <= max_i:
                List.append(matrix[i][j])
                i += 1

            max_j -= 1
            i = max_i
            j = max_j

            # third line

            while  min_j <= j <= max_j and min_j <= i <= max_i:
                List.append(matrix[i][j])
                j -= 1

            max_i -= 1
            i = max_i
            j = min_j

            while  min_j <= j <= max_j and min_j <= i <= max_i:
                List.append(matrix[i][j])
                i -= 1

            min_j += 1


            if len(List) == l*w:
                break


        return List


sol = Solution()
a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

b =   [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
      ]

print(b)
print(sol.spiralOrder(b))
















