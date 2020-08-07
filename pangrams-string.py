# Pangram is when a string contains all letters from the alphabet


# abc = "abcdefghijklmnopqrstuvwxyz"
# str1 = "abcdefghijklmnopqrstuvwxz"
# l_abc = list(abc)
# l_str1 = list(str1)
# all([True if x in str1 else False for x in l_abc])


def pangrams(s):
    str1 = s.lower()
    abc = list("abcdefghijklmnopqrstuvwxyz")
    res = all([True if x in str1 else False for x in abc])
    if res == True:
        return "pangram"
    else:
        return "not pangram"

# s1 = "The quick brown fox jumps over the lazy dog"
s1 = "We promptly judged antique ivory buckles for the next prize"

print(pangrams(s1))