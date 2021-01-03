# 1146. Snapshot Array

# Design

# https://coordinate.wang/index.php/archives/2570/

# Array
# running time: faster than 42.64%
class SnapshotArray1:

    def __init__(self, length: int):
        self.snapID = 0
        self.data = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index].append([self.snapID, val])

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1
        
    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.data[index], [snap_id, float('inf')]) - 1
        return self.data[index][i][1]


# Hash
# running time: faster than 96.85%
class SnapshotArray2:

    def __init__(self, length: int):
        self.d = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.d[index] = val

    def snap(self) -> int:
        self.snaps.append(self.d.copy())
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index] if index in self.snaps[snap_id] else 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)    


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)