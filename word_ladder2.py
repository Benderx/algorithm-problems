class Solution(object):
    class node():
        def __init__(self, v, d):
            self.val = v
            self.dist = d
            self.connected = []
            self.parents = []


    def word_dist(self, word1, word2, num):
        dist = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dist += 1
                if num == 0 and dist == 2:
                    break
        return dist


    def get_all_word_dists(self, wordList, word):
        d = {}
        for i in wordList:
            if i == wordList:
                continue
            d[i] = self.word_dist(i, word, 1)
        return d    


    def make_nodes(self, word_list, dists):
        a = dict()
        for i in word_list:
            a[i] = self.node(i, dists[i])
        return a


    def form_graph(self, beginWord, node_dict):
        root = node_dict[beginWord]
        curr = None
        queue = [root]
        visited = {beginWord: True}

        while len(queue) != 0:
            curr = queue.pop(0)
            visited[curr.val] = True
            for word in wordList:
                dist = self.word_dist(word, curr.val, 0)
                if dist < 2:
                    if word not in visited:
                        queue.append(node_dict[word])
                    curr.connected.append(node_dict[word])
                    node_dict[word].parents.append(curr)
        return root


    def get_info(self, root, endWord, end_dists):
        queue = [root]
        curr = None
        info = dict()
        done = -1
        visited = dict()
        for key in end_dists:
            info[key] = [None, end_dists[key]]
        info[root.val][0] = 0

        while len(queue) != 0:
            queue.sort(key=lambda x: info[x.val][0] + info[x.val][0])
            curr = queue.pop(0)
            visited[curr.val] = True
            if info[curr.val][0] == done:
                continue
            if curr.val == endWord:
                done = info[curr.val][0]

            for i in curr.connected:
                if i.val not in visited:
                    info[i.val][0] = info[curr.val][0] + 1
                    queue.append(i)
        if done == -1:
            return False

        return info


    def get_shortest(self, info, end_node):
        paths = []

        return paths


    def dfs_shortest(self, info, node):
        for i in node.parents:
            if info[i.val][0] == info[node.val][0] - 1:
                a = dfs_shortest(info, i)
                if len(a) > 0:
                    return a


    def findLadders(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        dists = self.get_all_word_dists(wordList, endWord)
        node_dict = self.make_nodes(wordList, dists)
        root = self.form_graph(beginWord, node_dict)
        info = self.get_info(root, endWord, dists)
        if not info:
            return []

        end_node = node_dict[endWord]
        shortest = self.get_shortest(info, end_node)
        return shortest

s = Solution()

wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"

print(s.findLadders(beginWord, endWord, wordList),   [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ])