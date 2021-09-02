# import re
# count =0
# matcher=re.finditer('ab','ababababababas')
# for match in matcher:
#     count+=1
# print("count is ",count)


import re
count =0
matcher=re.finditer('ab','ababababababas')
for match in matcher:
    print("matcg available at",match.start())
    print("group",match.group())
    count+=1
print("count is ",count)