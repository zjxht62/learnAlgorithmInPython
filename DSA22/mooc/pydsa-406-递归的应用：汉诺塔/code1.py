# 汉诺塔问题
def move_tower(height, fromPole, withPole, toPole):
    if height >= 1:
        move_tower(height -1, fromPole, toPole, withPole)
        move_disk(height, fromPole, toPole)
        move_tower(height-1, withPole, fromPole, toPole)

def move_disk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

move_tower(3, '#1', '#2', '#3')