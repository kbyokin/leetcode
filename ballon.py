# https://leetcode.com/problems/maximum-number-of-balloons/
text = "bbaaannnnllooooo"
lookup_table = {'b', 'a', 'l', 'o', 'n'}
counts = {}
text = list(text)
unqieChar = set(text)
numRuns = 0
# for toChar in lookup_table:
#     # to check there is enough char to form ballon
#     if toChar not in unqieChar:
#         print(0)
#         # return will exit to loop
#     else:
#         for char in text:
#             if char in lookup_table:
#                 counts[char] = counts.get(char, 0) + 1
#         # print(counts)
#         l_n_o, t_rest = min(counts['o'], counts['l']), min(counts['b'], counts['a'], counts['n'])
#         formBal = min(l_n_o, t_rest)
#         print(l_n_o, t_rest)
#         print(formBal)
#         if formBal > 0 and l_n_o >= 2:
#             print(formBal)
#         else:
#             print(0)
    
#     break
for char in text:
    if char in lookup_table:
        counts[char] = counts.get(char, 0) + 1

# l_n_o, t_rest = min(counts['o'], counts['l']), min(counts['b'], counts['a'], counts['n'])
# formBal = min(l_n_o, t_rest)
# print(counts[min(counts, key=counts.get)])
# print(max(counts, key=counts.get))

# for char in lookup_table:
#     print(char)
#     if char not in unqieChar:
#         print(0)
#         break
#     else:
#         l_n_o, t_rest = min(counts['o'], counts['l']), min(counts['b'], counts['a'], counts['n'])
#         formBal = min(l_n_o, t_rest)
#         print(l_n_o%t_rest)
#         print(formBal)
