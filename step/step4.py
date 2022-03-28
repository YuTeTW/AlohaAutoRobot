from function import *
from .source.direct import Direct
from .source.puddle import Puddle
from .source.tank import Tank
from .source.gas_pipeline import GasPipeline


class Step4:
    def __init__(self):
        self.direct = Direct()
        self.puddle = Puddle()
        self.tank = Tank()
        self.gas_pipeline = GasPipeline()


    def source(self, direct=False, puddle=False, tank=False, gaspipeline=False):
        if direct:
            click_by_id("step_4_index_direct")
        elif puddle:
            click_by_id("step_4_index_puddle")
        elif tank:
            click_by_id("step_4_index_tank")
        elif gaspipeline:
            click_by_id("step_4_index_pipeline")


    def next_step(self):
        time_end = time.time() + 10
        while True:
            try:
                click_by_class("Btn_lg page_block_bottom_next")
            except Exception as e:
                break
            # if time_end < time.time():
            #     break






