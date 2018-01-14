'Goal: From a list print out elements that are less than 5'


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print i

        
b = []
for i in a:
    if i < 5:
        b.append(i)

print b

c = [i for i in a if i < 5]
print c


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = set()

if len(a) > len(b):
    length = len(a)
else:
    length = len(b)

for i in b:
    if i in a:
        c.add(i)

print c


c = set([i for i in a if i in b])

print c

def palindrome(string):
    rev_str = string[::-1]
    if rev_str == string:
        print 'Palindrome'
    else:
        print 'Not a Palindrome'
        
if __name__ == '__main__':

    palindrome('nitin')
    palindrome('chetan')

