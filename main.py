import datetime
import os
import time

from TestAlohaWeb import start_test
from function import error, driver, url
from selenium.webdriver.common.by import By

from step.page import start
from step.step1 import Step1
from step.step2 import Step2
from step.step3 import Step3
from step.step4 import Step4
from step.step5 import Step5

step1 = Step1()
step2 = Step2()
step3 = Step3()
step4 = Step4()
step5 = Step5()

if __name__ == "__main__":
    driver.get(url)
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()
    driver.execute_script("document.body.style.zoom='0.5'")
    start_test()
