# example_1 easy
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