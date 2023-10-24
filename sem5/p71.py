def lcs(s1, s2):

  lcs = ""
  lcs_table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      if s1[i - 1] == s2[j - 1]:
        lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
      else:
        lcs_table[i][j] = max(lcs_table[i][j - 1], lcs_table[i - 1][j])

  i = len(s1)
  j = len(s2)
  while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
      lcs = s1[i - 1] + lcs
      i -= 1
      j -= 1
    elif lcs_table[i][j - 1] > lcs_table[i - 1][j]:
      j -= 1
    else:
      i -= 1

  return lcs


def main():
  s1 = "ACCGGTCGAGTG"
  s2 = "GTCGTTCGGAAT"

  LCS = lcs(s1, s2)

  print("The longest common subsequence of the two DNA is:", LCS)


if __name__ == "__main__":
  main()
