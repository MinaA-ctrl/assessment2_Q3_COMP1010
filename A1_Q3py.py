def check_matrix(lst):
    k = len(lst[0])
    for i in lst:
        if k != len(i):
            b = False
            return b
    b  = True

def convert_to_matrix(n):
    mat = []
    mat = n.split(",")
    k = 0
    for i in mat:
        mat[k] = i.split()
        k += 1
    return mat

def matrix_size(lst):
    h = 0
    w = len(lst[0])
    for i in lst:
        h += 1
    size = [h, w]
    return size

def check_if_can_be_multiplied(size_1, size_2):
    can = False
    if size_1[1] == size_2[0]:
        can = True
    return can

def matrix_multiplication(first_multiple, second_multiple):
    if check_if_can_be_multiplied(first_multiple["size"], second_multiple["size"]) == False:
        print("This multiplication isn't possible")
        return
    result = []
    a = first_multiple["size"][0]
    b = first_multiple["size"][1]
    c = second_multiple["size"][1]
    for i in range(a):
        row = []
        for j in range(c):
            number = 0
            for l in range(b):
                number += int(first_multiple["matrix"][i][l]) * int(second_multiple["matrix"][l][j])
            row.append(number)
        result.append(row)
    return result

def trace(matrix):
    sum = 0
    if matrix["size"][0] >= matrix["size"][1]:
        k = matrix["size"][1]
    else:
        k = matrix["size"][0]
    for i in range(k):
        sum += matrix["matrix"][i][i]
    return sum

def input_matrix():
    right_matrix = False
    k = 0
    while right_matrix == False:
        if k == 0:
            a = input("Input numbers for matrix A (to go to next row write ','): ")
            k += 1
        else:
            a = input("Wrong matrix \n Input numbers for matrix A (to go to next row write ','): ")
        matrix_a = convert_to_matrix(a)
        right_matrix = check_matrix(matrix_a)
        size_A = matrix_size(matrix_a)
    A = {"matrix": matrix_a, "size": size_A}
    k = 0
    right_matrix = False
    while right_matrix == False:
        if k == 0:
            b = input("Input numbers for matrix B (to go to next row write ','): ")
            k += 1
        else:
            b = input("Wrong matrix \n Input numbers for matrix B (to go to next row write ','): ")
        matrix_b = convert_to_matrix(b)
        right_matrix = check_matrix(matrix_b)
        size_B = matrix_size(matrix_b)
    B = {"matrix": matrix_b, "size": size_B}
    print(A, B)
    return A, B

def devide_by_6(matrix):
    result = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j/6)
        result.append(row)
    return result

def compare(tri, tra, k):
    print(tra)
    if tri < tra:
        print(f"Triagonals of {k} less then a trace of ({k}^3)/6")
    elif tri == tra:
        print(f"Triagonals of {k} equal to trace of ({k}^3)/6")
    else:
        print(f"Triagonals of {k} less then a trace of ({k}^3)/6")

def main():
    a = {"matrix": [[0, 1, 1, 0, 0, 0], 
                    [1, 0, 1, 1, 1, 0], 
                    [1, 1, 0, 0, 1, 1], 
                    [0, 1, 0, 0, 1, 0], 
                    [0, 1, 1, 1, 0, 1], 
                    [0, 0, 1, 0, 1, 0]], "size": [6, 6]}
    b = {"matrix": [[0, 1, 1, 0, 0], 
                    [1, 0, 1, 1, 0], 
                    [1, 1, 0, 0, 1], 
                    [0, 1, 0, 0, 1], 
                    [0, 0, 1, 1, 0]], "size": [5, 5]}
    c = {"matrix": [[0, 1, 1, 1, 1], 
                    [1, 0, 1, 1, 1], 
                    [1, 1, 0, 1, 1], 
                    [1, 1, 1, 0, 1], 
                    [1, 1, 1, 1, 0]], "size": [5, 5]}
    a_triangles = 4
    b_triangles = 1
    c_triangles = 10
    a_pow_2 = matrix_multiplication(a, a)
    a_pow_2_size = matrix_size(a_pow_2)
    a_2 = {"matrix": a_pow_2, "size": a_pow_2_size}
    b_pow_2 = matrix_multiplication(b, b)
    b_pow_2_size = matrix_size(b_pow_2)
    b_2 = {"matrix": b_pow_2, "size": b_pow_2_size}
    c_pow_2 = matrix_multiplication(c, c)
    c_pow_2_size = matrix_size(c_pow_2)
    c_2 = {"matrix": c_pow_2, "size": c_pow_2_size}
    #need to give size to the pow_2
    a_pow_3 = matrix_multiplication(a_2, a)
    b_pow_3 = matrix_multiplication(b_2, b)
    c_pow_3 = matrix_multiplication(c_2, c)
    final_a = {"matrix": devide_by_6(a_pow_3), "size": matrix_size(devide_by_6(a_pow_3))}
    final_b = {"matrix": devide_by_6(b_pow_3), "size": matrix_size(devide_by_6(b_pow_3))}
    final_c = {"matrix": devide_by_6(c_pow_3), "size": matrix_size(devide_by_6(c_pow_3))}
    trace_a = trace(final_a)
    trace_b = trace(final_b)
    trace_c = trace(final_c)
    compare(a_triangles, trace_a, "a")
    compare(b_triangles, trace_b, "b")
    compare(c_triangles, trace_c, "c")

main()