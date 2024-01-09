#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        connection = {}
        variables = set()
        answer = []

        for i, (alpha, beta) in enumerate(equations):
            if alpha not in connection:
                connection[alpha] = [[beta, values[i]]]
            else:
                connection[alpha].append([beta, values[i]])
            if beta not in connection:
                connection[beta] = [[alpha, 1 / values[i]]]
            else:
                connection[beta].append([alpha, 1 / values[i]])

            if alpha not in variables:
                variables.add(alpha)
            if beta not in variables:
                variables.add(beta)

        # def dfs(alpha, beta, visited):
        #     visited.add(alpha)

        #     for neighbor, mult in connection[alpha]:
        #         if neighbor not in visited:
        #             if neighbor == beta:
        #                 return mult
        #             times *= mult * dfs(neighbor, beta, visited)

        #     return times

        def dfs(alpha, beta, visited):
            visited.add(alpha)

            for neighbor, mult in connection[alpha]:
                if neighbor == beta:
                    return mult
                if neighbor not in visited:
                    result = dfs(neighbor, beta, visited)
                    if result != -1:
                        return mult * result

            return -1

        for alpha, beta in queries:
            if alpha not in variables or beta not in variables:
                answer.append(-1.0)
            elif alpha == beta:
                answer.append(1.0)
            else:
                answer.append(dfs(alpha, beta, set()))

        return answer


# @lc code=end
