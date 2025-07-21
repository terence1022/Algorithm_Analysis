def counting_sort(A, digit_place):
    n = len(A)
    output = [0] * n # 用來儲存排序結果的暫存陣列
    count = [0] * 10 # 因為數字的每一位是 0-9，共 10 個數字

    # 計算每個數字在當前位數上的出現次數
    for i in range(n):
        digit = (A[i] // digit_place) % 10
        count[digit] += 1

    # 更新 count，使其包含「小於等於」某個數字的數量
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 從右到左（為了保持穩定性）將數字放入 output
    for i in range(n - 1, -1, -1):
        digit = (A[i] // digit_place) % 10
        output[count[digit] - 1] = A[i]
        count[digit] -= 1

    # 將排序結果複製回原陣列
    for i in range(n):
        A[i] = output[i]

def radix_sort(A):
    # 找出最大值以判斷要排序幾位數
    max_num = max(A)
    digit_place = 1 # 從個位數開始

    # 持續對每一位數進行 Counting Sort
    while max_num // digit_place > 0:
        counting_sort(A, digit_place)
        digit_place *= 10

    return A

if __name__ == '__main__':
    A = [5, 2, 8, 4, 9, 1]
    radix_sort(A)
    print(A)