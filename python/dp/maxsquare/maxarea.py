def maximal_square(land):
    """
    Problem:
    Given a binary matrix where:
        1 -> good land
        0 -> bad land
    Find the area of the largest square consisting only of 1s.

    Example:
    land = [
        [0,1,1,0,1],
        [1,1,0,1,0],
        [0,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
    ]
    Output: 9   # (largest 3x3 square)

    Approach:
    - dp[i][j] = side length of largest square ending at (i, j)
    - If land[i][j] == 1:
          dp[i][j] = 1 + min(top, left, diagonal)
      else:
          dp[i][j] = 0

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """

    if not land or not land[0]:
        return 0  # edge case: empty matrix

    rows = len(land)
    cols = len(land[0])

    # DP grid storing largest square side ending at each cell
    dp = [[0] * cols for _ in range(rows)]

    max_side = 0  # track largest square side found

    for i in range(rows):
        for j in range(cols):

            if land[i][j] == 1:  # only process if good land

                if i == 0 or j == 0:
                    dp[i][j] = 1  # border cells can only form 1x1

                else:
                    # grow square based on smallest supporting neighbor
                    dp[i][j] = 1 + min(
                        dp[i-1][j],     # top
                        dp[i][j-1],     # left
                        dp[i-1][j-1]    # diagonal
                    )

                max_side = max(max_side, dp[i][j])  # update max

    return max_side * max_side  # return area


# ---- Example Run ----
if __name__ == "__main__":

    land = [
        [0,1,1,0,1],
        [1,1,0,1,0],
        [0,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
    ]

    result = maximal_square(land)  # compute max square area
    print("Maximum square area:", result)  # Expected output: 9
    