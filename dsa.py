# 1. Left Rotate the Array by One
# nums = [1, 2, 3, 4, 5, 6]
# n = len(nums)
# for i in range(n - 1):
#     nums[i], nums[i + 1] = nums[i +1 ], nums[i]
# print(nums)

# 2. Left Rotate Array by K Places
# nums = [1, 2, 3, 4, 5, 6]
# n = len(nums)
# k = 2
# k = k % n
# for i in range(k):
#     for i in range(n - 1):
#         nums[i], nums[i + 1] = nums[i +1 ], nums[i]
# print(nums)

# 3. Right Rotate the Array by One
# nums = [1, 2, 3, 4, 5, 6]
# n = len(nums)
# for i in range(n - 1, 0, -1):
#     nums[i], nums[i - 1] = nums[i - 1], nums[i]
# print(nums)

# 4. Right Rotate Array by K Places
# nums = [1, 2, 3, 4, 5, 6]
# n = len(nums)
# k = 2
# k = k % n
# for j in range(k):
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[i - 1] = nums[i - 1], nums[i]
# print(nums)

# 5. Move Zeros to End
# nums = [0, 1, 4, 0, 5, 2]
# n = len(nums)
# j = 0
# for i in range(n):
#     if nums[i] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         j += 1
# print(nums)

# 6. Largest Element
# nums = [3, 3, 6, 1]
# max = nums[0]
# n = len(nums)
# for i in range(1, n):
#     if nums[i] > max:
#        max = nums[i]
# print("The Max number is:", max)

# 7. Second Largest Element
# nums = [8, 8, 7, 6, 5]
# largest = -1
# second_largest = -1
# for num in nums:
#     if num > largest:
#        second_largest = largest
#        largest = num
#     elif num > second_largest and num != largest:
#          second_largest = num
# print("Largest Number is:", largest)
# print("Second Largest Number is:", second_largest)

#  8. Linear Search 
# nums = [2, -4, 4, 0, 10]
# target = 6
# n = len(nums)
# count = 0
# for i in range(n):
#     if nums[i] == target and count == 0:
#        print(i)
#        count += 1
# if count == 0:
#     print(-1)

# 9. Union of two sorted arrays
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 7]
# union = []
# for num in nums1:
#     if num not in union:
#         union = union + [num]
# for num in nums2:
#     if num not in union:
#         union = union + [num]
# print(union)

# 10. Find missing number
# nums = [0, 2, 3, 1, 4]
# n = len(nums)
# expected_sum = 0
# for i in range(n + 1):
#     expected_sum += i
# actual_sum = 0
# for num in nums:
#     actual_sum += num
# missing = expected_sum - actual_sum
# print(missing)

# 11. Maximum Consecutive Ones
# nums = [1, 1, 0, 0, 1, 1, 1, 0]
# max_count = 0
# count = 0 
# for i in range(len(nums)):
#     if nums[i] == 1:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count) 

# 12. Single Number - I 
# nums = [1, 3, 10, 3, 5, 1, 5]
# single_element = 0
# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#            count += 1
#     if count == 1:
#        single_element = nums[i]
# print(single_element)

# 13. Longest subarray with sum K
# nums = [10, 5, 2, 7, 1, 9]
# k = 15
# sum = 0
# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if nums[i]+nums[j] == k:
#            count += 1
        
# 14. Two Sum
# nums = [1, 6, 2, 10, 3]
# target = 7
# n = len(nums)
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == target:
#            print(i, j) 

# 15. Sort an array of 0's 1's and 2's
# nums = [1, 0, 2, 1, 0]
# n = len(nums)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if nums[j] > nums[j + 1]:
#            nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

# 16. Majority Element-I (Boyer–Moore Voting Algorithm)
# nums =  [7, 0, 0, 1, 7, 7, 2, 7, 7]
# count = 0
# majority_element = 0
# for num in nums:
#     if count == 0:
#        majority_element = num
#     if num == majority_element:
#        count += 1
#     else:
#         count -= 1
# print(majority_element)

