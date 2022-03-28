import datetime

from function import *

pure_chemical_list = ["chemical_71432", "chemical_74828", "chemical_78875", "chemical_630080", "chemical_106990", "chemical_115071"]


class Step3:
    def pure_chemical(self, chemical_CASNo):
        try:
            click_by_id("chemical_block_type_pure")  # 純物質
            click_by_id("chemical_" + str(chemical_CASNo))  # 純物質化學物
        except Exception as e:
            print("CASNo isn't exist")


    def solution(self, liquid_number, percent):
        try:
            click_by_id("chemical_block_type_liq")
            click_by_id("liq_" + str(liquid_number))
            driver.find_element(By.ID, "liqBlock_weight_info_input").send_keys(percent)
        except Exception as e:
            print("liquid number between 0 ~ 4")

    def next_step(self):
        time_end = time.time() + 5
        while True:
            try:
                click_by_id("step_3_content_next")
            except Exception as e:
                break
            # if time_end < time.time():
            #     break

