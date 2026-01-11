import unittest
def pairs_to_sum(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                pairs.append((i, j))

    if not pairs:
        print("No pairs add up to it")

    print(pairs)

nums = list(map(int, input("Enter list of numbers: ").split()))
target = int(input("Enter target: "))
pairs_to_sum(nums, target)