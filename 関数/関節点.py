def low_link(nodes):
    N = len(nodes)
    visited = [False] * N
    prenum = [0] * N
    parent = [0] * N
    lowest = [0] * N
    bridges = []
    timer = 1

    def rec(cur, prev, timer):
        # curを訪問した直後の処理
        prenum[cur] = lowest[cur] = timer
        timer += 1
        visited[cur] = True
        for nxt in nodes[cur]:
            if not visited[nxt]:
                # curからvへ訪問する直前の処理
                parent[nxt] = cur
                timer = rec(nxt, cur, timer)
                # nxtの探索が終了した直後の処理
                lowest[cur] = min(lowest[cur], lowest[nxt])
                # より近い経路を含まないなら橋とする
                if lowest[nxt] == prenum[nxt]:
                    # 番号の小さい方から入れる
                    bridges.append((min(cur, nxt), max(cur, nxt)))
            elif nxt != prev:
                # cur -> nxt がback-edgeの場合の処理
                lowest[cur] = min(lowest[cur], prenum[nxt])
        return timer
    # 必要な各値の取得(非連結に対応するため全頂点から)
    for i in range(N):
        if not visited[i]:
            timer = rec(i, -1, timer)

    # 間接点
    aps = set()
    # ルートの子ノードの数
    np = 0
    for i in range(1, N):
        p = parent[i]
        if p == 0:
            np += 1
        # 条件2の確認
        elif prenum[p] <= lowest[i]:
            aps.add(p)
    # 条件1の確認
    if np > 1:
        aps.add(0)

    return aps, bridges
