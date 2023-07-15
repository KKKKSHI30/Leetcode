# DFS Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.13: yes
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(image, sr, sc, color):
            if image[sr][sc] == original_color:
                image[sr][sc] = color
                for i in range(len(offsets)):
                    nr, nc = sr + offsets[i][0], sc + offsets[i][1]
                    if nr >= row or nr < 0 or nc >= col or nc < 0:
                        continue
                    else:
                        dfs(image, nr, nc, color)
        if image == [[]] or image == []:
            return image
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color != color:
            dfs(image, sr, sc, color)
        return image

# Tests:
test = Solution()
test.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)