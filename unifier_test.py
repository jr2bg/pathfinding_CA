from utils.CA_def import *
from utils.reader_maze import *



if __name__ == "__main__":
    # n_rows = 4
    # n_cols = 5
    # r_target = 1
    # c_target = 3
    # r_ped = 3
    # c_ped = 1

    #l_obst = [(2,0), (2,1), (2,3), (1,2)]
    #l_obst = []
    path_csv = "/home/jr2bg/Documents/masters/CIC/thesis/ai-maze-python/mazes/maze0.csv"
    chr_obs = "0"
    n_rows, n_cols, l_obst = read_maze_csv(path_csv, chr_obs = chr_obs)
    r_target = 0
    c_target = 0
    r_ped = n_rows -1
    c_ped = n_cols -1

    path_ped2tar = run(n_rows, n_cols, r_target,c_target ,r_ped,c_ped, l_obst)
    print(path_ped2tar)
