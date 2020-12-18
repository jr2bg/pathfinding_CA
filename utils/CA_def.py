def cell_init():
  return {"s_state":  0, "s_cf" : 0, "s_pf":0, "t_on" : 0, "p_ij":0, "phi_s": 0}

def obstacle_init():
  return {"s_state": -1, "s_cf" : 0, "s_pf":0, "t_on" : 0, "p_ij":0, "phi_s": 0}
    
def extract_neighbourhood(grid, i,j):
  nh = [[grid[i+i_t][j + j_t] for i_t in range(3)] for j_t in range(3)]
  return nh
    
    
def delta(i,j):
  if (i+j)%2 == 0:
    return 2**(1/2)
  return 1

def rules(nh, t):
  # requerimos que el tiempo de activación al principio sea diferente al tiempo considerado
  t_on = t + 1
    
  # determina si se cambió algo o ño
  is_changed = False


  # cambia de padre a hijo
  if nh[1][1]["s_state"] == 1 and nh[1][1]["t_on"] < t and nh[1][1]["s_pf"]= 0:
        
    # cambiamos a estatus de padre
    nh[1][1]["s_pf"] = 1
        
    # hubo un cambio
    is_changed = True
        
    return nh[1][1], is_changed
      
  # cuando ya no hay más cambios posibles
  elif nh[1][1]["s_state"] == 1 and nh[1][1]["t_on"] < t and nh[1][1]["s_pf"]= 1:
    return nh[1][1], is_changed


  # barriendo sobre toda la vecindad    
  for i in range(3):
    for j in range(3):
            
      # hay una celda activa en la vecindad que prendió a tiempo anterior al actual
      if nh[i][j]["s_state"] == 1 and nh[i][j]["t_on"] < t:

        # la celda considerada no está activa
        # o se actualizó en el mismo tiempo que se está considerando
        if nh[1][1]["s_state"] == 0 or (nh[1][1]["s_state"] == 1 and t_on == t):
          # hay un cambio
          is_changed = True
                  
          # se actualizan los estados
          s_state = 1
          # tiene un  tiempo de prendido
          t_on = t

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

        

  # condiciones de retorno:
  # en este caso o NO cambia para nada de su estatus de casilla vacía o
  # cambia por la parte 
  if s_state == 1:
    dc = {"s_state": s_state, "s_cf" : s_cf, "s_pf":s_pf, "t_on" = t_on, "p_ij":p_ij, "phi_s" : phi_s}
    return dc, is_changed
        
  return nh[1][1], is_changed


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

    prev_changes 
    
    #ciclo de barrido sobre toda la teselación
    for i in range(1,n_rows+1):
        for j in range(1,n_cols+1):
            # seleccionamos la vecindad
            nh = extract_neighbourhood(i,j)
            
            #aplicamos la regla de evolución
            evol = rules(nh)
            
            # 
            
        
    
