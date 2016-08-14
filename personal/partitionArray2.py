#!/usr/bin/python
#O(n)time,O(1)space
class Solution:
	"""
	@param nums: The integer array you should partition
	@param k: As description
	@return: The index after partition
	"""
	def partitionArray2(self, nums):
		i,j=0,len(nums)-1
		while i<=j:
			while i<=j and nums[i]<0:
				i+=1
			while i<=j and nums[j]>=0:
				j-=1
			if i<=j:
				nums[i],nums[j]=nums[j],nums[i]
				i+=1
				j-=1
		return nums
			
s = Solution()		
numbers=[1,-2,3,-1,2,-3]
print s.partitionArray2(numbers)

