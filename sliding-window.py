# Maximum sum subarray of size K

nums: list[int] = [8, 3, -2, 4, 5, -1, 0, 5, 3, 9, -6]
k: int = 5

# Nums will always be at least k elements

def maximum_sum(nums: list[int], k: int) -> int:
    current = 0

    for i in range(k):
        current += nums[i]

    best = current

    for r in range(k, len(nums)):
        current = current + nums[r] - nums[r - k]
        best = max(best, current)

    return best

print(maximum_sum(nums, k))
