if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores =list(arr)
    rs = max([x for x in scores if x < max(scores)])
    print(rs)
