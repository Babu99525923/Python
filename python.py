strs = ["flower","floral"]
prefix = strs[0]
print(prefix[:-2])
temp = ""
for i in range(len(strs)-1):
        for j in range(len(strs[0])):
                if((strs[i][j] == strs[i+1][j] if i+1 < len(strs[0]) else 0)):
                    temp = strs[i][j]
                    print(temp)

