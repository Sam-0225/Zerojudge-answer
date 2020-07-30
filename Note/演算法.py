#https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E8%AB%87%E4%BB%80%E9%BA%BC%E6%98%AF%E6%BC%94%E7%AE%97%E6%B3%95%E5%92%8C%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6-b1f6908e4b80
#時間複雜度 (Time Complexity)


def move():
    pass


N = 10
for i in range(1, N+1):  # O(n)
    move()

for i in range(1, N+1):  # O(n²)
    for j in range(1, N+1):
        move()

for i in range(1, N+1):  # O(n²)
    for j in range(1, N+1):
            move()

# !大 O 符號紀錄的時間複雜度時，有一個很重要的原則，也就是要「盡可能化簡」。
# 上述共 2n² + n 個步驟的程式，我們會把它的時間複雜度簡單記成 O(n²)。
# *為何 2n² + n 個步驟的程式，我們會將它的時間複雜度記的跟兩倍步驟數（ 4n² + 2n ）一樣，都是 O(n²) 呢？

# !演算法的速度不是以秒計算，而是以步驟次數