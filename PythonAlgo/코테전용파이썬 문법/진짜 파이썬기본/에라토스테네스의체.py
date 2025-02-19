
# 
def eratos(n):
  """
  n 이하의 소수를 모두 반환
  """
  # 0과 1은 소수가 아니므로 False
  sieve = [1] * (n + 1)
  sieve[0] = sieve[1] = 0
  
  # 2부터 n**1/2 까지 반복
  for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
      for j in range(i * i, n + 1, i):
        sieve[j] = 0
  # print(sieve)
  return [i for i,is_prime in enumerate(sieve) if is_prime]  
eratos(99999999)