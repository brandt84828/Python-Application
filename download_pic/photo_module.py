import requests
from bs4 import BeautifulSoup
import os
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def download_pic(url, path):
    pic = requests.get(url) 
    path += url[url.rfind('.'):] 
    with open(path, 'wb') as f: 
        f.write(pic.content)


def get_photolist(photo_name, download_num):
    page = 1 
    photo_list = [] 

    url = 'https://pixabay.com/zh/'  
    option = webdriver.ChromeOptions() 
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)
    browser.get(url)
    browser.implicitly_wait(30)
    browser.find_element(By.NAME, 'search').send_keys(photo_name)
    browser.find_element(By.NAME, 'search').send_keys(Keys.RETURN)

    while True:
        html = browser.page_source
        bs = BeautifulSoup(html, 'lxml')
        photo_item = bs.find('div', {'class': 'flex_grid credits search_results'}).find_all('div', {'class': 'item'})
        if len(photo_item) == 0:
            print('Error, no photo link in page', page)
            return None
        for i in range(len(photo_item)):
            photo = photo_item[i].find('img')['src']
            if photo == '/static/img/blank.gif':
                photo = photo_item[i].find('img')['data-lazy']
            if photo in photo_list:
                continue
            photo = photo.replace('_340', '1280')  #更換為1280解析度
            photo_list.append(photo)
            if len(photo_list) >= download_num:
                print('end by get photo list size', len(photo_list))
                browser.close()
                return photo_list
        page += 1
        try:
            next = browser.find_element_by_partial_link_text(
                '›').get_attribute('href')
            browser.get(next)
        except:
            browser.close()
            return photo_list


def create_folder(photo_name):
    folder_name = input("請輸入要儲存的資料夾名稱: ")

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: " + folder_name)
    else:
        print("找到資料夾: " + folder_name)

    if not os.path.exists(folder_name + os.sep + photo_name):
        os.mkdir(folder_name + os.sep + photo_name)
        print("建立資料夾: " + photo_name)
    else:
        print(photo_name + " 資料夾已存在")
    return folder_name


def get_photobythread(folder_name, photo_name, photo_list):
    download_num = len(photo_list) 
    Q = int(download_num / 100)  
    R = download_num % 100  
    for i in range(Q):
        threads = []
        for j in range(100):
            threads.append(threading.Thread(target=download_pic, args=(
                photo_list[i*100+j], folder_name + os.sep + photo_name + os.sep + str(i*100+j+1))))
            threads[j].start()
        for j in threads:
            j.join()
        print(int((i+1)*100/download_num*100), '%')

    threads = []
    for i in range(R):
        threads.append(threading.Thread(target=download_pic, args=(
            photo_list[Q*100+i], folder_name + os.sep + photo_name + os.sep + str(Q*100+i+1))))
        threads[i].start()
    for i in threads:
        i.join()
    print("100%")
