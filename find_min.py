def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if min_num > num:
            min_num = num
    return min_num


def main():
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56


if __name__ == "__main__":
    main()
