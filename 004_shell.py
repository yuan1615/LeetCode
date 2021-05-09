# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 16:38
# @Author  : Xin

'''
希尔排序：
改进的插入排序
利用gap(间隔进行了改进)
'''


class Solution(object):
    def insertion(self, nums):
        # nums = [9, 6, 1, 3, 5]
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] > nums[j - 1]:
                    break
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]

    def insertion_gap_time(self, nums, nums_ind_i):
        for j in range(1, len(nums_ind_i)):
            for k in range(j, 0, -1):
                if nums[nums_ind_i[k]] > nums[nums_ind_i[k - 1]]:
                    break
                if nums[nums_ind_i[k]] < nums[nums_ind_i[k - 1]]:
                    nums[nums_ind_i[k]], nums[nums_ind_i[k - 1]] = nums[nums_ind_i[k - 1]], nums[nums_ind_i[k]]

    def shell(self, nums, gaps=[4, 2]):
        # nums = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]
        # 先循环每一个gap

        for gap in gaps:
            times = len(nums) // gap
            # 保持余数
            remain = len(nums) % gap
            for i in range(times):
                nums_ind_i = [i * gap for i in list(range(gap))]
                nums_ind_i = [j + i for j in nums_ind_i]
                # 对nums_ind_i位置的元素进行插入排序
                self.insertion_gap_time(nums, nums_ind_i)
            # 对余数进行插入排序
            nums_ind_i = [i * gap for i in list(range(gap))]
            nums_ind_i = [j + times for j in nums_ind_i]
            nums_ind_i = nums_ind_i[:remain]
            self.insertion_gap_time(nums, nums_ind_i)
            print('gap=%d的输出结果是' % gap, nums)
        # 循环为gaps之后再做简单排序
        self.insertion(nums)
        print('最终输出结果为', nums)


# 上面利用了中间变量nums_ind_i来存储每一个gap需要排序的值了，其实不用这样，多占用了内存空间了！

class Solution2(object):
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def shell(self, nums):
        gap = 4
        while gap >= 1:
            for i in range(gap, len(nums)):
                for j in range(i, i % gap, -gap):
                    if nums[j] > nums[j - gap]:
                        break
                    elif nums[j] < nums[j - gap]:
                        self.swap(nums, j, j - gap)
            print('gap=%d的输出结果是' % gap, nums)
            gap = int(gap/2)


if __name__ == '__main__':
    # solution = Solution()
    # nums = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]
    # solution.shell(nums)
    solution = Solution2()
    nums = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]
    solution.shell(nums)
