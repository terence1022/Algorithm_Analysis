def bucket_sort(A):
    n = len(A)
    B = [[] for i in range(n)] # 建立 n 個空的桶子（每個桶子是一個 list）

    # 將陣列 A 中的元素分配到對應的桶中
    for i in range(n):
        index = min(int(n * A[i]), n - 1) # 計算應該放入的桶的索引
        B[index].append(A[i])

    # 對每個桶子進行排序
    for i in range(n):
        B[i].sort() # 可用插入排序或 Python 內建的排序

    result = []

    # 將所有排序後的桶子合併成一個結果陣列
    for i in range(n):
        result.extend(B[i])

    return result

if __name__ == '__main__':
    A = [5, 2, 8, 4, 9, 1]
    result = bucket_sort(A)
    print(result)