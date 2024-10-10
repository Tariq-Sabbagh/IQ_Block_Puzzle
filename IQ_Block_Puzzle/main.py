# from GUI import TheGame

from IQ_Block_Puzzle import get_Board

import test_GUI
import pygame
# import get_Board
# import get_bigcontour
# import GetPieces

stop = False
def DFS(board,visited,r,c):
    if r < 0 or c < 0 or r >= 8 or c >= 8 or visited[r][c] or board[r][c] != 0:
        # print(count)
        return 0
    visited[r][c] = True
    count=1
    count+=DFS(board,visited,r + 1, c)
    count+=DFS(board,visited,r - 1, c)
    count += DFS(board,visited,r, c + 1)
    count+=DFS(board,visited,r, c - 1)
    return count

def optemization(board):
    visited = [[False for _ in range(8)] for _ in range(8)]
    rows, cols = 8, 8
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0 and not visited[r][c]:
                # print(count)
                count = DFS(board, visited, r, c)
                if count == 1 or count == 2 or count == 4:
                    v=False
                    return False
    return True

def run(board,all_poisitions_list):
    global stop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not stop:
            test_GUI.draw(board)  # Initial draw
            runner(all_poisitions_list, board)
    pygame.quit()

# def draw(board):
#     # running = True
#     # while running:
#     #     grid=getboard()
#     #     for event in pygame.event.get():
#     #         if event.type == pygame.QUIT:
#     #             running = False
#
#         # Fill the screen with white
#         screen.fill((255, 255, 255))
#
#         # Draw the grid
#         for row in range(8):
#             for col in range(8):
#                 color = colors[board[row][col]]
#                 pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
#
#                 # Optional: Draw the grid lines
#                 pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)
#
#         # Update the display
#         pygame.display.flip()


def get_legal_squares(board, piece):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            _, legal_move = add_piece(board, piece, row, col)
            if legal_move:
                legal_moves.append((row, col))
    # print(f"Legal moves for piece: {legal_moves}")
    return legal_moves







def runner(allPieces, board):
    global stop
    if stop:
        # test_GUI.draw(board)
        return

    if all([all(row) for row in board]):
        print("Puzzle solved!")
        print_matrix(board)
        stop = True
        return

    if not allPieces:
        print("No more pieces left to place.")
        return

    pieces = allPieces[0]

    for i, piece in enumerate(pieces):
        legal_moves = get_legal_squares(board, piece)

        for x, y in legal_moves:
            newBoard, valid = add_piece(board, piece, x, y)
            if (optemization(newBoard)):
                if valid:
                    if not stop:
                        test_GUI.draw_with_fade(newBoard, piece, x, y)
                        # pygame.time.delay(test_GUI.delay_duration)
                        runner(allPieces[1:], newBoard)

# def solution(board):
#     if all([all(row) for row in board]):
#         print("Solution found:")
#         print_matrix(board)
#         return True
#     return False



def add_piece(board, piece, start_x, start_y):
    # التحقق من أن القطعة غير فارغة
    if not piece or not piece[0]:
        # print(f"Piece is invalid at position ({start_x}, {start_y}): {piece}")
        return board, False

    # التحقق من أبعاد القطعة
    if start_x < 0 or start_y < 0 or start_x + len(piece) > len(board) or start_y + len(piece[0]) > len(board[0]):
        # print(f"Piece out of bounds at position ({start_x}, {start_y}): {piece}")
        return board, False

    valid = True
    changed_squares = []

    for i, row in enumerate(piece):
        for j, val in enumerate(row):
            if val != 0:  # إذا كانت الخلية تحتوي على جزء من القطعة
                if board[start_x + i][start_y + j] != 0:
                    # print(f"Position occupied at ({start_x + i}, {start_y + j})")
                    return board, False  # إذا كانت الخلية مشغولة
                changed_squares.append((start_x + i, start_y + j, val))

    # نسخ اللوحة وتحديثها
    new_board = [row[:] for row in board]
    for changed_row, changed_col, val in changed_squares:
        new_board[changed_row][changed_col] = val  # تحديث اللوحة بالقطعة
    # print(f"Piece added at ({start_x}, {start_y}): {piece}")
    return new_board, valid


# دالة توليد التدويرات والانعكاسات لكل قطعة
def generate_piece_positions(pieces):
    all_positions = []
    for piece in pieces:
        all_positions.append(get_all_positions(piece))
    return all_positions

# دالة لتوليد جميع التدويرات والانعكاسات لقطعة واحدة
def get_all_positions(piece):
    positions = get_rotations(piece)
    for pos in positions:
        y_reflect = reflect_vertical(pos)
        x_reflect = reflect_horizontal(pos)
        if y_reflect not in positions:
            positions.append(y_reflect)
        if x_reflect not in positions:
            positions.append(x_reflect)
    return positions

