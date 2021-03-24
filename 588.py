# 588. Design In-Memory File System
# Design


# http://bookshadow.com/weblog/2017/05/21/leetcode-design-in-memory-file-system/
# runtime: faster than 72.58%
class FileSystem:

    def __init__(self):
        self.root = {'dirs': {}, 'files': {}}

    def ls(self, path: str) -> List[str]:
        node, type = self.getExistedNode(path)
        if type == 'dir': 
            l = []
            for k in node['dirs'].keys():
                l.append(k)
            for k in node['files'].keys():
                l.append(k)
            return sorted(l)
        return [path.split('/')[-1]]        

    def mkdir(self, path: str) -> None:
        node = self.root
        # dirs = path.split('/')
        for dir in filter(len, path.split('/')):
            if dir not in node['dirs']:
                node['dirs'][dir] = {'dirs': {}, 'files': {}}
            node = node['dirs'][dir]


    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        self.mkdir(path)
        node, type = self.getExistedNode(path)
        if file not in node['files']:
            node['files'][file] = ''
        node['files'][file] += content

        
    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        node, type = self.getExistedNode(path)
        return node['files'][file]


    def getExistedNode(self, path):
        node = self.root
        for dir in filter(len, path.split('/')):
            if dir in node['dirs']: node = node['dirs'][dir]
            else: return node, 'file'
        return node, 'dir'

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)