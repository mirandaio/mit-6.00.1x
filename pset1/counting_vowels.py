s = "azcbobobegghakl"
count = 0

for c in s:
    if c in "aeiou":
        count += 1

print "Number of vowels: " + str(count)
