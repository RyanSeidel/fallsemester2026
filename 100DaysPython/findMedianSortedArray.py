from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         
         newArray = []

         p1, p2 = 0, 0

         while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                newArray.append(nums1[p1])
                p1 += 1
            else:
                newArray.append(nums2[p2])
                p2 += 1

         while p1 < len(nums1):
            newArray.append(nums1[p1])
            p1 += 1

         while p2 < len(nums2):
            newArray.append(nums1[p2])
            p2 += 1

         total_len = len(newArray)

         print(newArray) # This will now print to your console!

         
         if total_len % 2 == 1:
            # Odd length: return the middle element as a float
            return float(newArray[total_len // 2])
         else:
            # Even length: average the two middle elements
            mid = total_len // 2
            return (newArray[mid - 1] + newArray[mid]) / 2.0

# --- Execution block to trigger the print ---
if __name__ == "__main__":
    solution = Solution()
    
    # Wrap the method call in print() to see what it returns
    result = solution.findMedianSortedArrays([1, 3], [2])
    print(result)