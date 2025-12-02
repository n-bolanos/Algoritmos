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
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "D"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "A"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "I"

    return b, c

cadena1 = input()
cadena2 = input()

b, c = LCS_lenght(cadena1, cadena2, len(cadena1), len(cadena2))

for i in range(1, len(cadena1)+1):
    print(*b[i][1:], sep="\t")

print()

for i in range(1, len(cadena1)+1):
    print(*c[i][1:], sep="\t")
