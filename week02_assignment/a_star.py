import hou
import math
import sys
import random

sys.path.append(r"C:\Users\phile\development\rAML\a_star\scripts")

from a_star import AStarPathFinding

def get_maze_from_grid():
    grid = hou.pwd().parm('grid_path').eval()
    geo = hou.node(grid).geometry()
    
    prims = geo.prims()
    num_rows = num_cols = int(math.sqrt(len(prims)))
    
    grid_matrix = []
    
    for row in range(num_rows):
        new_row = []
        for col in range(num_cols):
            prim_index = row * num_cols + col
            prim = geo.prim(prim_index)
            color = prim.attribValue("Cd")
            new_row.append(1 if color == (1.0,1.0,1.0) else 0)
        grid_matrix.append(new_row)
        
    return(grid_matrix)
    


def position_object(obj_path, row, col, cell_size=1):
    main_char = hou.node(obj_path)
    world_x = col * cell_size
    world_z = row * cell_size
    
    center = main_char.parmTuple("t").eval()
    main_char.parmTuple("t").set((world_x, 0, world_z))
    pos = (row, col)
    return pos
    
def valid_cells():
    maze = get_maze_from_grid()
    val_cells = []
    row_index = 0
    for row in maze:
        col_index = 0
        for col in row:
            if col == 1:
                val_cells.append((row_index,col_index))
            col_index += 1
        row_index += 1
    val_cells.remove((6,1))
    return val_cells
    
def random_valid():
    v_cells = valid_cells()
    rand_val_cell = v_cells[random.randint(0, len(valid_cells())-1)]
    return rand_val_cell

    
def solve_maze():
    main_char_path = hou.pwd().parm("main_char").eval()
    
    maze = get_maze_from_grid()
    print("")  
    
    npcCount = hou.pwd().parm("npcs").eval()
    
    i = 1
    for npc in range(npcCount):
        rv_cell = random_valid()    
        npc_char_path = hou.pwd().parm("npc_"+ str(i)).eval()
        #print(npc_char_path)
        
        start_pos = position_object(npc_char_path, rv_cell[0], rv_cell[1])
        target_pos = position_object(main_char_path, 6, 1)
      
        pathFinder = AStarPathFinding(maze, start_pos, target_pos)
        path = pathFinder.find_path()
    
        if path:
            print("Path found: ", path)
        else:
            print("No path found!")
        i += 1  
