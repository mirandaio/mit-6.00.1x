s = "azcbobobegghakl"
start = 0
end = 0
temp_start = 0

for i in range(1, len(s)):
    if s[i-1] > s[i]:
        temp_start = i
        
    if i - temp_start > end - start:
        start = temp_start
        end = i
                                            
print 'Longest substring in alphabetical order is:', s[start:end+1]
