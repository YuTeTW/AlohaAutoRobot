from function import *


class Puddle:
    def state(self, evaporate=False, poolfire=False):
        if evaporate:
            click_by_id("selectPuddleCondition_normal")
        if poolfire:
            click_by_id("selectPuddleCondition_burning")
        click_by_id("puddle_step0_block_next")


    def puddle_volume(self, area=None, diameter=None,
                      volume=None, volume_unit_liter=False, volume_unit_cubic_meter=False, volum_unit_gallon=False,
                      depth=None, depth_unit_meter=False, depth_unit_centimeter=False,
                      weight=None, weight_unit_kg=False, weight_unit_ton=False, weight_unit_pound=False, weight_unit_metric_ton=False):
        if area:
            click_by_id("puddleVolume_select_countUnit_area")
            input_data_by_id("puddleVolume_area_input", area)
        elif diameter:
            click_by_id("puddleVolume_select_countUnit_diamater")
            input_data_by_id("puddleVolume_diamater_input", diameter)
        if volume:
            click_by_id("puddleVolume_select_countWeight_volume")
            input_data_by_id("puddleVolume_countWeight_volume_input", volume)
            if volume_unit_liter:
                click_by_class("t_body_l", 6)
            elif volume_unit_cubic_meter:
                click_by_class("t_body_l", 7)
            elif volum_unit_gallon:
                click_by_class("t_body_l", 8)
        elif depth:
            click_by_id("puddleVolume_select_countWeight_depth")
            input_data_by_id("puddleVolume_countWeight_depth_input", depth)
            if depth_unit_meter:
                click_by_class("t_body_l", 10)
            elif depth_unit_centimeter:
                click_by_class("t_body_l", 11)
        elif weight:
            click_by_id("puddleVolume_select_countWeight_weight")
            input_data_by_id("puddleVolume_countWeight_weight_input", weight)
            if weight_unit_kg:
                click_by_class("t_body_l", 13)
            elif weight_unit_ton:
                click_by_class("t_body_l", 14)
            elif weight_unit_pound:
                click_by_class("t_body_l", 15)
            elif weight_unit_metric_ton:
                click_by_class("t_body_l", 16)


    def surface(self, soil=False, concrete=False, sandy_dry_soil=False, moist_sandy_soil=False, water=False, temperture=None):
        if soil:
            click_by_class("t_body_l", 18)
        elif concrete:
            click_by_class("t_body_l", 19)
        elif sandy_dry_soil:
            click_by_class("t_body_l", 20)
        elif moist_sandy_soil:
            click_by_class("t_body_l", 21)
        elif water:
            click_by_class("t_body_l", 22)

        if temperture:
            click_by_id("puddle_puddle_type_user")
            input_data_by_id("puddle_puddle_type_user_input", 25)
        else:
            click_by_id("puddle_puddle_type_ground")


    def puddle_temperture(self, ground_temp=False, air_temp=False, self_temp=None):
        if ground_temp:
            click_by_id("puddle_puddle_type_ground")
        elif air_temp:
            click_by_id("puddle_puddle_type_air")
        elif self_temp:
            click_by_id("puddle_puddle_type_user")
            input_data_by_id("puddle_puddle_type_user_input", air_temp)

