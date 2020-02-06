def canFinish(n, edge):
        indgree = [0]*n
        zero_indgree = []
        conn = {i:[] for i in range(n)}
        
        # 构建邻接表 & 统计各点入度
        for item in edge:
            conn[item[1]].append(item[0])
            indgree[item[0]] += 1
        
        # 统计零入度节点
        for i in range(n):
            if indgree[i] == 0:
                zero_indgree.append(i)
        
        # 依次 遍历零入度节点 & 删去连接的路径（该节点出度节点的入度值-1） & 判断出度节点是否变成了零入度节点，并维护到数组中
        i = 0
        while i < len(zero_indgree):
            for node in conn[zero_indgree[i]]:
                indgree[node] -= 1
                if indgree[node] == 0:
                    zero_indgree.append(node)
            i += 1
            
        # 遍历完成后，若零入度节点数等于总节点数，则可以
        if len(zero_indgree) == n:
            return True
        else:
            return False