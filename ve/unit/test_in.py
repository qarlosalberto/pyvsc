# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
'''
Created on Jul 28, 2019

@author: ballance
'''

import unittest
from unittest.case import TestCase

import vsc
from vsc_test_case import VscTestCase


class TestIn(VscTestCase):
    
    def test_single(self):

        @vsc.randobj
        class my_s(object):
            
            def __init__(self):
                super().__init__()
                self.a = vsc.rand_bit_t(8)
                self.b = vsc.rand_bit_t(8)
                self.c = vsc.rand_bit_t(8)
                self.d = vsc.rand_bit_t(8)
                
            @vsc.constraint
            def ab_c(self):
                
#                self.a in vsc.rangelist(self.b+1, [self.b+2,self.c], 8)
                self.a in vsc.rangelist(1, 2, 4, 8)
               

                self.c != 0
                self.d != 0
                
                self.c < self.d
                self.b in vsc.rangelist(vsc.rng(self.c,self.d))
                
        v = my_s()
        for i in range(100):
            v.randomize()
            print("a=" + str(v.a) + " b=" + str(v.b) + " c=" + str(v.c) + " d=" + str(v.d))        
        

    def test_single_d(self):

        @vsc.randobj        
        class my_s():
            
            def __init__(self):
                super().__init__()
                self.a = vsc.rand_bit_t(8)
                self.b = vsc.rand_bit_t(8)
                self.c = vsc.rand_bit_t(8)
                self.d = vsc.rand_bit_t(8)
                
            @vsc.constraint
            def ab_c(self):
                
#                self.a in vsc.rangelist(self.b+1, [self.b+2,self.c], 8)
                self.a in vsc.rangelist(1, 2, 4, 8)
               

                self.c != 0
                self.d != 0
                
                self.c < self.d
                self.b in vsc.rangelist(vsc.rng(self.c,self.d))
                
        v = my_s()
        for i in range(100):
            v.randomize()
            print("a=" + str(v.a) + " b=" + str(v.b) + " c=" + str(v.c) + " d=" + str(v.d))

    def test_in_list_1(self):

        @vsc.randobj
        class my_s(object):
            
            def __init__(self):
                super().__init__()
                self.a = vsc.rand_bit_t(8)
                self.b = vsc.rand_bit_t(8)
                self.l = vsc.list_t(vsc.uint8_t())
                
                for i in range(4):
                    self.l.append(i)
                
            @vsc.constraint
            def ab_c(self):
                
#                self.a in vsc.rangelist(self.b+1, [self.b+2,self.c], 8)
                self.a in self.l
                
        v = my_s()
        for i in range(5):
            v.randomize()
            print("a=" + str(v.a) + " b=" + str(v.b))

    def test_in_list_comb(self):

        @vsc.randobj
        class my_s(object):
            
            def __init__(self):
                super().__init__()
                self.a = vsc.rand_bit_t(8)
                self.b = vsc.rand_bit_t(8)
                self.l = vsc.list_t(vsc.uint8_t())
                
                for i in range(4):
                    self.l.append(i)
                
            @vsc.constraint
            def ab_c(self):
                
                self.a in vsc.rangelist(self.l, 10, 12, 14)
                
        v = my_s()
        with v.randomize_with() as it:
            it.a in vsc.rangelist(0, 1, 2, 3)
            
        self.assertTrue(v.a in [0,1,2,3])
        
        # Now, clear the list so only 10, 12, 14 exist
        v.l.clear()
        v.randomize()
        
        self.assertTrue(v.a in [10, 12, 14])

    def test_in_list_plain(self):

        @vsc.randobj
        class my_s(object):
            
            def __init__(self):
                super().__init__()
                self.a = vsc.rand_bit_t(8)
                self.b = vsc.rand_bit_t(8)
                self.l = list(range(4))
                
            @vsc.constraint
            def ab_c(self):
                
                self.a in vsc.rangelist(self.l, 10, 12, 14)
                
        v = my_s()
        with v.randomize_with() as it:
            it.a in vsc.rangelist(0, 1, 2, 3)
            
        self.assertTrue(v.a in [0,1,2,3])

        