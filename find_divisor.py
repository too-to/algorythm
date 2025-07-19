N, K =map(int, input().split())
a = [] # 약수 리스트

for i in range(1, N+1, 1):  
    if N % i == 0:  # N를 i로 나눴을 때 나머지가 0이면
        a.append(i) # i를 약수 리스트에 추가
    elif i == N: # i가 N이면
        a.append(i) # i를 약수 리스트에 추가

if len(a) >= K: # 리스트 a 요소가 숫자 K가 개수와 크거나 같을 때
    print(a[K-1]) # 리스트 a의 K번째 요소를 출력
else: # 만약 약수의 개수가 K보다 작다면 0을 출력
    print(0)
