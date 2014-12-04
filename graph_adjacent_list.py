#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Graph(object):
    def __init__(self, verteces):
        self.verteces = verteces
        self.edges = 0
        self.adjcent = [[] for dummy in xrange(self.get_v_count())]
        self.edgeTo = [[None for d in xrange(self.get_v_count())]
                for dummy in xrange(len(self.verteces))]

    def __repr__(self):
        ret = ''
        for i, lst in enumerate(self.adjcent):
            node = str(self.verteces[i]) + ' -> '
            for adj in lst:
                node += str(self.verteces[adj]) + ' '
            ret += node.strip() + '\n'
        return ret

    def get_v_count(self):
        return len(self.verteces)

    def add_edge(self, v, w):
        v_idx = self.verteces.index(v)
        w_idx = self.verteces.index(w)
        self.adjcent[v_idx].append(w_idx)
        self.adjcent[w_idx].append(v_idx)
        self.edges += 1
        return self

    def dfs(self, start=None):
        if start is None:
            start_idx = 0
        else:
            start_idx = self.verteces.index(start)
        stack = [start_idx]
        visited = []
        while stack:
            v = stack.pop()
            visited.append(v)
            for adj in self.adjcent[v]:
                if adj not in stack and adj not in visited:
                    stack.append(adj)
        return self.idx_to_value(visited)

    def bfs(self, start=None):
        if start is None:
            start_idx = 0
        else:
            start_idx = self.verteces.index(start)
        queue = deque([start_idx])
        visited = []
        while queue:
            v = queue.popleft()
            visited.append(v)
            for adj in self.adjcent[v]:
                if adj not in queue and adj not in visited:
                    queue.append(adj)
                    self.edgeTo[start_idx][adj] = v
        return self.idx_to_value(visited)

    def idx_to_value(self, lst):
        ret = []
        for v in lst:
            ret.append(self.verteces[v])
        return ret

    def path(self, v, w):
        v_idx = self.verteces.index(v)
        w_idx = self.verteces.index(w)
        if self.edgeTo[v_idx] == [None] * self.get_v_count():
            self.bfs(v)
        i = w_idx # i 从终点开始回溯路径
        path = [i]
        while i != v_idx:
            i = self.edgeTo[v_idx][i]
            path.append(i)
        path.reverse()
        return self.idx_to_value(path)

    def topSort(self, v):
        result = []
        visited = []

        v_idx = self.verteces.index(v)

        self.topSortHelper(v_idx, visited, result)

        result.reverse()
        return self.idx_to_value(result)

    def topSortHelper(self, v, visited, result):
        visited.append(v)

        for adj in self.adjcent[v]:
            if adj not in visited:
                self.topSortHelper(adj, visited, result)

        if v not in result:
            result.append(v)


if __name__ == '__main__':
    stations = [
            '上地',
            '双井',
            '回龙观',
            '军博',
            '传媒大学',
            '牡丹园',
            '五道口',
            '雍和宫' ];
    subline = Graph(stations)

    subline.add_edge('上地','回龙观') \
    .add_edge('上地', '五道口') \
    .add_edge('五道口', '军博') \
    .add_edge('五道口', '牡丹园') \
    .add_edge('军博', '牡丹园') \
    .add_edge('军博', '传媒大学') \
    .add_edge('牡丹园', '雍和宫') \
    .add_edge('牡丹园', '双井') \
    .add_edge('雍和宫', '传媒大学') \
    .add_edge('雍和宫', '双井') \
    .add_edge('双井', '传媒大学') \
    .add_edge('传媒大学', '回龙观')

    print subline
    print 'dfs:'
    for v in subline.dfs('牡丹园'):
        print v,
    print
    print 'bfs:'
    for v in subline.bfs('上地'):
        print v,
    print
    print 'path: 双井 -> 上地:'
    for v in subline.path('双井', '上地'):
        print v, # 双井, 牡丹园, 五道口, 上地
    print

    print 'topSort from 回龙观:'
    for v in subline.topSort('回龙观'):
        print v,
    print
