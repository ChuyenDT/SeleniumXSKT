from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# 1: khai bao brower

# 3: get link department_tphcm
'''show_department_link = brower.find_element_by_xpath("/html/body/div[3]/section[1]/ul[2]/li[1]/a")
show_department_link.click()
sleep(5)
# 4: get link department_tphcm in 30 day
show_link30day = brower.find_element_by_xpath('//*[@id="HCM0"]/tbody/tr[12]/td/a[2]')
show_link30day.click()
sleep(5)'''
# 5: get result
def get_data_from_brower():
    brower = webdriver.Chrome(executable_path="./chromedriver.exe")
    # 2: open URL "https://xskt.com.vn/"
    brower.get("https://xskt.com.vn/xshcm-xstp/100-ngay")
    sleep(5)
    fullday = 100
    aRay = ['2', '3', '4', '5', '6', '8', '9', '10', '11']
    for day in range(fullday):
        day =str(day)
        for changeTr in aRay:        
            # thay thế kí tự 'x'trong chuỗi element bằng giá trị của changeTr sau đó gán lại cho element chuỗi mới
            element = '//*[@id="HCMY"]/tbody/tr[x]/td[2]'
            element = element.replace('Y', day)
            element = element.replace('x', changeTr)
            if changeTr == '2' or changeTr == '11':
                element = (element + "/em")
                #print(element)
                result = brower.find_element_by_xpath(element)
                with open("30day.txt",'a+',encoding='utf8') as f:
                    f.write(result.text)
                    f.write(" ")
                #print(result.text, "\n------")
            else:
                element = (element + "/p")
                #print(element)
                result = brower.find_element_by_xpath(element)
                with open("30day.txt",'a+',encoding='utf8') as f:
                    f.write(result.text)
                    f.write(" ")
                #print(result.text, "\n------")  
    brower.close()
def main():
    get_data_from_brower()

if __name__ == "__main__":
    main()