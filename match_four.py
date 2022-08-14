def draw_bord(r, c):
    return [[None for _ in range(c)] for _ in range(r)]


def print_bord(f):
    [print([x if x else 0 for x in y]) for y in f]


def user_input(player):
    return int(input(f'Player {player}, please choose a column!')) - 1


def do_the_move(col, player, field, free_rows):
    if free_rows[col] != -1:
        field[free_rows[col]][col] = player
        free_rows[col] -= 1
    return field, (free_rows[col], col)


def print_winner(player):
    print(f'Player {player} wins!')


def play_again(new_field='', to_start_first=1, to_start_second=2):
    command = input('Press 1 to play again, press 2 for exit!')
    while command not in ('1', '2'):
        command = input('Press 1 to play again, press 2 for exit!')
    if command == '1':
        play(new_field, to_start_second, to_start_first)
    exit()


def normalize_player_pos(player, look_at, field):
    lst = []
    for i in deltas:
        pos_row = look_at[0] + 1
        pos_col = look_at[1]
        row_delta, col_delta = i[0], i[1]
        while 0 <= pos_row < len(field) and 0 <= pos_col < len(field[0]) and field[pos_row][pos_col] == player:
            pos_row -= row_delta
            pos_col -= col_delta
        lst.append((pos_row + row_delta, pos_col + col_delta))
    return lst


def check_for_win_condition(player, look_at, field):
    lst = []

    for index, i in enumerate(deltas):
        counter = 0
        pos_row = look_at[index][0]
        pos_col = look_at[index][1]
        row_delta, col_delta = i[0], i[1]
        while 0 <= pos_row < len(field) and 0 <= pos_col < len(field[0]) and field[pos_row][pos_col] == player:
            counter += 1
            pos_row += row_delta
            pos_col += col_delta
        lst.append(counter == need_to_connect)
    return any(lst)


def play(field, current_player=1, other_player=2):
    # current_player, other_player = 1, 2
    free_rows = [len(field) - 1] * len(field[0])
    while True:
        current_player_input = user_input(current_player)
        field, pos = do_the_move(current_player_input, current_player, field, free_rows)
        print_bord(field)
        pos = normalize_player_pos(current_player, pos, field)
        if check_for_win_condition(current_player, pos, field):
            print_winner(current_player)
            play_again(draw_bord(bord_rows, bord_columns), current_player, other_player)
        else:
            current_player, other_player = other_player, current_player


# SETTINGS #
need_to_connect = 4
bord_rows = 6
bord_columns = 7
# SETTINGS #

bord = draw_bord(bord_rows, bord_columns)

deltas = (
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1)
)

play(bord)
