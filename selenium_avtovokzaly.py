from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Импорт класса для работы с выпадающим списком

import time
import re
import datetime


dat1 = '31.08.2023'

# Определение шаблона регулярного выражения для поиска текста
#pattern = re.compile(r"Купить за \d+")
r = re.compile("Купить за [а-яА-Я0-9.]+")


def insert_input(elem_id,data):
    tag_elem = data[0]
    text_to_insert = data[1]
    print(f"//{tag_elem}[@class='{elem_id}']")
    div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//{tag_elem}[@class='{elem_id}']")))
    div_element[-1].send_keys(text_to_insert)

def cheks(num):
    try:
        select_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select")))  # Найдем все элементы <select>
        select_element =select_elements[0+num]
        select = Select(select_element)
        select.select_by_value("2")


        select_element =select_elements[2+num]
        select = Select(select_element)  # Создаем объект класса Select, передавая ему найденный элемент
        select.select_by_value("1")
        elems =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text() = 'М']")))                                                 
        elems[-1].click()

        elem = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='День']")))
        elem[-1].send_keys('5')
        elem = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='Год']")))
        elem[-1].send_keys('1999')
        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@class='ym-disable-keys']")))
        print('SEND KEYS= ',int(num//4))
        div_element[int(num//4)].send_keys("5739153426")
        #div_element[0].send_keys('март')

        select_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select")))  # Найдем все элементы <select>
        #select_element =select_elements[3]
        #select = Select(select_element)
        #but = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text() = 'Продолжить']")))
        #select.select_by_index(1)
        #but[0].click()
        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='select-container placeholder']")))
        div_element[-1].click()

        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='seat-box seat-widget__seat seat-box_free pointer']")))
        div_element[-1].click()
        return False
    except Exception as ex:
        print('ОШИБКА',ex)
        return True


chrome_options = Options()
#chrome_options.add_argument("--headless")

# Укажите абсолютный путь к chromedriver.exe на вашем компьютере
chrome_driver_path = "E:\\projects\\BUS_BUS_BUS\\chromeDriver\\chromedriver.exe"

# Инициализируем объект Service
service = Service(executable_path=chrome_driver_path)

# Инициализируем драйвер, передавая объект Service
driver = webdriver.Chrome(service=service, options=chrome_options)


# Открываем сайт
wait = WebDriverWait(driver, 60)
wait2 = WebDriverWait(driver, 2)
wait3 = WebDriverWait(driver, 300)
url = f"https://www.avtovokzaly.ru/booking/route/3326882/from/8473802/to/8473803/dt/8189134?date={dat1}" # Ваш маршрут
#url = f"https://www.avtovokzaly.ru/booking/route/3205773/from/7798577/to/7798578/dt/7985172?date={dat1}"
while True:
    try:
        driver.get(url)
        dic = {
        "1n ym-disable-keys":['input',"оаоаоа"],
        "2n ym-disable-keys":['input',"оаоаоа"],
        "3n ym-disable-keys":['input',"оаоаоао"]

            }
        for i in dic:
            insert_input(i,dic[i])#'1n ym-disable-keys','оаоаоаоа')


        #div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[@class='select-container placeholder']")))
        #print(div_element[0])
        #div_element[0].click()

        select_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select")))  # Найдем все элементы <select>
        select_element =select_elements[0]
        select = Select(select_element)  # Создаем объект класса Select, передавая ему найденный элемент
        select.select_by_value("2")


        select_element =select_elements[2]
        select = Select(select_element)  # Создаем объект класса Select, передавая ему найденный элемент
        select.select_by_value("1")


        elems =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text() = 'М']")))
        print(elems)                                                     
        elems[0].click()

        elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='День']")))
        elem.send_keys('5')
        elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Год']")))
        elem.send_keys('1999')
        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@class='ym-disable-keys']")))
        div_element[0].send_keys("5739153426")
        select_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select")))  # Найдем все элементы <select>
        but = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text() = 'Продолжить']")))

        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='select-container placeholder']")))
        div_element[-1].click()

        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='seat-box seat-widget__seat seat-box_free pointer']")))
        div_element[0].click()
        but[0].click()
        time.sleep(2)
        box = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class = 'box']")))
        box[1].click()
        box[2].click()
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight-100);")
        div_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@class='ym-disable-keys']")))
        div_element[1].send_keys("jfjfjffj@maail.ru")
        elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='+7 912 345-67-89']")))
        elem.click()
        elem.send_keys("79123456789")

        elems =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class = 'button button-green booking-form__submit']")))
        print('А ЭТО КОНЕЦ')
        elems_echo =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class = 'button']")))
        print(elems_echo,len(elems_echo))
        elems_echo[-1].click()

        j = 1
        while True:
            for i in dic:
                insert_input(i,dic[i])
            fl = cheks(4*j)
            if fl:
                break
            else:
                elems_echo =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class = 'button']")))
                elems_echo[-1].click()
                j+=1
        while True:
            try:
                elems =  wait2.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class = 'button button-green booking-form__submit']")))
                elems[-1].click()
                break
            except Exception as ex:
                time.sleep(2)
        while True:
            try:
                elems =  wait2.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='alert alert-success clearfix half-mt']")))
                break
            except Exception as ex:
                time.sleep(2)
                print('Задержка для прогрузки страницы')


    
    except Exception as ex:
        print('продолжение....')
        continue




















