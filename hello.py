#少なくとも指定のキャラクターが1回以上出るガチャ確立プログラム
print("排出率は？(％)：")
percent = float(input())
print("引く回数は？(回)：")
times = float(input())
print("少なくとも１回以上出る確率は....")
answer = 1 - ((1 - percent / 100) ** float(times))
print("約" , int(answer*100) , "％です" , sep = "")