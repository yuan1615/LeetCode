# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 18:50
# @Author  : Xin

# 选择排序算法

#

class Solution(object):
    def selectSort(self, nums):
        # nums = [2, 1, 5, 4, 3, 9, 6, 8, 7]
        for i in range(len(nums)):
            minPos = i
            temp = nums[minPos]
            temp_min_Pos = minPos
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minPos]:
                    minPos = j
            nums[temp_min_Pos] = nums[minPos]
            nums[minPos] = temp
            # print minPos
            print('第%d调换的位置是%d和%d' %(i, temp_min_Pos, minPos))
            # print nums
            print('第{}次调换位置后为：'.format(i + 1), end=' ')
            for k in range(len(nums)):
                print(nums[k], end=' ')
            print()

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 1, 5, 4, 3, 9, 6, 8, 7]
    solution.selectSort(nums)
