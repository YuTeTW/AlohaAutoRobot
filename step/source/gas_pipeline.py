from function import *


class GasPipeline:
    def escape(self, burning=False):
        if burning:
            click_by_id("pipeline_step1_select_burn")
        else:
            click_by_id("pipeline_step1_select_unburn")

    def pipeline(self, diameter=None, length=None, closed=False, smooth=False):
        input_data_by_id("pipeline_step2_input_diameter", diameter)
        input_data_by_id("pipeline_step2_input_length", length)
        if closed:
            click_by_id("pipeline_step2_pipelineClose_true")
        else:
            click_by_id("pipeline_step2_pipelineClose_false")
        if smooth:
            click_by_id("pipeline_step2_pipelineRough_1")
        else:
            click_by_id("pipeline_step2_pipelineRough_0")
        click_by_id("pipeline_step2_confirm")


    def pipelin_pressure_and_hole(self, pressure, unit_psia=False, unit_atm=False, unit_pa=False, unknow=False, temp=30, hole_size=None):
        input_data_by_id("pipeline_step3_input_diameter", pressure)
        if unit_psia:
            click_by_class("t_body_l", 6)
        if unit_atm:
            click_by_class("t_body_l", 7)
        if unit_pa:
            click_by_class("t_body_l", 8)
        if unknow:
            click_by_id("pipeline_step3_pipelineTemp_0")
        else:
            click_by_id("pipeline_step3_pipelineTemp_1")
            input_data_by_id("pipeline_step3_pipelineTemp_input", temp)

        if hole_size:
            click_by_id("pipeline_step3_pipelineHole_1")
        else:
            click_by_id("pipeline_step3_pipelineHole_0")
        input_data_by_id("pipeline_step3_pipelineHole_input", 50)

        pass