# إزالة التكرارات
def remove_duplicates(matrix_list):
    unique_matrices = set(tuple(map(tuple, matrix)) for matrix in matrix_list)
    return [list(map(list, matrix)) for matrix in unique_matrices]

# دالة التدوير
def get_rotations(piece):
    rotations = [piece]
    for _ in range(3):
        piece = rotate_piece(piece)
        if piece not in rotations:
            rotations.append(piece)
    return rotations

# تدوير القطعة 90 درجة
def rotate_piece(piece):
    return [list(row)[::-1] for row in zip(*piece)]

# انعكاس أفقي
def reflect_horizontal(matrix):
    return [row[::-1] for row in matrix]

# انعكاس رأسي
def reflect_vertical(matrix):
    return matrix[::-1]


# طباعة اللوحة
def print_matrix(matrix):
    for row in matrix:
        out_row = []
        for cell in row:
            out_row.append(color_map[cell])
        print(" ".join(out_row))
    print("\n")


if __name__ == '__main__':
    # pices = (
    # #     # [],
    #
    #     [[1, 0, 0],  # |
    #      [1, 0, 0],  # |
    #      [1, 0, 0],  # |
    #      [1, 1, 1]   # |_ _ _
    #      ],
    #
    #
    # [[2, 0],  # |
    #  [2, 0],  # |
    #  [2, 0],  # |
    #  [2, 2]   # |_ _
    #  ],
    #
    # [
    # [3, 0],  # |
    # [3, 0],  # |
    # [3, 3]  # |_
    # ],
    #
    # [
    #     [4, 0],  # |
    #     [4, 4]   # |_
    # ],
    #
    # [
    #     [5, 0, 0],  # |
    #     [5, 0, 0],  # |
    #     [5, 5, 5]   # |_ _ _
    # ],
    #
    # [[6, 0],  # |
    #  [6, 0],  # |
    #  [6, 0],  # |
    #  [6, 6],  # |- - - -|
    #  [6, 6]   # |_ _ _ _|
    #  ],
    #
    # [
    #     [7, 0],  # |
    #     [7, 0],  # |
    #     [7, 7],  # |- -|
    #     [7, 7]   # |_ _|
    # ],
    # [
    #     [8, 0],  # |
    #     [8, 8],  # |-|
    #     [8, 8]   # |_|
    # ],
    #
    # [
    # [9, 9, 0],  # |- - -
    # [9, 9, 9],  # |_ _ _ _|
    # [9, 9, 9]  # |_ _ _ _|
    # ],
    #
    # [
    # [10, 10, 10]  # - - -
    # ],
    #
    #     [
    #         [11, 0],   # |
    #         [11, 11],  # |--
    #         [11, 0],   # |
    #         [11, 0]    # |
    #     ],
    #
    #     [
    #         [0,   0, 12],           # |
    #         [0,   0, 12],           # |
    #         [12, 12, 12], # |-------|
    #         [12,  0,  0],   # |
    #         [12,  0,  0]    # |
    #     ]
    #
    # )
    color_map = (
        "⬜️",
        "💗",
        "🟦",
        "🟪",
        "🟥",
        "⬛️",
        "🔵",
        "🟫",
        "🟧",
        "🟨",
        "💙",
        "🔷",
        "🟩"
    )
    # new_list=[]
    # new_list=get_all_positions(pices[1])
    # new_list = remove_duplicates(new_list)
    # # print_matrix_color(matrix)
    # # print_matrix(matrix)
    # board = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
    # board,t=add_pice(board,0,0,pices[11])
    # print_matrix_color(board)

    # board,t=add_pice(board,0,0,pices[4])
    # print_matrix_color(board)
    # print(t)

    # for i in new_list:
    #     runner(i)
    # solution
    # get_bigcontour.runCode()
    # board = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
    # board=get_Board.getBoard(board)
    # pices=GetPieces.get_piece()
    #
    # board = [
    #     [12, 12, 12, 6, 6, 6, 6, 6],
    #     [1, 3, 12, 6, 6, 2, 2, 11],
    #     [1, 3, 12, 12, 12, 2, 11, 11],
    #     [1, 3, 3, 7, 7, 2, 5, 11],
    #     [1, 1, 1, 7, 7, 2, 5, 11],
    #     [0, 0, 0, 7, 5, 5, 5, 0],
    #     [0, 0, 0, 7, 4, 4, 0, 0],
    #     [0, 0, 10, 10, 10, 4, 0, 0]]

    # board = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
    # print_matrix(board)
    # all_poisitions_list = generate_piece_positions(pices)
    # # run(board,all_poisitions_list)

    # runner(all_poisitions_list,board)
    # board = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
    # run(board)
    board,pieces= get_Board.run_getBoard()
    print_matrix(board)
    all_poisitions_list = generate_piece_positions(pieces)
    run(board,all_poisitions_list)



