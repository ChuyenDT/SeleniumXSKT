from collections import Counter
def number_max():
    s = open('probability2.txt')               
    result_list2 = s.readlines()
    # convert list 'string' to list int 
    result_list2 = list(map(int,result_list2))
    # sử dụng Counter để tìm số lần xuất hiện của các số
    cnt = Counter(result_list2)
    print(cnt)