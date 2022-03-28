import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://aloha.fastwise.net"
# url = "https://aloha.eric.org.tw/"
driver = webdriver.Chrome()
driver.set_window_position(-900, -1400)
driver.set_window_size(900, 1400)


def click_by_id(buttom_Id):
    js = 'document.getElementById("' + buttom_Id + '").click()'
    driver.execute_script(js)


def click_by_class(class_name, number=0):
    js = 'document.getElementsByClassName("' + class_name + '")[' + str(number) + '].click()'
    driver.execute_script(js)


def input_data_by_id(id, data):
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "A")
    driver.find_element(By.ID, id).send_keys(Keys.CONTROL + "A")
    driver.find_element(By.ID, id).send_keys(Keys.BACKSPACE)
    driver.find_element(By.ID, id).send_keys(data)


def input_data_by_class(class_name, data, num=0):
    driver.find_elements(By.CLASS_NAME, class_name)[num].send_keys(data)


def error(path, file_name, **kwargs):
    all_params = "error_params: "
    for key, value in kwargs.items():
        all_params = all_params + str(key) + "=" + str(value) + ", "
    with open(path + file_name + ".txt", "a", encoding="utf-8") as file:
        file.write(all_params + "\n")





