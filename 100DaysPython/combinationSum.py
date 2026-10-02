from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Write your recursive/backtracking logic here

        combinations = []

        self.dfs(candidates, target, [], combinations)

        return combinations

    def dfs(self, nums, target, path, combinations):
        if target < 0:
            return

        if target == 0: 
            combinations.append(path)

        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], combinations)


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(f"Test 1 Output: {sol.combinationSum(candidates1, target1)}")
    
    # Test Case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    print(f"Test 2 Output: {sol.combinationSum(candidates2, target2)}")
    
    # Test Case 3
    candidates3 = [2]
    target3 = 1
    print(f"Test 3 Output: {sol.combinationSum(candidates3, target3)}")