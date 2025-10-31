import random
import datetime

# 使用当前日期时间生成seed
now = datetime.datetime.now()
seed_value = int(now.strftime("%Y%m%d%H%M%S"))
random.seed(seed_value)

# 定义可选的三位组合
options = ["000", "001", "010", "011", "100", "101", "110", "111"]

# 生成6组随机结果
random_groups = [random.choice(options) for _ in range(6)]

print(now)
print("\n卦象: ")

# 根据不同随机结果输出对应的符号
for code in random_groups:
    if code == "000":
        print("─── ───   ⭕")
    elif code == "111":
        print("───────   ❌")
    elif code in ["001", "010", "100"]:
        print("───────")
    else:
        print("─── ───")
