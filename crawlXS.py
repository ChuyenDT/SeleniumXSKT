from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#1: khai bao brower
brower = webdriver.Chrome(executable_path="./chromedriver.exe")
#2: open URL "https://xskt.com.vn/"
brower.get("https://xskt.com.vn/")
sleep(5)
#3: get link department_tphcm
show_department_link =brower.find_element_by_xpath("/html/body/div[3]/section[1]/ul[2]/li[1]/a")
show_department_link.click()
sleep(5)
#4: get result
''' các giá trị trong aRay tương ứng với giá trị các thẻ <tr> phân tích đc trong element
    //*[@id="HCM0"]/tbody/tr[2]/td[2]/em
    //*[@id="HCM0"]/tbody/tr[3]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[4]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[5]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[6]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[8]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[9]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[10]/td[2]/p
    //*[@id="HCM0"]/tbody/tr[11]/td[2]/em '''
aRay = ['2','3','4','5','6','8','9','10','11']
for i in aRay:
    element = '//*[@id="HCM0"]/tbody/tr[x]/td[2]'
    # thay thế kí tự 'x'trong chuỗi element bằng giá trị của i sau đó gán lại cho element chuỗi mới
    element = element.replace('x',i)
    if i == '2' or i == '11':
        element = (element + "/em")
        result = brower.find_element_by_xpath(element)
        print(result.text,"\n------")
    else:
        element = (element + "/p")
        result = brower.find_element_by_xpath(element)
        print(result.text,"\n------")
        
sleep(5)   
# close brower
brower.close()
