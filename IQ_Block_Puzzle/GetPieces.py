
pices = (
        # [],

        [[1, 0, 0],  # |
         [1, 0, 0],  # |
         [1, 0, 0],  # |
         [1, 1, 1]   # |_ _ _
         ],


    [[2, 0],  # |
     [2, 0],  # |
     [2, 0],  # |
     [2, 2]   # |_ _
     ],

    [
    [3, 0],  # |
    [3, 0],  # |
    [3, 3]  # |_
    ],

    [
        [4, 0],  # |
        [4, 4]   # |_
    ],

    [
        [5, 0, 0],  # |
        [5, 0, 0],  # |
        [5, 5, 5]   # |_ _ _
    ],

    [[6, 0],  # |
     [6, 0],  # |
     [6, 0],  # |
     [6, 6],  # |- - - -|
     [6, 6]   # |_ _ _ _|
     ],

    [
        [7, 0],  # |
        [7, 0],  # |
        [7, 7],  # |- -|
        [7, 7]   # |_ _|
    ],
    [
        [8, 0],  # |
        [8, 8],  # |-|
        [8, 8]   # |_|
    ],

    [
    [9, 9, 0],  # |- - -
    [9, 9, 9],  # |_ _ _ _|
    [9, 9, 9]  # |_ _ _ _|
    ],

    [
    [10, 10, 10]  # - - -
    ],

        [
            [11, 0],   # |
            [11, 11],  # |--
            [11, 0],   # |
            [11, 0]    # |
        ],

        [
            [0,   0, 12],           # |
            [0,   0, 12],           # |
            [12, 12, 12], # |-------|
            [12,  0,  0],   # |
            [12,  0,  0]    # |
        ]

    )
new_list=[]
new_pieces=[]
def get_piece(indexPices):
    global new_pices
    # print(indexPices)
    for index in indexPices:
        new_list.append(pices[index-1])
    for pice in pices:
        if pice not in new_list:
            new_pieces.append(pice)

    return new_pieces
    #
    # for row in new_pieces:
    #     print(row,"\n")


        # new_pices = tuple(None if idx == row else item for idx, item in enumerate(pices))
    # print(new_pices)
    # return new_pices

