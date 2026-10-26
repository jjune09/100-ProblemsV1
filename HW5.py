def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    from collections import deque
    rows, cols = len(maze), len(maze[0])
    
    directions = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    
    if not start or not end:
        return {"distance": -1, "path": []}
    
    q = deque()
    q.append((start[0], start[1], 0, [list(start)]))  # row, col, dist, path
    visited = set()
    visited.add(start)
    
    while q:
        r, c, dist, path = q.popleft()
        
        if (r, c) == end:
            return {"distance": dist, "path": path}
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            ndist = dist + 1
            npath = path + [[nr, nc]]
            
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                
                cr, cc = nr, nc
                conveyor_path = []
                
                
                while maze[cr][cc] in directions:
                    ddr, ddc = directions[maze[cr][cc]]
                    cr2, cc2 = cr + ddr, cc + ddc
                    if not (0 <= cr2 < rows and 0 <= cc2 < cols): 
                        break
                    if maze[cr2][cc2] == '#': 
                        break
                    conveyor_path.append([cr2, cc2])
                    cr, cc = cr2, cc2
                
                final_pos = (cr, cc)
                if final_pos not in visited:
                    visited.add(final_pos)
                    q.append((cr, cc, ndist, npath + conveyor_path))
    
    return {"distance": -1, "path": []}
    pass

if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}
    
    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2],
    #  [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}