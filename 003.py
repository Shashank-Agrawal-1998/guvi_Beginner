c = input()
if (len(c)==1) and ((65<=ord(c)<=90) or (97<=ord(c)<=122)):
    if c=='a' or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U':
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')