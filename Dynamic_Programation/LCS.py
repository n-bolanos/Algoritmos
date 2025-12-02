"""
By: Nicolas Andrés Bolaños Fernandez / nov-2025
This file contains a function that uses dynamic programation to improve 
its performance in contrast to brute force code.
"""

def LCS_lenght(x, y, m, n):
    """This function determines the lenght of the longest common sequence among two same-sized strings.
    Inputs:
        x (str): String to compare
        y (str): String to compare
        m (int): length of x
        """
    b = [["" for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i] == y[i]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"

    return b, c