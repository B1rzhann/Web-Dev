#1
def first_last6(nums):
  if nums[0]==6 or nums[len(nums)-1]==6:
    return True
  return False

#2
def same_first_last(nums):
  if len(nums)>=1 and nums[0]==nums[len(nums)-1]:
    return True
  return False

#3
def make_pi():
  return [3,1,4]

#4
def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  return False

#5
def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  return False

#6
def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]

#7
def reverse3(nums):
  return [nums[2],nums[1],nums[0]]

#8
def max_end3(nums):
    max_value = max(nums[0], nums[2])
    return [max_value, max_value, max_value]

#9
def sum2(nums):
  if len(nums)>=2:
    return nums[0]+nums[1]
  if len(nums)==1:
    return nums[0]
  return 0

#10
def middle_way(a, b):
  return [a[1],b[1]]

#11
def make_ends(nums):
  return [nums[0],nums[len(nums)-1]]

#12
def has23(nums):
  if nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3:
    return True
  return False