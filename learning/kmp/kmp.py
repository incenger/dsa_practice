def prefix_function_naive(s):
    n = len(s)

    prefix= [0] * n
    for i in range(len(s)):
        for j in range(i + 1):
            if s[:j] == s[i - j + 1 : i + 1]:
                prefix[i] = j

    return prefix


def prefix_function_On2(s):
    """
    The first optimization: prefix[i+1] <= prefix[i] + 1
    """
    n = len(s)
    prefix = [0] * n
    for i in range(len(s)):
        upper_bound = prefix[i - 1] + 1 if i > 0 else 0
        for j in range(upper_bound, -1, -1):
            if s[:j] == s[i - j + 1 : i + 1]:
                prefix[i] = j
                break

    return prefix


def prefix_function_On(s):
    """
    The second optimization
    """
    n = len(s)
    prefix = [0] * n

    for i in range(1, n):
        j = prefix[i - 1]

        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]

        if s[i] == s[j]:
            # Found a candidate
            # The new prefix is s[0...j-1] + s[j]
            prefix[i] = j + 1

    return prefix


def kmp_concatenation(pattern, text):
    P = len(pattern)
    s = pattern + "#" + text
    prefix = prefix_function_On(s)
    match_start_pos = []

    for i in range(P + 1, len(s)):
        if prefix[i] == P:
            match_start_pos.append(i - 2 * P)

    return match_start_pos


def kmp_two_pointers(pattern, text):
    P, T = len(pattern), len(text)
    prefix = prefix_function_On(pattern)
    i, j = 0, 0

    match_start_pos = []

    while i < T:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == P:
            match_start_pos.append(i - j)
            j = prefix[j - 1]
        elif i < T and text[i] != pattern[j]:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    return match_start_pos


if __name__ == "__main__":
    s = "abcabcd"
    print(prefix_function_On(s))
