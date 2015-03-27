#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Graph(object):
    def __init__(self, verteces):
        self.verteces = verteces
        self.edges = 0
        self.adjs = [[] for i in xrange(self.get_v_count())]
        self.edgesTo = [[None] * self.get_v_count()
                for i in xrange(self.get_v_count())]

    def __repr__(self):
        ret = ''
        for i, adj in enumerate(self.adjs):
            ret += str(self.verteces[i]) + ' ->'
            for a in adj:
                ret += ' ' + str(self.verteces[a])
            ret += '\n'

        return ret

    def get_v_count(self):
        return len(self.verteces)

    def add_edge(self, v, w):
        v_idx = self.verteces.index(v)
        w_idx = self.verteces.index(w)
        self.adjs[v_idx].append(w_idx)
        self.adjs[w_idx].append(v_idx)
        self.edges += 1
        return self

    def idx_to_value(self, lst):
        return map(lambda i: self.verteces[i], lst)

    def dfs(self, start=None):
        if start is None:
            s = 0
        else:
            s = self.verteces.index(start)
        stack = [s]
        visited = []
        while stack:
            v = stack.pop()
            visited.append(v)
            for adj in self.adjs[v]:
                if adj not in visited and adj not in stack:
                    stack.append(adj)
        return self.idx_to_value(visited)

    def bfs(self, start=None):
        if start is None:
            s = 0
        else:
            s = self.verteces.index(start)
        queue = deque([s])
        visited = []
        while queue:
            v = queue.popleft()
            visited.append(v)
            for adj in self.adjs[v]:
                if adj not in queue and adj not in visited:
                    queue.append(adj)
                    self.edgesTo[s][adj] = v
        return self.idx_to_value(visited)
        pass


    def path(self, v, w):
        v_idx = self.verteces.index(v)
        w_idx = self.verteces.index(w)
        if self.edgesTo[v_idx] == [None] * self.get_v_count():
            self.bfs(v)
        p = [w_idx] # 因为是回溯方式找路径, 所以第一个记录点是终点
        i = w_idx
        while i != v_idx:
            i = self.edgesTo[v_idx][i]
            p.append(i)
        p.reverse()
        return self.idx_to_value(p)

    def topSort(self, v):
        v_idx = self.verteces.index(v)
        result = []
        visited = []

        self.topSortHelper(v_idx, visited, result)

        result.reverse()
        return self.idx_to_value(result)

    def topSortHelper(self, v, visited, result):
        if v not in visited:
            visited.append(v)

        for adj in self.adjs[v]:
            if adj not in visited:
                self.topSortHelper(adj, visited, result)

        if v not in result:
            result.append(v)
        pass


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
