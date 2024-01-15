#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation_mapping = {}

        for citation in citations:
            if citation not in citation_mapping:
                citation_mapping[citation] = 1
            else:
                citation_mapping[citation] += 1

        min_count = 0
        for citation in reversed(sorted(citation_mapping.keys())):
            min_count += citation_mapping[citation]
            if min_count >= citation:
                return max(min_count - citation_mapping[citation], citation)

        return len(citations)


# @lc code=end
