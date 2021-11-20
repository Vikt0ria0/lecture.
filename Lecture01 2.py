s = input()
t = s.lower()

for i in range(len(s)):
    b = t.count(t[i])
    print("{} -- {}".format(s[i], b))
    
