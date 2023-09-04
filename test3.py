def josephus(n, k):
    survivor = 0

    # 開始從 2 到 n 依次計算存活者的位置
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    # 因為陣列從 0 開始，所以將最終答案加一
    return survivor + 1


if __name__ == "__main__":
    """
    1 2 3 4 5
    1 2 4 5
    2 4
    4
    """
    # 輸入總共的同事數和報數的k值
    n = int(input("請輸入同事的總數："))
    k = 3  # 根據題目，報數固定為3

    # 呼叫josephus函數計算最後留下的同事的順位
    result = josephus(n, k)

    print(f"最後留下的同事是第 {result} 順位。")
    
    
