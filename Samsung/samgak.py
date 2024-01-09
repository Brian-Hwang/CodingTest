def get_test_cases():
    with open("test_cases.txt", "r") as file:
        test_cases = file.read().splitlines()
        test_case_num = test_cases[0]

    return test_case_num, test_cases


def get_level(samgak):
    upper_limit = int((2 * samgak) ** 0.5) + 1

    low, high = 0, upper_limit

    while low <= high:
        mid = (low + high) // 2
        last_samgak_in_mid_level = mid * (mid + 1) // 2

        if last_samgak_in_mid_level < samgak:
            low = mid + 1
        elif last_samgak_in_mid_level > samgak:
            high = mid - 1
        else:
            return mid - 1
    return high


def get_reachable_samgak(start, start_level, end_level):
    leftmost = start + (end_level - start_level) * (start_level + end_level - 1) // 2
    rightmost = leftmost + (end_level - start_level)
    return leftmost, rightmost


def get_lowest_samgak(test_case):
    start, end = min(int(test_case[0]), int(test_case[1])), max(
        int(test_case[0]), int(test_case[1])
    )
    start_level, end_level = get_level(start) + 1, get_level(end) + 1

    if start_level == end_level:
        return end - start

    leftmost, rightmost = get_reachable_samgak(start, start_level, end_level)

    samgak = end_level - start_level
    if leftmost <= end <= rightmost:
        return samgak

    if end < leftmost:
        return samgak + leftmost - end
    else:
        return samgak + end - rightmost


if __name__ == "__main__":
    test_case_num, test_cases = get_test_cases()
    # Can I use cache?
    for i in range(1, int(test_case_num) + 1):
        samgak = get_lowest_samgak(test_cases[i].split())
        print(f"#{i} {samgak}")
