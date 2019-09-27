'''
思路：从中挑出最大的，然后从最大的左边元素中拿到最左端次大的，中间必然是可以填雨水的，
然后在最左次大的左边再找最左第三大的，次大和第三大中必然也可以填雨水，依次类推知道遍历到最左端；
最大元素的右边计算方式与左边类似，找最右次大、第三大……最后可计算得到总可装填雨水量。
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        max_h = self.getMax(height)
        max_p = height.index(max_h)
        if max_p > 1:
            res_l, max_p_l = self.count(height, 0, max_p)
            if len(height) - max_p > 1:
                res_r, max_p_r = self.count(height, max_p + 1, len(height))
                result = res_l + res_r + self.trap1(height, 0, max_p_l) + self.trap1(height, max_p_r, len(height))
            else:
                result = res_l + self.trap1(height,0, max_p_l)
        elif len(height) - max_p > 1:
            res_r, max_p_r = self.count(height, max_p + 1, len(height))
            result = res_r + self.trap1(height, max_p_r, len(height))
        else:
            result = 0
        return result

    def trap1(self, height, i, j):
        if j - i <= 1 or (j != len(height) and i != 0):
            return 0
        else:
            res, max_p = self.count(height, i, j)
            result = res + self.trap1(height, i, max_p) + self.trap1(height, max_p+1, j)
            return result

    def count(self, height, i, j):
        res = 0
        if i == 0:
            max_h = self.getMax(height[i:j])
            max_p = height.index(max_h)
            for k in height[max_p + 1: j]:
                res += max_h - k
        else:
            max_h = self.getMax(height[i:j])
            max_p = len(height) - height[::-1].index(max_h)-1
            for k in height[i: max_p]:
                res += max_h - k
        return res, max_p

    def getMax(self, height):
        return max(height)

if __name__ == '__main__':
    s = Solution()
    res = s.trap([0,5,6,4,6,1,0,0,2,7])
    print('结果：', res)