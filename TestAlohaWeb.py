import datetime
import os
from function import error, driver
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


def start_test():
    for chemical in [71432, 74828, 78875, 630080, 106990, 115071]:
        for direct_unit in ["liters"]:
            for volume_info in ["gas", "liquid"]:
                for self_temp in [-500, -50, -5, 5, 50, 500]:
                    for self_press in [50000, 500000, 5000000, 50000000]:
                        for source_situation in ["instantaneous", "continuous"]:
                            for amount in [10, 100, 1000, 10000, 100000]:

                                today = datetime.datetime.now().strftime("%Y_%m_%d_%H")
                                path = os.getcwd() + "/result/" + today + "/"
                                if not os.path.isdir(path):
                                    os.makedirs(path)

                                try:
                                    start()

                                    step1.time(year=2021, month=6, day=7, session="下午", hour=12, minute=00)
                                    step1.location(address="台中市精武路295號", )
                                    step1.buliding(air_exchange=True, air_exchange_data=0.5)
                                    step1.next_step()

                                    step2.astomspheric(wind_speed=2, wind_is_from=90, humidity=50, air_temperature=30, measurement_high=200)
                                    step2.ground_roughness(input_roughness_roughness=0.03)
                                    step2.cloud_cover(5)
                                    step2.inversion_height(100)
                                    step2.class_stability(stability="C")

                                    step2.next_step()


                                    step3.pure_chemical(chemical_CASNo=chemical)
                                    # time.sleep(5)
                                    print("step333333")
                                    step3.next_step()

                                    step4.source(direct=True)

                                    step4.direct.unit_volume(liters=True)

                                    if volume_info == "liquid":
                                        step4.direct.volume_info(liquid=True, self_temp=self_temp)
                                    else:
                                        step4.direct.volume_info(gas=True, self_temp=self_temp, self_press=self_press)

                                    if source_situation == "continuous":
                                        step4.direct.source_situation(continuous=True, amount=amount, cont_unit_min=True, cont_time=30)
                                    else:
                                        step4.direct.source_situation(instantaneous=True, amount=amount)

                                    step4.direct.source_height(0)

                                    step4.next_step()

                                    step5.threat_zone(ok=3, toxic=True)
                                    step5.get_source_strength(path=path, file_name="online_aloha")

                                except:
                                    try:
                                        text = driver.find_element(By.CLASS_NAME, "error_data").text
                                        with open(path + "liters_online_aloha_error_text" + ".txt", "a", encoding="utf-8") as file:
                                            file.write(text)
                                        error(path=path, file_name="liters_online_aloha_error_text", chemical_CASNo=chemical,
                                              direct_unit=direct_unit, volume_info=volume_info, self_temp=self_temp,
                                              self_press=self_press, source_situation=source_situation, amount=amount)
                                    except:
                                        error(path=path, file_name="liters_online_aloha_error", chemical_CASNo=chemical,
                                              direct_unit=direct_unit, volume_info=volume_info, self_temp=self_temp,
                                              self_press=self_press, source_situation=source_situation, amount=amount)