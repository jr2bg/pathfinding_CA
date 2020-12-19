from utils.CA_def import *


nh = [[{"s_state":  -1, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0}],

      [{"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0}],

      [{"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  -1, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0},
       {"s_state":  1, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0}]
    ]
print(rules(nh))
