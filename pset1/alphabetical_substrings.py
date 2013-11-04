s = "azcbobobegghakl"
max_start = 0
max_end = 0

start = 0
while start < len(s):
    end = start + 1
    while end < len(s) and s[end-1] <= s[end]:
        end += 1

    if max_end - max_start < end - start:
        max_end = end
        max_start = start

    start = end

print "Longest substring in alphabetical order is:", s[max_start:max_end]
