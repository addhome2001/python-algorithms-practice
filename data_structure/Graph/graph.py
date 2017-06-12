# -*- coding: utf-8 -*-
"""圖形"""

if __name__ == '__main__':
    import os
    import sys
    DIR_PATH = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(DIR_PATH, '..')))
    from dictionary import Dictionary
    from queue_c import Queue
    from stack import Stack
else:
    from .dictionary import Dictionary
    from .queue_c import Queue
    from .stack import Stack

class Graph(object):
    """
    圖形類別
    """

    def __init__(self):
        """初始化頂點、頂點關係字典"""
        self.vertices = []
        self.relaction = Dictionary()

    def add_vertex(self, vertex):
        """增加頂點，並在關係字典中添加新陣列"""
        self.vertices.append(vertex)
        self.relaction.set(vertex, [])

    def add_edge(self, source, target):
        """增加邊，將目標和來源頂點添加進關係陣列中"""
        self.relaction.get(source).append(target)
        self.relaction.get(target).append(source)

    def initialize_color(self):
        """
        初始化頂點顏色
        白色：未探索
        灰色：已發現
        黑色：探索完畢
        """
        color = {}
        for vertex in self.vertices:
            color[vertex] = 'white'
        return color

    def bfs(self, operator, begin_at=0):
        """
        廣度優先探索
        探索最先入列的頂點，以Queue（先進先出）對頂點做操作
        近入隊的頂點會先被探索
        """
        color = self.initialize_color()
        apex = self.vertices[begin_at]
        queue = Queue()
        queue.enqueue(apex)

        while not queue.isEmpty():
            wait_v = queue.dequeue()
            neighbors = self.relaction.get(wait_v)
            color[wait_v] = 'gray'

            for neighbor in neighbors:
                if color[neighbor] == 'white':
                    queue.enqueue(neighbor)
                    color[neighbor] = 'gray'

            color[wait_v] = 'black'

            if operator:
                operator(wait_v)

    def bfs_search_path(self, begin_at=0):
        """
        利用廣度優先搜尋
        得出由頂點到達各個頂點的邊數
        探索最先入列的頂點，以Queue（先進先出）對頂點做操作
        返回:
            previous_v每個頂點的上個頂點
            path_distance由頂點至該點的距離
        """
        color = self.initialize_color()
        apex = self.vertices[begin_at]
        queue = Queue()
        queue.enqueue(apex)
        prev_vertex = {}
        path_distance = {}

        for vertex in self.vertices:
            prev_vertex[vertex] = None
            path_distance[vertex] = 0

        while not queue.isEmpty():
            wait_v = queue.dequeue()
            neighbors = self.relaction.get(wait_v)
            color[wait_v] = 'gray'

            for neighbor in neighbors:
                if color[neighbor] == 'white':
                    queue.enqueue(neighbor)
                    color[neighbor] = 'gray'
                    prev_vertex[neighbor] = wait_v
                    path_distance[neighbor] += 1

            color[wait_v] = 'black'

        return {
            'prev_vertex': prev_vertex,
            'path_distance': path_distance
        }

    def from_vertex(self, operator, begin_at=0):
        """
        取得頂點到各頂點的最短路徑
        以廣度優先路徑搜尋取得的個頂點前一個頂點
        並根據每個頂點的前一個頂點分析出有效路徑
        """
        prev_vertex = self.bfs_search_path(begin_at).get('prev_vertex')
        begin_index = begin_at + 1
        new_vertices = self.vertices[begin_index:]

        for vertex in new_vertices:
            path = Stack()
            current_vertex = vertex
            result = ''

            while current_vertex:
                path.push(current_vertex)
                current_vertex = prev_vertex[current_vertex]

            while not path.isEmpty():
                result += '{} '.format(path.pop())

            operator(result)

    def dfs(self, operator):
        """
        深度優先探索
        由某個頂點開始遍歷
        當到最後一個頂點，便回朔至之前頂點的其他路徑
        直到遍歷完畢
        """
        color = self.initialize_color()

        def visit(vertex, color, operator):
            """
            以遞迴方式遍歷頂點
            只有在頂點的狀態為未探索(white)才進行遞迴
            """
            color[vertex] = 'gray'
            operator(vertex)
            neighbors = self.relaction.get(vertex)

            for neighbor in neighbors:
                if color[vertex] == 'white':
                    visit(neighbor, color, operator)

            color[vertex] = 'black'

        for vertex in self.vertices:
            if color[vertex] == 'white':
                visit(vertex, color, operator)

    def dfs_search_path(self):
        """
        利用深度優先探索
        得出每個頂點的發現時間以及探索完畢時間
        在理想情況下，最終頂點的探索完畢會落在頂點數的一至兩倍
        而每個頂點的探索完畢時間會大於發現時間
        """
        color = self.initialize_color()
        time = 0
        discovery = {}
        finish = {}

        def visit(vertex, color, discovery, finish):
            """
            以遞迴方式遍歷頂點
            只有在頂點的狀態為未探索(white)才進行遞迴
            """
            nonlocal time
            time += 1
            color[vertex] = 'gray'
            discovery[vertex] = time
            neighbors = self.relaction.get(vertex)

            for neighbor in neighbors:
                if color[neighbor] == 'white':
                    visit(neighbor, color, discovery, finish)

            color[vertex] = 'black'
            time += 1
            finish[vertex] = time

        for vertex in self.vertices:
            discovery[vertex] = 0
            finish[vertex] = 0

        for vertex in self.vertices:
            if color[vertex] == 'white':
                visit(vertex, color, discovery, finish)

        return {
            'discovery': discovery,
            'finish': finish
        }

    def discovery_and_finish(self, operator):
        """
        正規化頂點發現時間和完成時間
        以深度優先路徑搜尋取得的發現和完成時間字典
        """
        info = self.dfs_search_path()
        finish = info.get('finish')
        discovery = info.get('discovery')

        for vertex, discovery_time in discovery.items():
            if vertex in finish:
                finish_time = finish.get(vertex)
                operator('{} discovery: {}, finish: {}'.format(vertex, discovery_time, finish_time))

    def __str__(self):
        result = ''
        for vertex in self.vertices:
            result += '{}->{}\n'.format(vertex, ' '.join(self.relaction.get(vertex)))
        return result

if  __name__ == '__main__':
    graph = Graph()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        graph.add_vertex(v)
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'G')
    graph.add_edge('D', 'H')
    graph.add_edge('B', 'E')
    graph.add_edge('B', 'F')
    graph.add_edge('E', 'I')
    graph.bfs(lambda v: print('{} have been visited.'.format(v)))
    graph.from_vertex(print)
    graph.dfs(lambda v: print('{} have been visited.'.format(v)))
    graph.discovery_and_finish(print)
