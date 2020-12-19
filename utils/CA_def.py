import copy

def cell_init():
    return {"s_state":  0, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0}

def obstacle_init():
    return {"s_state": -1, "s_cf" : 0, "s_pf":0, "p_ij":(0,0), "phi_s": 0}

# i, j empiezan desde 1!!!!!!
def extract_neighbourhood(grid, i,j):
    nh = [[grid[i +i_t][j + j_t] for j_t in range(-1,2)] for i_t in range(-1,2)]
    return nh

def delta(i,j):
    if (i+j)%2 == 0:
        return 2**(1/2)
    return 1

# función  para imprimir la vecindad con los prendidos solamente
def print_nh_up(nh):
    for i in range(3):
        for j in range(3):
            print(nh[i][j]["s_state"], end = "\t")
        print()

# barre de arriba a abajo, izquierda a derecha
def rules(nh):
    #print(s_pf)
    is_changed = False

    # si ya no hay nada más que pueda cambiar, esto es, ya es padre
    # ni tampoco cambiará cuando sea un obstáculo
    if nh[1][1]["s_pf"] == 1 or nh[1][1]["s_state"] == -1:
        return nh[1][1] , is_changed

    for i in range(3):
        for j in range(3):

            # hay una celda activa alrededor
            if nh[i][j]["s_state"] == 1:
                # la celda considerada no está activa
                if nh[1][1]["s_state"] == 0:
                    # se actualizan los estados
                    s_state = 1

                    #se vuelve chavo
                    s_cf = 1
                    #print("holiiiiiiii")
                    s_pf = 0
                    d = delta(i,j)

                    # si es la primera vez que encuentra a un vecino activo
                    if nh[1][1]["phi_s"] == 0:
                        phi_s = nh[i][j]["phi_s"] + d
                        #print(i,j)
                        # dirección
                        # como i,j son mayores que 0 y la vecindad debe
                        # tomar valores entre -1,1, les restamos 1
                        p_ij = (i -1,j -1)

                    # encontrar el mínimo de la distancia
                    if nh[i][j]["phi_s"] + d < phi_s:
                        # cambio de la distancia
                        phi_s = nh[i][j]["phi_s"] + d
                        # dirección
                        p_ij = (i -1,j -1)

                # cambia de padre a hijo
                else:
                    s_pf = 1
                    s_state = 1
                    s_cf = 1
                    phi_s = nh[1][1]["phi_s"]
                    p_ij = nh[1][1]["p_ij"]

                # hubo cambios a fuerzas
                is_changed = True


    #if s_state == 1:
    if is_changed:
        dc = {"s_state": s_state, "s_cf" : s_cf, "s_pf":s_pf, "p_ij":p_ij, "phi_s" : phi_s}
        return dc, is_changed

    return nh[1][1],is_changed


# encontrar el path entre el target y el pedestrian de acuerdo a la dirección a seguir
def find_path(grid, r_target, c_target, r_ped, c_ped):
    # +1 por que ambos empiezan en cero, y tenemos paredes en los extremos
    point = (r_ped +1, c_ped +1)
    path_ped2tar = [point]

    # siempre que el punto no corresponda al target
    while point != (r_target +1, c_target +1):

        # aproxima al siguiente número más pequeño distinto de 0 (salvo en
        # la posición del target)
        # solo tenemos la dirección  a la cual dirigirse
        p_ij = grid[point[0]][point[1]]["p_ij"]

        point = (point[0] + p_ij[0], point[1] + p_ij[1])

        path_ped2tar.append(point)
        #print(point[0], point[1])

    return path_ped2tar


# las posiciones (r_*, c_*) comienzan desde cero!!!
# l_obst es una lista de obstáculos, son pares de tuplas
def run(n_rows, n_cols, r_target,c_target , r_ped, c_ped, l_obst):
    # inicializar el grid
    grid = [[cell_init() for j in range(n_cols + 2)] for i in range(n_rows + 2)]

    # inicialización de los obstáculos
    for i in range(n_rows +2):
        grid[i][0]         = obstacle_init()
        grid[i][n_cols +1] = obstacle_init()

    for j in range(n_cols + 2):
        grid[n_rows + 1][j] = obstacle_init()
        grid[0][j]          = obstacle_init()

    # agregando los obstáculos en l_obst
    for pos in l_obst:
        grid[pos[0] +1][pos[1] +1] = obstacle_init()

    # para crear una copia
    new_grid = copy.deepcopy(grid)

    # array 2D para imprimir
    arr_tp = [[-1 for j in range(n_cols + 2)] for i in range(n_rows + 2)]

    # consideración del target
    dic_target = {"s_state":  1, "s_cf" : 1, "s_pf":1,
                  "p_ij":(r_target +1,c_target +1), "phi_s": 0}
    grid[r_target + 1][c_target + 1] = dic_target


    # impresión de la configuración inicial
    for i in range(n_rows +2):
        for j in range(n_cols +2):
            arr_tp[i][j] = round(grid[i][j]["phi_s"],2)

    for r in arr_tp: print(*r, sep = "\t");
    print("-------")


    # cambios
    is_changed = True
    # mientras haya cambios
    while is_changed:

        # considerar si hubo cambios en otros lados
        is_changed = False

        #ciclo de barrido sobre toda la teselación
        for i in range(1, n_rows+1):
            for j in range(1,n_cols+1):
                # seleccionamos la vecindad
                nh = extract_neighbourhood(grid, i , j)

                #aplicamos la regla de evolución y la asociamos a la evolución
                new_grid[i][j], change = rules(nh)

                # agregamos valores de verdad, con al menos un cambio
                # entonces es suficiente para seguir actualizando
                is_changed = is_changed or change

                # para actializar el array a imprimir
                arr_tp[i][j] = round(new_grid[i][j]["phi_s"],2)

                ######
                #if i == 2 and j == 5: print_nh_up(nh);return;
                #####

        # cambio de los grids
        tmp = grid
        grid = new_grid
        new_grid = tmp

        for r in arr_tp: print(*r, sep = "\t");
        print("--------")

    # si no hay camino, que lance un error uwu
    if grid[r_ped +1][c_ped +1]["s_state"] != 1:
        raise Exception("No path from pedestrian to target!!!")

    print("nothing wrong")
    path_ped2tar = find_path(grid, r_target, c_target, r_ped, c_ped)
    return path_ped2tar
