soon_case_param = [1,2,3,4,5]
tmp = soon_case_param
soon_case_param[0] = 55
print(tmp)

soon_case_param = [1,2,3,4,5]
tmp = soon_case_param[:]
soon_case_param[0] = 55
print(tmp)
