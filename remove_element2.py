nums = [0,1,2,2,3,0,4,2]
val = 2
list = []
count = 0
for item in nums:
    if (item != val):
        list.append(item)
for item in list:
    nums[count] = item
    count += 1

print(count)
print(nums)