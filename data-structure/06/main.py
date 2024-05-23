from copy import deepcopy

def read_board_state(path):
    state_str = open(path, 'r').readline()
    # print(state_str)
    board_state = state_str.split(',')
    # print_board_state(board_state)
    return board_state

def print_board_state(board):
    for row in range(0,7):
        if(row % 2 == 0):
            print('+-----+-----+-----+')
        else:
            start_id = (row//2)*3
            print(f'|{board[start_id]:>{3}}  |{board[start_id+1]:>{3}}  |{board[start_id+2]:>{3}}  |')

def move_atas(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id+3]
    new_state[current_zero_id+3] = '0'
    return new_state

def move_bawah(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id-3]
    new_state[current_zero_id-3] = '0'
    return new_state

def move_kiri(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id+1]
    new_state[current_zero_id+1] = '0'
    return new_state

def move_kanan(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id-1]
    new_state[current_zero_id-1] = '0'
    return new_state

def update_queue_and_visited(queue, visited, new_state, move, current_state_key):
    visited_key = ','.join(new_state)
    # cek apa pernah visit state ini
    if(visited.get(visited_key)==None):
        # belum pernah, masuk queue
        queue.append([new_state, move])
        visited[visited_key]=[True, current_state_key, move]

def BFS(init_state:list, goal_state:list):
    queue = [[init_state, None]]
    visited = {','.join(init_state):True}
   
    while queue:
        current_state, move = queue[0]
        current_state_key = ','.join(current_state)
        queue.pop(0)
        current_zero_id = current_state.index('0')

        if(current_state == goal_state):
            print('found solution')
            break

        # cek available move
        
        # tile pindah ke atas
        if(current_zero_id < 6):
            new_state = move_atas(current_state, current_zero_id)
            update_queue_and_visited(queue, visited, new_state, 'up', current_state_key)
            # print(len(queue))
        
        # tile pindah bawah
        if(current_zero_id > 2):
            new_state = move_bawah(current_state, current_zero_id)

            # cek apa ini goal state?
            update_queue_and_visited(queue, visited, new_state, 'down', current_state_key)
            # print(len(queue))

        # tile pindah kiri
        if(current_zero_id%3 < 2):
            new_state = move_kiri(current_state, current_zero_id)

            # cek apa ini goal state?
            update_queue_and_visited(queue, visited, new_state, 'left', current_state_key)
            # print(len(queue))

        # tile pindah kanan
        if(current_zero_id%3 > 0):
            new_state = move_kanan(current_state, current_zero_id)

            # cek apa ini goal state?
            update_queue_and_visited(queue, visited, new_state, 'right', current_state_key)

    path_key = ','.join(goal_state)
    init_key = ','.join(init_state)
    paths = []
    print_board_state(new_state)
    while path_key != init_key:
        _, new_key, move = visited[path_key]
        # print(new_key, move)
        paths.append((new_key, move))
        # state = new_key.split(',')
        # print_board_state(state)
        path_key = new_key
    # print(visited)
    counter = 1
    for state_key, move in paths[::-1]:
        state = state_key.split(',')
        print(f'{counter}. Move:{move}')
        counter+=1
        # print_board_state(state)


def main():
    init_state = read_board_state('start.txt')
    goal_state = read_board_state('goal.txt')
    print('START')
    print_board_state(init_state)
    print('GOAL')
    print_board_state(goal_state)

    # start searching
    print('Begin search ... ')
    BFS(init_state, goal_state)

if __name__ == "__main__":
    main()
