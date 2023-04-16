
def fibrec(nth, nums, rStr):
    if nth == 0:
        return (0, rStr)
    
    if nth == 1:
        return (1, rStr)
    
    if nth in nums:
        return (nums[nth], rStr)
    
    mem1, mem2 = fibrec(nth-2, nums, rStr), fibrec(nth-1, nums, rStr)

    mem = mem1[0] + mem2[0]
    rStr += f"{mem1[1]}{mem2[1]}"

    rStr += f'{str(mem)} ' 
    nums[nth] = mem
    return ( mem, rStr )

nums = {}
rStr = ''
result, finalStr = fibrec(12, nums, rStr)
print (f"result: {result}")
print(finalStr)
print(nums.keys())
print('rStr: ' + rStr)

# mem = []
# for elem in nums:
#     if elem in mem:
#         continue
#     else:
#         res = fibrec(elem) + fibrec(elem-1)
#         mem.append(res)