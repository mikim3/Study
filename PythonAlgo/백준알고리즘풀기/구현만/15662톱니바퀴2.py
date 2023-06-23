# 230622 17:44시작 ~ 18:40 마무리

# 톱니 A가 돌았을떄 그옆에 A가 맞닿은 톱니의 극이 다르다면
# B는 A가 회전한 방향과 반대방향으로 회전하게 된다.

# 이 작용은 연쇄작용도 고려하여야 한다.
# 1번이 돈다면 그 옆에 2번도 그옆에 3번도 생각해야 한다.(돌아버린 톱니바퀴 옆에부터 순서대로 생각)


#  입력
# 가장 왼쪽 톱니부터 주어지고 톱니당  시계방향으로 12시부터 시계방향으로 8개 톱니로 주어진다.
# N극은 0 S극은 1이다.
#  그 다음줄로 회전횟수K가 주어짐
# 회전방법은 $(몇번째 바퀴 회전) $(어떤 방향회전?) 1는 시계방향 -1는 반시계방향이다.
#

# 회전하기 전에 옆에도 같이 회전할지를 결정한다.  회전 한 후에 결정X
#

# 옆에서 회전한거의 반대방향으로 회전한다.


# import sys
# input = sys.stdin.readline

# 톱니
t = int(input())
li = []
for i in range(t):
  li.append(list(input()))
# print(li, "\n")

# 회전횟수
k = int(input())

#
def rotate_t(t_select, dir, li):
  if (dir == 1):
    # print("dir == 1")
    # 한칸씩 뒤로 민다.
    tmp = li[t_select][7]
    for i in range(7, 0, -1):
      li[t_select][i] = li[t_select][i - 1]
    li[t_select][0] = tmp
    # print("한칸씩 뒤로밈", li)
  # 반시계방향
  elif (dir == -1):
    tmp = li[t_select][0]
    for i in range(7):
      li[t_select][i] = li[t_select][i+1]
    li[t_select][7] = tmp
    # print("한칸씩 앞으로 당김", li)
  print("rotate_t 결과", li)

for i in range(k):
  # 선택된 톱니, 돌아갈 방향
  t_select, dir = map(int, input().split())
  t_select = t_select - 1

  # 톱니가 왼쪽끝 오른쪽 끝인거에 따라사 나뉨
  
  # 톱니가 왼쪽 끝
  if (t_select == 0):
    if (li[t_select][2] == li[t_select + 1][6]):
      
  # 톱니가 오른쪽 끝
  if (t_select == t-1):  

  rotate_t(t_select, dir, li)
  print("rotate 직후",li)
  # 0 1 [2] 3 4 5 [6] 7 확인해야함



# print("밀기끝", li)

su = 0
for i in range(t):
  if li[i][0] == '1':
    su += 1
print(su)


