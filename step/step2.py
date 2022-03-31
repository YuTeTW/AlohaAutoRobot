from function import *

class Step2:
    def astomspheric(self, wind_speed=None,
                     wind_is_from=None,
                     humidity=None,
                     air_temperature=None,
                     measurement_high=None):
        input_data_by_id("env_block_wind_input", wind_speed)
        input_data_by_id("env_block_windDirec_input", wind_is_from)
        input_data_by_id("env_block_wet_input", humidity)
        input_data_by_id("env_block_temp_input", air_temperature)
        input_data_by_id("env_block_height_input", measurement_high)


    def ground_roughness(self, open_country=False,
                         urban_or_forest=False,
                         open_wate=False,
                         input_roughness_roughness=None):
        if open_country:
            click_by_class("t_body_l", 5)
        if urban_or_forest:
            click_by_class("t_body_l", 6)
        if open_wate:
            click_by_class("t_body_l", 7)
        if input_roughness_roughness:
            click_by_class("t_body_l", 8)
            input_data_by_id("env_Other_block_ground_input", input_roughness_roughness)


    def cloud_cover(self, amount):
        click_by_class("t_body_l", 11)
        input_data_by_id("env_Other_block_cloud_input", amount)


    def inversion_height(self, height):
        if height:
            click_by_class("t_body_l", 14)
            input_data_by_id("env_Other_block_inHeight_input", height)
        else:
            click_by_class("t_body_l", 13)


    def class_stability(self, stability="B"):
        i = 23
        while True:
            try:
                click_by_class("t_body_l", i)
                break
            except Exception as e:
                i -= 1
        input_data_by_id("env_Other_block_air_input", stability)


    def next_step(self):
        time_end = time.time() + 5
        while True:
            try:
                click_by_id("step_2_content_next")
                break
            except Exception as e:
                pass
            # if time_end < time.time():
            #     break