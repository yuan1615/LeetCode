# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 15:56
# @Author  : Xin

'''
插入排序：
从第二个开始，一直到len（）
一直和前面的数进行比较，如果比前面的小则交换位置

'''

class Solution(object):
    def insertion(self, nums):
        # nums = [9, 6, 1, 3, 5]
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] > nums[j -1]:
                    break
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
            print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [9, 6, 1, 3, 5]
    solution.insertion(nums)
