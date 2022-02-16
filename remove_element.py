#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [-1,0,0,0,0,3,3]
list = []
count = 0
for item in nums:
    if (list.__contains__(item) == False):
        list.append(item)
for item in list:
    nums[count] = item
    count += 1

print(count)
print(nums)