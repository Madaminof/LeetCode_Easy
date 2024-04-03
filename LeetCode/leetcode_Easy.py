""""# example_1 easy
def twoSum(self, nums, target):
        self.n = nums
        self.t = target
        for i in range(len(self.n)):
            for j in range(i + 1, len(self.n)):
                if self.n[i] + self.n[j] == self.t:
                    return [i, j]


s = "42 sjdcbjddcs"
a = s.split()

for i in a:
    if i.isdigit():
        print(int(i))

def searchInsert( nums, target):
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# stringdagi eng uzun soz toping
def lengthOfLastWord( s):
        list1=[]
        for i in s.split():
            s1=len(i)
            list1.append(s1)
        return list1[-1]  


def plusOne(digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


# leetCode error: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates_PushBack_(nums):
        s1=set(nums)
        l2=list(s1)
        len1=len(nums)-len(l2)
        for i in range(len1):
            l2.append(("_"))
        return l2
print(removeDuplicates_PushBack_([0,0,1,1,1,2,2,3,3,4]))
"""

"""
s="dabba"   
def solution(s1):
     l=[]
     for i in s1:
        l.append(i)
     dic={}
     for i in l:
        dic[i]=l.count(i)
     return dic    
print(solution(s))   """


  
"""
def RemoveElement(head,val):
    l=[]
    for i in head:
        if i!=val:
            l.append(i)
    return l
print(RemoveElement([1,2,6,3,4,5,6],6))"""



def containsDuplicate(nums):
    c=0
    l1=[]
    result=True
    for i in nums:
        l1.append(nums.count(i))
    for i in l1:
        if i>1:
            c+=1
    if c>=1:
        result= True
    else:
        result=False
    return result    
print(containsDuplicate([1,2,3,4,5,1,3]))    

 





