| Iteration | i | cardPoints[i] (incoming) | i-ws | cardPoints[i-ws] (outgoing) | current_sum | min_subarray_sum | Current Window |
| --------- | - | ------------------------ | ---- | --------------------------- | ----------- | ---------------- | -------------- |
| Initial   | - | -                        | -    | -                           | 10          | 10               | [1,2,3,4]      |
| 1         | 4 | 5                        | 0    | 1                           | 14          | 10               | [2,3,4,5]      |
| 2         | 5 | 6                        | 1    | 2                           | 18          | 10               | [3,4,5,6]      |
| 3         | 6 | 1                        | 2    | 3                           | 16          | 10               | [4,5,6,1]      |


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)
        n = len(cardPoints)
        if k==n:
            return total_sum
        ws = n-k
        curr_sum = sum(cardPoints[:ws])
        min_array_sum = curr_sum
        for i in range(ws, n):
            curr_sum += cardPoints[i]-cardPoints[i-ws]
            min_array_sum= min(min_array_sum, curr_sum)
        return total_sum-min_array_sum
