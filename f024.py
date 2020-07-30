"""
f024: Problem D. 乒乓大賽

殿壬是個天才兒童，他除了喜歡貓咪、蝴蝶、亮亮的燈泡、還喜歡打乒乓球。
今天他跟他的好朋友，瑤瑤，打了一場乒乓球比賽。對了，瑤瑤她很喜歡畫畫，因為這樣可以為殿壬打氣，不過這又是另一回事了。
乒乓球比賽的規則是這樣子的：每一局雙方從 0 分開始，每一球都會由殿壬或是瑤瑤得分，而在一局之中先同時達成以下兩個條件的人就會贏得這一局：
第一個條件是至少得到 11 分，第二個條件是得分數比對方多至少 2 分。而這是一場三局兩勝的乒乓球比賽，也就是說當有人贏得兩局，比賽就結束了。
殿壬跟瑤瑤比完一場精彩的比賽後，想要回顧這場比賽，卻發現他們沒有紀錄每球的得分者是誰。但是，雙方都記得自己在整場比賽中總共得了幾分，他們也記得誰獲得了勝利。不過，殿壬跟瑤瑤的記憶力都不是很好，他們有可能記錯了。請問根據他們提供的資訊，你能判斷他們是不是一定記錯了嗎？

第一行會有一個整數 T，代表總共有幾筆測試資料。
接下來 T 筆測試資料中，每一行有三個正整數 A,B,W，分別代表殿壬所記得的自己的總得分數，瑤瑤所記得的自己的總得分數，以及這場比賽的贏家( 1 代表殿壬，2 代表瑤瑤)。
1≤T≤30
0≤A,B≤100000

對於每一筆測試資料，請輸出一字串 "YES" 或 "NO" (不含引號)。輸出 "YES" 代表他們記得的比賽情形是有可能發生的，輸出 "NO" 代表他們記得的比賽情形是不可能發生的。

"""


def judge(a, b, w):
    out = 'No'
    if a == 22 and b <= 18 and w == 1:
        out = 'Yes'
    elif a > 22 and (b == a - 2 or b == a - 4) and w == 1:
        out = 'Yes'
    else:
        if 2 <= a - b <= 11 and w == 1:
            out = 'Yes'


T = int(input())
for _ in range(T):

    A, B, W = map(int, input().split())
    if A > B:
        judge(A, B, W)
    else:
        if W == 1:
            judge(B, A, 2)
        else:
            judge(B, A, 1)
"""
未完成
"""