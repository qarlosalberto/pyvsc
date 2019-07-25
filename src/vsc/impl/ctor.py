
#   Copyright 2019 Matthew Ballance
#   All Rights Reserved Worldwide
#
#   Licensed under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in
#   compliance with the License.  You may obtain a copy of
#   the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in
#   writing, software distributed under the License is
#   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#   CONDITIONS OF ANY KIND, either express or implied.  See
#   the License for the specific language governing
#   permissions and limitations under the License.

'''
Created on Jul 23, 2019

@author: ballance
'''
from vsc.model.rand_obj_model import RandObjModel


rand_obj_type_m = {}
constraint_l = []

def register_rand_obj_type(t):
#    rand_obj_type_m[t] = RandObjModel(t)
    pass
    
def push_constraint(c):
    constraint_l.append(c)
    
def pop_constraints(t):
    
    if t != None:
        ret = []
        t_qname = t.__qualname__
        i=0
        while i < len(constraint_l):
            s = constraint_l[i]
            s_qname = s.t.__qualname__
            
            if len(s_qname) > len(t_qname) and t_qname == s_qname[:s_qname.rfind('.')]:
                ret.append(s)
                constraint_l.remove(s)
            else:
                i += 1
    else:
        ret = constraint_l.copy()
        constraint_l.clear()

    return ret        
    