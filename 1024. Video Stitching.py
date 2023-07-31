# Chronological Ordering
# Time: O(nlogn)
# Space: O(n)
# 2023.07.29: no

class Solution(object):
    def videoStitching(self, clips, T):
        if T == 0:
            return 0

        # Sort clips by starting point in ascending order and by ending point in descending order
        clips.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        curEnd, nextEnd = 0, 0
        i, n = 0, len(clips)

        while i < n and clips[i][0] <= curEnd:
            # Greedily choose the next clip within the interval of the current res-th video
            while i < n and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1

            # Found the next clip, update curEnd
            res += 1
            curEnd = nextEnd

            if curEnd >= T:
                # Can already cover the interval [0, T]
                return res

        # Unable to continuously cover the interval [0, T]
        return -1

# Tests:
test = Solution()
test.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)