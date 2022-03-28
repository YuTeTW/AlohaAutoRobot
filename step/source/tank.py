from function import *

class Tank:
    def tank_type(self, horizontal_cylinder_diameter=None, horizontal_cylinder_length=None,
                    vertical_cylinder_diameter=None, vertical_cylinder_length=None,
                    sphere_diameter=None):
        if horizontal_cylinder_diameter and horizontal_cylinder_length:
            click_by_id("tank_step1_tankType_1")
            input_data_by_id("tank_step1_tankSize_diameter", horizontal_cylinder_diameter)
            input_data_by_id("tank_step1_tankSize_length", horizontal_cylinder_length)
        elif vertical_cylinder_diameter and vertical_cylinder_length:
            click_by_id("tank_step1_tankType_2")
            input_data_by_id("tank_step1_tankSize_diameter", vertical_cylinder_diameter)
            input_data_by_id("tank_step1_tankSize_height", vertical_cylinder_length)
        elif sphere_diameter:
            click_by_id("tank_step1_tankType_3")
            input_data_by_id("tank_step1_tankSize_diameter", sphere_diameter)
        click_by_id("tank_step1_confirm")


    def state(self, liquid=False, gas=False, unknow= False, self_temperture=None):
        if liquid:
            click_by_id("tank_step2_list_l")
        elif gas:
            click_by_id("tank_step2_list_g")
        elif unknow:
            click_by_id("tank_step2_list_u")

        if self_temperture:
            click_by_id("tank_step2_list_1")
            input_data_by_id("tank_step2_tankContentTemp_input", self_temperture)
        else:
            click_by_id("tank_step2_list_0")
        click_by_id("tank_step2_confirm")


    def liquid_set(self, weight=None, volume=None, percent=None):
        # input_data_by_id("step3_list_l_weight", weight)
        # input_data_by_id("step3_list_l_volume", volume)
        # 需先選擇錯誤才可導入值
        input_data_by_id("step3_list_l_percent", 101)#錯誤
        click_by_class("errJump_content_btn_true")
        input_data_by_id("step3_list_l_percent", percent)#正確
        click_by_id("tank_step3_confirm")#確定


    def gas_or_unknow_set(self, pressure=None, pressure_unit_atm=False, pressure_unit_mmHg=False, pressure_unit_psia=False, pressure_unit_pa=False,
                                amount=None, amount_unit_kg=False, amount_unit_pound=False, amount_unit_ton=False):
        if pressure:
            input_data_by_id("step3_list_press", pressure)
            if pressure_unit_atm:
                click_by_class("t_body_l", 6)
            if pressure_unit_mmHg:
                click_by_class("t_body_l", 7)
            if pressure_unit_psia:
                click_by_class("t_body_l", 8)
            if pressure_unit_pa:
                click_by_class("t_body_l", 9)
        if amount:
            input_data_by_id("step3_list_l_volume", amount)
            if amount_unit_kg:
                click_by_class("t_body_l", 11)
            if amount_unit_pound:
                click_by_class("t_body_l", 12)
            if amount_unit_ton:
                click_by_class("t_body_l", 13)


    def failure(self, unburn=False, poolfire=False, fireball=False):
        if unburn:
            click_by_id("tank_step4_burn_0")
        if poolfire:
            click_by_id("tank_step4_burn_1")
        if fireball:
            click_by_id("tank_step4_burn_2")

        click_by_id("tank_step4_confirm")

    def unburn_set(self, circle=True, hole=True, diameter=None, length=None, width=None, unit_cm=False, unit_m=False, unit_feet=False):
        if circle and diameter:
            click_by_id("tank_step5_holeShape_0")
            input_data_by_class("tank_step5_normal_inputContent", Keys.TAB)
            input_data_by_class("tank_step5_normal_inputContent", diameter)
        elif hole and length and width:
            click_by_id("tank_step5_holeShape_1")
            input_data_by_class("tank_step5_normal_inputContent", Keys.TAB)
            input_data_by_class("tank_step5_normal_inputContent", hole)
            input_data_by_class("tank_step5_normal_inputContent", Keys.TAB)
            input_data_by_class("tank_step5_normal_inputContent", hole)
        else:
            print("step4 進階設定有值沒填")

        if hole:
            click_by_id("tank_step5_sourcePoint_0")
        else:
            click_by_id("tank_step5_sourcePoint_1")

        if unit_cm:
            click_by_class("t_body_l", 11)
        if unit_m:
            click_by_class("t_body_l", 12)
        if unit_feet:
            click_by_class("t_body_l", 13)
        click_by_id("tank_step5_confirm")

        pass


    def poolfire_set(self):
        pass


    def fireball_set(self, percent=False, pressure=False, temperture=False, pre_unit_atm=False, pre_unit_mmHg=False, pre_unit_psia=False, pre_unit_pa=False):
        if percent:
            click_by_id("tank_step5_fire_percent")
            input_data_by_id("tank_step5_fire_percentInput", percent)
        if pressure:
            click_by_id("tank_step5_fire_press")
            input_data_by_id("tank_step5_fire_pressInput", pressure)
            if pre_unit_atm:
                click_by_class("t_body_l", 16) #單位
            elif pre_unit_mmHg:
                click_by_class("t_body_l", 17) #單位
            elif pre_unit_psia:
                click_by_class("t_body_l", 18) #單位
            elif pre_unit_pa:
                click_by_class("t_body_l", 19) #單位
        if temperture:
            click_by_id("tank_step5_fire_temp")
            input_data_by_id("tank_step5_fire_tempInput", temperture)
        click_by_id("tank_step5_confirm")
        pass

    def hole_height(self, height, percent, max_diameter=None, max_area=None):
        input_data_by_class("holeHeight_input", Keys.TAB)
        input_data_by_class("holeHeight_input", height)
        input_data_by_class("holeHeight_input", Keys.TAB)
        input_data_by_class("holeHeight_input", percent)
        click_by_id("step_other_holeHeight_confirm")
        if max_diameter:
            input_data_by_class("SJ_title", Keys.TAB)
            input_data_by_class("SJ_title", max_diameter)
        if max_area:
            input_data_by_class("SJ_title", Keys.TAB)
            input_data_by_class("SJ_title", max_area)
        click_by_id("step_other_puddleValue_confirmm")
        #形成兩向流提示
        if not max_diameter and max_diameter:
            click_by_class("errJump_content_btn_true")


