employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},
]

# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)

#print employee names
# for employe in employees:
#     # "e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1
#     print(employe["e_name"])
#

# for employe in employees:
#     # "e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1
#     print(employe["e_name"].upper())

# e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
# print(e_upper)
#

# for employee in employees:
#     if employee["department"]=="developer":
#         print(employee["e_name"])

develp=filter(lambda emp:emp["department"]=="developer",employees)
print(employees)



# total=0
# total sum of salary
# for employee in employees:
#     total=total+employee["salary"]
# print(total)

# 1 case ---Map
# 2 case with condition--- filter
# 3 case with processing to a single value ---reduce
