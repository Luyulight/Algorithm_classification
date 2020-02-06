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


    ''' ---------bfs---------------
    采用队列的数据结构，取队列首元素，将该节点标记为已访问，将该节点的未被访问过且不在队列中的邻接结点加入队列中
    '''
    def breadth_first_search(self,root=None):
            queue = []
            order = []
            def bfs():
                while len(queue)>0:
                    node = queue.pop(0)
                    self.visited[node] = True
                    for n in self.node_neighbors[node]:
                        if (not n in self.visited) and (not n in queue):
                            queue.append(n)
                            order.append(n)
    
            if root:
                queue.append(root)
                order.append(root)
                bfs()

            # 散落的几个无法访问到的直接加入queue和order
            for node in self.nodes():
                if not node in self.visited:
                    queue.append(node)
                    order.append(node)
                    bfs()
    
            self.visited = {}
            print order