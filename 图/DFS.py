
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {} # key的节点可以访问到哪些节点
        self.visited = {} # key的节点是否被访问过
 
    def add_nodes(self, nodelist):
 
        for node in nodelist:
            self.add_node(node)
 
    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []
 
    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
 
            if (u != v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()


    ''' ---------dfs---------------
    1、递归DFS：访问节点，将该节点标记为已访问，同时对根节点的邻接结点中未访问过的结点递归调用DFS
    2、非递归DFS：取栈顶元素（不出栈），找到栈顶元素的一个未被访问过的邻接结点（注意是一个就行，不需要所有邻接结点入栈，与BFS不同），访问、标记为已访问并入栈，直到栈顶元素的所有邻接结点都被访问过，栈顶元素出栈，直到栈空
    '''
        #递归DFS
        def depth_first_search(self,root=None):
            order=[]
            def dfs(node):
                self.visited[node] = True
                order.append(node)
                for n in self.node_neighbors[node]:
                    if not n in self.visited:
                        dfs(n)
    
            if root:
                dfs(root)
    
            #对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
            for node in self.nodes():
                if not node in self.visited:
                    dfs(node)
            self.visited = {}
            print order
            return order
    
        #非递归DFS
        def depth_first_search2(self,root=None):
            stack = []
            order = []
            #self.visited[root] = True
            def dfs():
                while stack:
                    node = stack[-1]
                    for n in self.node_neighbors[node]:
                        if not n in self.visited:
                            order.append(n)
                            stack.append(n)
                            self.visited[n] = True
                            break # 重要
                    # 这个else的意思应该是node_neighbors[node]的所有节点都在visited里被标记，那说明这个节点已经遍历结束，可以弹出
                    else:
                        stack.pop()
            if root:
                stack.append(root)
                order.append(root)
                self.visited[root]=True
                dfs()
    
            for node in self.nodes():
                if node not in self.visited:
                    stack.append(node)
                    order.append(node)
                    self.visited[node]=True
                    dfs()
    
            self.visited = {}
            print order
            return order