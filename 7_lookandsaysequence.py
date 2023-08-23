from sys import stdin

def lookAndSequence(n):
	# Write your code here.
    if n == 1:
        return "1"
    s = lookAndSequence(n - 1)
    result = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i == len(s) - 1 or s[i] != s[i + 1]:
            result.append(str(count) + s[i])
            count = 0
    return ''.join(result)

def takeInput() :
	n = int(input().strip())
	return n

t = int(input().strip())
for i in range(t) :
	n = takeInput()
	print(lookAndSequence(n))
