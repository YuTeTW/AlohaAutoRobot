from function import *

class Direct:
    def unit_mass(self, grams=False, kilograms=False, pound=False, tons=False):
        global compensate
        compensate = False
        if grams:
            click_by_class("t_body_l", 6)
        if kilograms:
            click_by_class("t_body_l", 7)
        if pound:
            click_by_class("t_body_l", 8)
        if tons:
            click_by_class("t_body_l", 9)


    def unit_volume(self, cubic_meters=False, liters=False, cubic_feet=False, gallons=False):
        global compensate
        compensate = True
        if cubic_meters:
            click_by_class("t_body_l", 10)
        if liters:
            click_by_class("t_body_l", 11)
        if cubic_feet:
            click_by_class("t_body_l", 12)
        if gallons:
            click_by_class("t_body_l", 13)


    def volume_info(self, gas=False, liquid=False, self_temp=None, self_press=None,
                    pre_unit_pa=False, pre_unit_mmHg=False, pre_unit_atm=False, pre_unit_psia=False):
        if gas:
            click_by_id("selectChemcialType_gas")
        if liquid:
            click_by_id("selectChemcialType_liq")
        if self_temp:
            click_by_id("selectChemcialTemp_user")
            input_data_by_id("selectChemcialTemp_user_input", self_temp)
        if self_press:
            click_by_id("selectChemcialPress_user")
            input_data_by_id("selectChemcialPress_user_input", self_press)
            if pre_unit_pa:
                click_by_class("t_body_l", 15)
            if pre_unit_mmHg:
                click_by_class("t_body_l", 16)
            if pre_unit_atm:
                click_by_class("t_body_l", 17)
            if pre_unit_psia:
                click_by_class("t_body_l", 18)


    def source_situation(self, instantaneous=False, continuous=False,
                         amount = 100, cont_unit_sec = False, cont_unit_min = False, cont_unit_hr = False , cont_time = 1):
        if instantaneous:
            click_by_id("selectConditionType_instant")
            input_data_by_id("selectConditionVolume_instant", amount)

        if continuous:
            click_by_id("selectConditionType_continuous")
            input_data_by_id("selectConditionVolume_instant", amount)
            if compensate:
                if cont_unit_sec:
                    click_by_class("t_body_l", 15)
                if cont_unit_min:
                    click_by_class("t_body_l", 16)
                if cont_unit_hr:
                    click_by_class("t_body_l", 17)
            else:
                if cont_unit_sec:
                    click_by_class("t_body_l", 15)
                if cont_unit_min:
                    click_by_class("t_body_l", 16)
                if cont_unit_hr:
                    click_by_class("t_body_l", 17)
            input_data_by_id("selectConditionTime_instant", cont_time)


    def source_height(self, height):
        input_data_by_id("direct_height_input", height)





# # def input_data():#dict_input: A):
# # 體積選項
# # 1氣態
# click_by_id("directChemical_temp_user")
# input_data_by_id("directChemical_temp_inputTemp")
# click_by_id("directChemical_pres_user")
# input_data_by_id("directChemical_pres_inputPres")
# click_by_class("t_body_l", 16)
# click_by_id("DirectChemicalValue_confirm")
# # 2液態
# click_by_id("directChemical_type_water")
# click_by_id("directChemical_temp_user")
# input_data_by_id("directChemical_temp_inputTemp", 20)

