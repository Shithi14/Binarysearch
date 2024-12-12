class Solution:
    def binarysearch(self, arr, k):
        # Binary Search function to find the smallest index of 'k' in the sorted array 'arr'
        n = len(arr)
        left = 0
        right = n - 1
        search = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == k:
                search = mid  # 'k' found, store index
                right = mid - 1  # Continue searching in the left part of the array
            
            elif arr[mid] < k:
                left = mid + 1  # Search in the right part
            else:
                right = mid - 1  # Search in the left part
        
        return search  # Return the smallest index of 'k' or -1 if not found


# Driver Code
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        k = int(input())  # Element to search for
        arr = list(map(int, input().split()))  # Sorted array
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)  # Output the index of 'k' or -1 if not found
        print("~")
