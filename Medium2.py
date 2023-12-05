def find_majority_elements(nums):
    count_first, count_second = 0, 0
    candidate_first, candidate_second = None, None
    for num in nums:
        if candidate_first is not None and num == candidate_first:
            count_first += 1
        elif candidate_second is not None and num == candidate_second:
            count_second += 1
        elif count_first == 0:
            candidate_first, count_first = num, 1
        elif count_second == 0:
            candidate_second, count_second = num, 1
        else:
            count_first -= 1
            count_second -= 1
    count_first, count_second = 0, 0
    for num in nums:
        if num == candidate_first:
            count_first += 1
        elif num == candidate_second:
            count_second += 1

    result = []
    if count_first > len(nums) // 3:
        result.append(candidate_first)
    if count_second > len(nums) // 3:
        result.append(candidate_second)

    return result
nums = [3, 2, 3]
output = find_majority_elements(nums)
print(output)
