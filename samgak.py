def get_test_cases():
    with open("test_cases.txt", "r") as file:
        test_cases = file.read().splitlines()
        test_case_num = test_cases[0]

    return test_case_num, test_cases


def get_lowest_samgak(test_case):
    samgak = 0
    start, end = int(test_case[0]), int(test_case[1])

    return samgak


if __name__ == "__main__":
    test_case_num, test_cases = get_test_cases()

    for i in range(1, int(test_case_num) + 1):
        samgak = get_lowest_samgak(test_cases[i].split())
        print(f"#{i} {samgak}")
