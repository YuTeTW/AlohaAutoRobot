from function import *
from typing import Optional


class Step1:
    def time(self, year = None,  # 西元
             month: int = None,
             day: int = None,
             session: str = None,  # "上午"、"下午"
             hour: int = None,
             minute: int = None,):
        if year or month or day or hour or minute or hour or minute :
            if 24 > hour > 12:
                hour -= 12
            click_by_class("t_body_l", 2)
            driver.find_element(By.ID, "time_block_self_date").send_keys(year)
            driver.find_element(By.ID, "time_block_self_date").send_keys(month)
            if month == 1 :
                driver.find_element(By.ID, "time_block_self_date").send_keys(Keys.TAB)
            driver.find_element(By.ID, "time_block_self_date").send_keys(day)
            driver.find_element(By.ID, "time_block_self_time").send_keys(session)
            driver.find_element(By.ID, "time_block_self_time").send_keys(Keys.TAB)
            driver.find_element(By.ID, "time_block_self_time").send_keys(hour)
            if hour == 1:
                driver.find_element(By.ID, "time_block_self_time").send_keys(Keys.TAB)
            driver.find_element(By.ID, "time_block_self_time").send_keys(minute)
        else:
            pass


    def location(self, address: Optional[str] = "台北市中山區民權東路一段45號4號",
                 latitude: Optional[float] = None,
                 longtitude: Optional[float] = None,
                 altitude: Optional[float] = None,
                 unit: Optional[str] = "m"):
        if latitude and longtitude:
            click_by_id("locate_select_latlon")
            input_data_by_id("locate_block_lat_input", latitude)
            input_data_by_id("locate_block_lon_input", longtitude)
            click_by_id("locate_select_latlon_confirm")
        else:
            input_data_by_id("locate_block_address_input", address)
            click_by_id("locate_select_address_confirm")
        if altitude:
            input_data_by_id("locate_block_height_input", altitude)
            if unit == "km":
                click_by_class("t_body_l", 5)
            else:
                click_by_class("t_body_l", 4)
        pass


    def buliding(self, enclosed_office: Optional[bool] = False,
                 single_storied: Optional[bool] = False,
                 single_storied_affect: Optional[bool] = False,
                 double_storied: Optional[bool] = False,
                 double_storied_affect: Optional[bool] = False,
                 air_exchange: Optional[bool] = False,
                 air_exchange_data: Optional[float] = 0.5):
        if enclosed_office:
            click_by_id("building_block_close")
        if single_storied:
            click_by_id("building_block_build_1")
            if single_storied_affect:
                click_by_class("t_body_l", 8)
            else:
                click_by_class("t_body_l", 7)
        if double_storied:
            click_by_id("building_block_build_2")
            if double_storied_affect:
                click_by_class("t_body_l", 11)
            else:
                click_by_class("t_body_l", 10)
        if air_exchange:
            click_by_id("building_block_open")
            driver.find_element(By.ID, "building_block_open_input").send_keys(air_exchange_data)
            pass

        pass


    def next_step(self):
        time_end = time.time() + 5
        while True:
            try:
                click_by_id("step_1_content_next")
            except Exception as e:
                break
            # if time_end < time.time():
            #     break


