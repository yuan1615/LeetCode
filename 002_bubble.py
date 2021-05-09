# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 14:40
# @Author  : Xin

'''
冒泡排序：
从第一个数开始，两两比价，大的数放到最后面，重复执行
'''

class Solution(object):
    def bubble(self, nums):
        # nums = [9, 6, 1, 3, 5]
        for j in range(len(nums) - 1):
            for i in range(len(nums) - 1 - j):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [9, 6, 1, 3, 5]
    solution.bubble(nums)
