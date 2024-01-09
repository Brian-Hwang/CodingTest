def get_test_cases():
    with open("test_cases2.txt", "r") as file:
        test_cases = file.read().splitlines()
        test_case_num = test_cases[0]

    return test_case_num, test_cases


def min_sacrifice(triples):
    n = len(triples)
    INF = float("inf")
    dp = [[[INF for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        a, b, c = triples[i - 1]
        for j in range(2):
            for k in range(2):
                dp[i][1][k] = min(dp[i][1][k], dp[i - 1][j][k] + b + c)
                dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][k] + a + c)
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k] + a + b)

    return min(dp[n][1][1], dp[n][1][0] + triples[-1][1], dp[n][0][1] + triples[-1][0])


if __name__ == "__main__":
    test_case_num, test_cases = get_test_cases()
    test_case_line = 1
    for i in range(1, int(test_case_num) + 1):
        agent_num = int(test_cases[test_case_line])
        test_case_line += 1

        if agent_num < 3:
            print(f"#{i} -1")
            test_case_line += agent_num
            continue

        triples = []
        for j in range(agent_num):
            him, ji, minchup = map(int, test_cases[test_case_line].split())
            test_case_line += 1
            triples.append((him, ji, minchup))

        sacrifice = min_sacrifice(triples)
        print(f"#{i} {sacrifice}")
