# 17:56시작 18:07답봄 도저히 안 떠오름
#

# 아래와 같이 리스트슬라이싱을 max값에 넣을수 있다.
# right_max = max(world[i+1:])


# 높높이 0도 아래에 벽으로 막혀있다고 보면 된다.
# h w

#중력에 맞게 물이 고이는 조건은 뭘까???
# 격리된 공간에서 가장 낮은 벽의 높이대로 고인다.
# 양끝 벽중에 더 낮은 벽의 높이대로 쌓인다.

# 특정 위치를 기준으로 앙옆에 자신보다 작은 높이의 블록이 있다면 해당위치에는 물이 고일 수 없다.
# 그리고 물이 고이는 양은 위 조건 충족이후 왼쪽 오른쪽벽의 높이에서 현재위치의 높이를 뺸만큼 고인다.

h, w = map(int, input().split())

world = list(map(int, input().split()))
water_total = 0
# i번째 좌표에 물이 얼마나 쌓여있을까 판단
for i in range(1, w-1):
    # 현재 위치보다 왼쪽
    left_max = max(world[:i])
    # 현재 위치보다 오른쪽
    right_max = max(world[i+1:])

    compare_min = min(left_max,right_max)

    # 물이 쌓일수 있는 조건
    if (compare_min >= world[i]):
        water_total += compare_min - world[i]
    # print(water_total)
print(water_total)




