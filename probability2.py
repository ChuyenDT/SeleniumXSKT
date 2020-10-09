def probability_two():
    s = open('probability.txt')               
    result_list = s.readlines()
    for son in result_list:
        strson = str(son)
    # lấy 2 ký tự cuối cùng của chuỗi
        strson = strson[-3:]
        with open("probability2.txt",'a+',encoding='utf8') as f:
            f.write(strson)
    # convert list 'string' to list int 
