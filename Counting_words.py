#write a pyhton program that counts and returns the number of words in a given text
string =input('enter string: ')
ch = 0
wrd = 1
for i in string:
    ch = ch+1
    if(i == ' '):
        wrd = wrd+1
print('number of character appear in this string are :', ch)
print('number of word appear in this string are :', wrd)