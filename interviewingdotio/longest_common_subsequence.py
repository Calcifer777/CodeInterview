# Given two strings s1 and s2, return the longest common subsequence of s1 and s2
# (with longest common subsequence defined as the longest sequence of characters such
# that all of them appear in both of the strings, possibly with other characters in between)


def longest_common_subsequence(s1, s2):

    if len(s1)*len(s2) == 0:
        return ''

    if s1[0] == s2[0]:
        lngst_subseq = s1[0] + longest_common_subsequence(s1[1:], s2[1:])
    else:
        lngst_subseq = longest_common_subsequence(s1, s2[1:])

    result = max(
        lngst_subseq,
        longest_common_subsequence(s1[1:], s2),
        key=len)
    return result


if __name__ == '__main__':
    tests = [
        [('aaaa', 'aa'), 'aa'],
        [('', '..'), ''],
        [('AGGTAB', 'GXTXAYB'), 'GTAB'],
        [('ABAZDC', 'BACBAD'), 'ABAD'],
        [('ABBA', 'ABCABA'), 'ABBA'],
    ]
    for test in tests:
        print(
            "\ns1: ", test[0][0],
            "\ns2: ", test[0][1],
            "\nexpected: ", test[1],
            "\nactual: ", longest_common_subsequence(*test[0]),
            "\n",
        )