# 17. Kadane's Algorithm (Negative sum decreases future total ❌, Positive sum increases future total ✅)
# nums = [-2, -3, -7, -2, -10, -4]
# max_sum = nums[0]
# curr_sum = nums[0]
# n = len(nums)
# for i in range(1, n) :
#     if curr_sum + nums[i] > nums[i]: 
#        curr_sum = curr_sum + nums[i]
#     else:
#         curr_sum = nums[i]
#     if curr_sum > max_sum :
#         max_sum = curr_sum
# print(max_sum)

# 18. Best time to buy and sell stock
# arr =  [3, 8, 1, 4, 6, 2]
# min_price = arr[0]
# max_profit = 0
# n = len(arr)
# for price in arr:
#     if price < min_price:
#        min_price = price
#     profit = price - min_price
#     if profit > max_profit:
#        max_profit = profit
# print(max_profit)

#  19. Rearrange array elements by sign
# nums = [2, 4, 5, -1, -3, -4]
# n = len(nums)
# result = [0] * n
# posIndex = 0
# negIndex = 1
# for num in nums:
#     if num > 0:
#        result[posIndex] = num
#        posIndex += 2
#     else:
#         result[negIndex] = num
#         negIndex += 2
# print(result)

# 20. Next Permutation
# nums = [1,2,3]
# n = len(nums)
# for i in range(n):
#     if nums[i] < nums[i + 1]:

# 21. check if array is sorted and rotated
# nums = [3,4,5,1,2]
# n = len(nums)
# count = 0
# for i in range(1, n):
#     # if nums[i] < nums[i-1]:  (we found a break in the sorted order. Increment count.)
#        count += 1
# # if nums[n - 1] > nums[0]:  (it counts as a break because the "end" of the sorted chain cannot logically connect back to the "start.")
#    count += 1
# # if count <= 1:  (the array is a valid sorted and rotated array.)
#    for i in range(n):
#        for j in range(0, n-i-1):
#            if nums[j] > nums[j+1]:
#               nums[j], nums[j+1] = nums[j+1], nums[j] 
# print("The sorted and rotated element is:", nums)

# 21. Array Search or Linear Search
# arr = [1, 2, 3, 4]
# x = 3
# n = len(arr)
# for i in range(n):
#     if arr[i] == x:
#        print("Element found at index:", i)   
#     else:
#         print("Element not found")

# 22. Rotate Array
# nums = [1,2,3,4,5,6,7]
# n = len(nums)
# k = 3
# k = k % n
# for j in range(k):
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[i - 1] = nums[i - 1], nums[i]
# print(nums)

# 23. Remove Duplicates from Sorted Array
# nums = [1,1,2]
# n = len(nums)
# i = 0
# for j in range(1, n):
#     if nums[j] != nums[i]:
#        i += 1
#        nums[i] = nums[j]
# print(i + 1)

# 24. Max Consecutive Ones
# nums = [1,1,0,1,1,1]
# max_count = 0
# count = 0
# for num in nums:
#     if num == 1:
#        count += 1
#     else:
#         count = 0
#     if count > max_count:
#        max_count =count 
# print(max_count)

# 25.Rotate Array
# nums = [1,2,3,4,5,6,7]
# n = len(nums)
# k = 3
# k = k % n
# for j in range(k):
#     if j < k:
#        for i in range(n - 1, 0, -1):
#            nums[i], nums[i - 1] = nums[i - 1], nums[i]
# print(nums)

#
# 
# 
# x=int(input()) 

# nums = [2, 3, 1, 4]
# n = len(nums)
# for i in range(0, n + 1):
#     if i not in nums:
#        print(i)

# Plus One
digits = [1,2,3]
n = len(digits)
for i in range(n-1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        print(digits)
        break
        digits[i] = 0
else:
    digits = [1] + digits
    print(digits)



print("Hemanath Rapelli")