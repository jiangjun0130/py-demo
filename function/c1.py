# 返回多个返回值


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


skill1_damage, skill2_damage = damage(3,6)
# 序列解包
print(skill1_damage, skill2_damage)

damages = damage(3,6)
# 不推荐使用下标获取结果
print(damages[0], damages[1])
print(type(damages))