def cell_init():
    return {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":0, "phi_s": 0}

def obstacle_init():
    return {"s_state": -1, "s_cf" : 0, "s_pf":0, "p_ij":0, "phi_s": 0}
    
def extract_neighbourhood(grid, i,j):
    nh = [[grid[i+i_t][j + j_t] for i_t in range(3)] for j_t in range(3)]
    return nh
    
    
def delta(i,j):
    if (i+j)%2 == 0:
        return 2**(1/2)
    return 1

def rules(nh):
    for i in range(3):
        for j in range(3):
            
            # hay una celda activa alrededor
            if nh[i][j]["s_state"] == 1:
                # la celda considerada no está activa
                if nh[1][1] == 0:
                    # se actualizan los estados
                    s_state = 1
                    
                    #se vuelve chavo
                    s_cf = 1
                    d = delta(i,j)
                    
                    # si es la primera vez que encuentra a un vecino activo
                    if nh[1][1]["phi_s"] == 0:
                        phi_s = nh[i][j]["phi_s"] + d
                        # dirección
                        p_ij = (i,j)
                    
                    # encontrar el mínimo de la distancia
                    if nh[i][j]["phi_s"] + d < phi_s:
                        # dirección
                        p_ij = (i,j)
                        
                # cambia de padre a hijo    
                else:
                    s_pf = 1
                    s_state = 1
                    s_cf = 1
                    phi_s = nh[1][1]["phi_s"]
                    p_ij = nh[1][1]["p_ij"]
                

    if s_state == 1:
        dc = {"s_state": s_state, "s_cf" : s_cf, "s_pf":s_pf, "p_ij":p_ij, "phi_s" : phi_s}
        return dc
        
    return nh[1][1]


def run(n_rows, n_cols):
    # inicializar el grid
    grid = [[cell_init() for j in range(n_cols + 2)] for i in range(n_rows + 2)]
    
    # inicialización de los obstáculos
    for i in range(n_rows +2):
        grid[i][0]         = obstacle_init()
        grid[i][n_cols +1] = obstacle_init()
    
    for j in range(n_cols + 2):
        grid[n_rows + 1][j] = obstacle_init()
        grid[0][j]          = obstacle_init()
        
    
    new_grid = grid.copy()
    
    #ciclo de barrido sobre toda la teselación
    for i in range(1,n_rows+1):
        for j in range(1,n_cols+1):
            # seleccionamos la vecindad
            nh = extract_neighbourhood(i,j)
            
            #aplicamos la regla de evolución
            evol = rules(nh)
            
            # 
            
        
    