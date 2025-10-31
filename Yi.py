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
for code in random_groups[::-1]:
    if code == "000":
        print("─── ───   ⭕")
    elif code == "111":
        print("───────   ❌")
    elif code in ["001", "010", "100"]:
        print("───────")
    else:
        print("─── ───")




# guaxiang 数组，判断阴阳
guaxiang = ["1" if code.count("1") % 2 == 1 else "0" for code in random_groups]

lower_three = guaxiang[:3]
upper_three = guaxiang[3:]


bagua_names = {
    ("1","1","1"): "☰ 乾 (Qián - 天)",
    ("0","0","0"): "☷ 坤 (Kūn - 地)",
    ("0","1","0"): "☵ 坎 (Kǎn - 水)",
    ("1","0","1"): "☲ 离 (Lí - 火)",
    ("1","0","0"): "☳ 震 (Zhèn - 雷)",
    ("0","0","1"): "☶ 艮 (Gèn - 山)",
    ("0","1","1"): "☴ 巽 (Xùn - 风)",
    ("1","1","0"): "☱ 兑 (Duì - 泽)"
}

# 获取上卦、下卦的卦名
upper_name = bagua_names.get(tuple(upper_three), "未知上卦")
lower_name = bagua_names.get(tuple(lower_three), "未知下卦")

print("上卦：", upper_name)
print("下卦：", lower_name)


