'''
Lấy từng dòng trong 30day.txt truyển vào từng phần tử trong list, sau đó dùng for duyệt qua từng phần tử
 để thay thế "\n" thành "space", tiếp tục thay thế "space" thành "\n" rồi ghi vào file probability.txt
 Mục đích: Khi ghi vào file probability.txt thì từng số được ghi trên từng dòng, để sau này dùng
 readlines() tuyền từng dòng thành tưng phần tử của list, mối phần tử là mỗi số riêng
'''
#lấy từng dòng trong file 30day.txt gắn vào từng phần tử trong result_list(result_list = ['phần tư_1','phần tử_2'])

def probability_one():
    f = open('30day.txt')
    result_list = f.readlines()
    for son in result_list:
        strson = str(son)
        strson = strson.replace('\n',' ')
        strson = strson.replace(' ','\n')
        with open("probability.txt",'a+',encoding='utf8') as f:
            f.write(strson)

