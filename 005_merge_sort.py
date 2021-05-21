# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 13:57
# @Author  : Xin

'''
归并排序
1.利用了递归的思想
2.解决的问题是如果有两个有序的数组，我们怎么对它排序

利用三个指针，1个等长的空间
'''


class Solution(object):

    def sort(self, nums, left, right):
        if left < right:
            #  分成两半
            mid = int((left + right - 1) / 2)
            #  左边排序
            self.sort(nums, left, mid)
            #  右边排序
            self.sort(nums, mid + 1, right)
            #
            self.mergesort(nums, left, mid, right)

    def mergesort(self, nums, leftPtr, rigthPtr, rightBound):
        '''
        :param nums:
        :param leftPtr:左边位置
        :param rigthPtr:中间位置（记住是第一个结束的位置，而不是第二个开始的位置）
        :param rightBound:右边位置
        :return:
        '''
        result = [None for i in range(rightBound - leftPtr + 1)]
        i = leftPtr
        j = rigthPtr + 1
        k = 0
        while i <= rigthPtr and j < rightBound + 1:
            if nums[i] <= nums[j]:
                result[k] = nums[i]
                k += 1
                i += 1
            else:
                result[k] = nums[j]
                j += 1
                k += 1
        # 判断那个没有加完
        if i <= rigthPtr:
            result[k:] = nums[i:rigthPtr + 1]
        elif j < rightBound + 1:
            result[k:] = nums[j:rightBound + 1]
        nums[leftPtr:(rightBound + 1)] = result
        # print(nums)


if __name__ == "__main__":
    nums = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    solution = Solution()
    solution.sort(nums, 0, len(nums) - 1)
    print(nums)
