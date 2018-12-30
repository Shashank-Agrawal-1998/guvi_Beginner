s = input()
vowel = 0
l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(s)):
    if s[i] in l:
        vowel = 1
        break
if vowel == 1:
    print('yes')
else:
    print('no')