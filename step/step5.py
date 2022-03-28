from function import *

class Step5:
    def calculation(self, gussian=False, heavy_gas=False):
        click_by_id("selectComputeType_input_auto")
        if gussian:
            click_by_id("selectComputeType_input_gussian")
        if heavy_gas:
            click_by_id("selectComputeType_input_heavy")
        click_by_id("SJ_selectComputeType_confirm")
        click_by_id("errJump_content_btn_true")


    def threat_zone(self, toxic=False, flammable=False, explode=False, r_area=None, o_area=None, y_area=None, observe=None):
        click_by_id("step_5_area_btn")
        if toxic:
            click_by_id("select_line_toxic")
            click_by_id("selectHazardousAreaType_confirm")
            time.sleep(0.5)
            click_by_class("Btn_lg", 3)  # 確定
        if flammable:
            click_by_id("select_line_flammable")
            click_by_id("selectHazardousAreaType_confirm")
            time.sleep(1)
            click_by_class("Btn_lg", 5)  # 確定
        if explode:
            click_by_id("select_line_explode")
            click_by_id("selectHazardousAreaType_confirm")
            click_by_id("DirectChemicalValue_confirm")
            time.sleep(0.5)
            click_by_class("Btn_lg", 6)  # 確定


        if r_area and o_area and y_area and observe:
            time.sleep(0.5)
            click_by_class("t_body_l", r_area)
            click_by_class("t_body_l", o_area)
            click_by_class("t_body_l", y_area)
            click_by_class("t_body_l", observe)
            click_by_class("Btn_lg", 4)  # 確定


    def threatzone_toxic(self):
        click_by_id("step_5_area_btn")
        click_by_id("select_line_toxic")
        click_by_id("selectHazardousAreaType_confirm")


    def threatzone_flammable(self):
        click_by_id("step_5_area_btn")
        click_by_id("select_line_flammable")
        click_by_id("selectHazardousAreaType_confirm")


    def threatzone_explode(self, onfire_time=None, by_explode=False, unblock=False):
        click_by_id("step_5_area_btn")
        click_by_id("select_line_explode")
        click_by_id("selectHazardousAreaType_confirm")
        if onfire_time:
            click_by_id("overpressure_time_know")
            input_data_by_id("overpressure_time_input", onfire_time)
        if by_explode:
            click_by_id("overpressure_type_explotion")
        if unblock:
            click_by_id("overpressure_stuck_easy")
        click_by_id("DirectChemicalValue_confirm")
        time.sleep(0.5)
        click_by_class("Btn_lg", 6)

    def threatzone(self):
        click_by_id("step_5_area_btn")
        time.sleep(0.5)
        click_by_class("Btn_lg", 4)

    def threat_point_rel(self, x=0, y=0, unit_m=False, unit_km=False):
        click_by_id("step_5_point_btn")
        click_by_id("selectPositionType_rel")
        # driver.find_element(By.CLASS_NAME, "hazardPoint_rel_input").send_keys("backspace")
        input_data_by_class("hazardPoint_rel_input", Keys.BACKSPACE)
        input_data_by_class("hazardPoint_rel_input", x)
        input_data_by_class("hazardPoint_rel_input", Keys.BACKSPACE, 1)
        input_data_by_class("hazardPoint_rel_input", y, 1)

        # key_list = [Keys.TAB, x, Keys.TAB, y]
        # for key in key_list:
        #         driver.find_element(By.ID, "hazardPoint_content_top").send_keys(key)
        # if unit_m:
        #     click_by_class("t_body_l", 34)
        # if unit_km:
        #     click_by_class("t_body_l", 35)
        click_by_id("hazardPoint_confirm")


    def threat_point_abs(self, x=0, y=0, x_from_E=False, x_from_W=False, y_from_N=False, y_from_S=False, unit_m=False, unit_km=False):
        click_by_id("selectPositionType_abs")
        if x_from_E:
            click_by_class("t_body_l", 55)
        if x_from_W:
            click_by_class("t_body_l", 56)
        if y_from_N:
            click_by_class("t_body_l", 58)
        if y_from_S:
            click_by_class("t_body_l", 59)
        distant_list = [Keys.TAB, x, Keys.TAB, y]
        for distant in distant_list:
                driver.find_element(By.ID, "hazardPoint_content_top").send_keys(distant)
        click_by_id("hazardPoint_confirm")
        if unit_m:
            click_by_class("t_body_l", 61)
        if unit_km:
            click_by_class("t_body_l", 62)
        click_by_id("hazardPoint_confirm")


    def download_kml(self):
        click_by_id("step_5_area_download")
        pass


    def download_source_strength(self, path):
        time.sleep(3)
        charts = driver.find_element(By.ID, "step_5_strong_main")
        charts.screenshot(path)


    def get_source_strength(self, path, file_name):
        all_data = driver.find_elements_by_class_name("normal_data_list")
        for data in reversed(all_data):
            each_text = data.text.split()
            if '總洩漏量:' in each_text:
                print(each_text[1])
                with open(path + file_name + ".txt", "a") as file:
                    file.write(str(each_text[1]) + "\n")



