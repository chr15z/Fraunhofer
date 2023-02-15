import cv2
import numpy as np

img000 = cv2.imread("Resources/005.png")

img0 = cv2.imread("Resources/0.png")
img1 = cv2.imread("Resources/1.png")
img2 = cv2.imread("Resources/2.png")
img3 = cv2.imread("Resources/3.png")
img4 = cv2.imread("Resources/4.png")
img5 = cv2.imread("Resources/5.png")
img6 = cv2.imread("Resources/6.png")
img7 = cv2.imread("Resources/7.png")
img8 = cv2.imread("Resources/8.png")
img9 = cv2.imread("Resources/9.png")

s1 = [[0, 0, 0, 0, 0, 7, 0, 3, 0],
      [0, 0, 0, 0, 0, 0, 5, 0, 0],
      [0, 5, 9, 0, 0, 2, 7, 0, 0],
      #
      [1, 0, 0, 4, 0, 0, 0, 0, 8],
      [0, 2, 0, 0, 0, 5, 0, 0, 0],
      [0, 4, 3, 8, 0, 0, 0, 6, 0],
      #
      [9, 3, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 7, 0, 8, 2, 0],
      [0, 8, 0, 9, 4, 0, 0, 0, 5]
      ]


def img_2_arr(img, size):
    resized_img = cv2.resize(img, (size, size))
    arr = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            arr[x][y] = resized_img[x][y][0]
    return arr


def show_img(img):
    while True:
        cv2.imshow("input img", img)
        if cv2.waitKey(1) == ord("q"):
            break


arr_zero = img_2_arr(img0, 25)
arr_one = img_2_arr(img1, 25)
arr_two = img_2_arr(img2, 25)
arr_three = img_2_arr(img3, 25)
arr_four = img_2_arr(img4, 25)
arr_five = img_2_arr(img5, 25)
arr_six = img_2_arr(img6, 25)
arr_seven = img_2_arr(img7, 25)
arr_eight = img_2_arr(img8, 25)
arr_nine = img_2_arr(img9, 25)


def create_sudoku(arr):
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    for x in range(9):
        for y in range(9):
            sudoku[y][x] = what_num(arr, x, y)
    return sudoku


def what_num(arr, x, y):
    x *= 25
    y *= 25
    sad_zero = get_sad(arr, arr_zero, x, y)
    sad_one = get_sad(arr, arr_one, x, y)
    sad_two = get_sad(arr, arr_two, x, y)
    sad_three = get_sad(arr, arr_three, x, y)
    sad_four = get_sad(arr, arr_four, x, y)
    sad_five = get_sad(arr, arr_five, x, y)
    sad_six = get_sad(arr, arr_six, x, y)
    sad_seven = get_sad(arr, arr_seven, x, y)
    sad_eight = get_sad(arr, arr_eight, x, y)
    sad_nine = get_sad(arr, arr_nine, x, y)
    min_value = min(sad_zero, sad_one, sad_two, sad_three, sad_four, sad_five, sad_six, sad_seven, sad_eight, sad_nine)
    if min_value == sad_zero:
        return 0
    if min_value == sad_one:
        return 1
    if min_value == sad_two:
        return 2
    if min_value == sad_three:
        return 3
    if min_value == sad_four:
        return 4
    if min_value == sad_five:
        return 5
    if min_value == sad_six:
        return 6
    if min_value == sad_seven:
        return 7
    if min_value == sad_eight:
        return 8
    if min_value == sad_nine:
        return 9
    return 10


def get_sad(sudoku_arr, num_arr, width, height):    # sum of absolute difference
    sad = np.uint64(0)

    for i in range(len(num_arr)):
        for j in range(len(num_arr)):
            sad += abs(num_arr[i][j] - sudoku_arr[i + height][j + width])

    return sad


def print_sudoku(arr):
    for row in range(9):
        for col in range(9):
            if col % 3 != 2:
                print(str(arr[row][col]), end=" ")
            else:
                if col != 8:
                    print(str(arr[row][col]), end=" | ")
                else:
                    print(str(arr[row][col]), end=" ")
        print("")
        if row % 3 == 2 and row != 8:
            print("------|-------|------")
    print("")


def is_num_possible(row, col, num, arr):
    for row_i in range(9):
        if arr[row_i][col] is num:
            return False
    for col_i in range(9):
        if arr[row][col_i] is num:
            return False
    upper_left_row = (row // 3) * 3
    upper_left_col = (col // 3) * 3
    for row_i in range(3):
        for col_i in range(3):
            if arr[upper_left_row + row_i][upper_left_col + col_i] == num:
                return False
    return True


def solve_sudoku(arr):
    for row_i in range(9):
        for col_i in range(9):
            if arr[row_i][col_i] == 0:
                for num in range(1, 10):
                    if is_num_possible(row_i, col_i, num, arr):
                        arr[row_i][col_i] = num
                        solve_sudoku(arr)
                        arr[row_i][col_i] = 0
                return
    print("Solved Sudoku:")
    print_sudoku(arr)


#####################################


arr_img000 = img_2_arr(img000, 225)
new_s0 = create_sudoku(arr_img000)

print_sudoku(new_s0)
solve_sudoku(new_s0)
show_img(img000)
