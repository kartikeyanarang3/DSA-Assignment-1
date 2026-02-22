#recursive binary search function
def binary_search(arr, low, high, target):
  if low>high:
    return -1
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  elif target < arr[mid]:
    return binary_search(arr, low, mid-1, target)
  else:
    return binary_search(arr, mid+1, high, target)
# The Time Complexity is O(log n) because our search space is getting half after every time function is called
# The Space Complexity is O(log n) due to the recursive call stack depth
