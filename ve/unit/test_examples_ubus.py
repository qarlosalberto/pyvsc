'''
Created on Jan 23, 2020

@author: ballance
'''
from unittest.case import TestCase

import vsc
from vsc.rand_obj import RandObj
from vsc.types import rand_enum_t, rand_bit_t, rangelist
from enum import Enum, auto


class TestExamplesUbus(TestCase):
    
    def test_ubus(self):
        
        class ubus_read_write_enum(Enum):
            READ = auto()
            WRITE = auto()
        
        class ubus_transfer(RandObj):
            
            def __init__(self):
                super().__init__()
                self.addr = rand_bit_t(16)
                self.read_write = rand_enum_t(ubus_read_write_enum)
                self.size = rand_bit_t(32)
#                rand bit [7:0]            data[];
#                rand bit [3:0]            wait_state[];
                self.error_pos = rand_bit_t(32)
                self.transmit_delay = rand_bit_t(32)
                self.master = ""
                self.slave = ""

#             @vsc.constraint
#             def c_read_write(self):
#                 self.read_write in rangelist(
#                     ubus_read_write_enum.READ, 
#                     ubus_read_write_enum.WRITE)

            @vsc.constraint
            def c_size(self):
                self.size in rangelist(1,2,4,8)

#            constraint c_data_wait_size {
#                data.size() == size;
#                wait_state.size() == size;

            @vsc.constraint
            def c_transmit_delay(self):
                self.transmit_delay <= 10

        xfer = ubus_transfer()
        for i in range(100):
            xfer.randomize()
            print("size=" + str(xfer.size) + " transmit_delay=" + str(xfer.transmit_delay))
            
        for i in range(100):
            with xfer.randomize_with() as it:
                it.size == 1
            print("size=" + str(xfer.size) + " transmit_delay=" + str(xfer.transmit_delay))