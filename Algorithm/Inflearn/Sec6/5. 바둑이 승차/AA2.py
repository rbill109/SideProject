import sys

def DFS(v, tot, p_tot):
    global res
    print(f"v:{v} tot: {tot} p_tot: {p_tot} max: {res}")
    if tot > C:
        print("무게 초과")
        return

    # if p_tot < res:
    #     return
    
    if tot > res:
        res = tot
    if v==N:
        print("바둑이 이제 없음")
        return
    else:
        DFS(v+1, tot+a[v], p_tot+a[v])
        DFS(v+1, tot, p_tot+a[v])

if __name__=="__main__":
    C, N = map(int, sys.stdin.readline().split())
    a = [int(sys.stdin.readline()) for _ in range(N)]
    res = 0
    DFS(0, 0, 0)
    print(res)