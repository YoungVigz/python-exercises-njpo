class Node:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

class KDTree:
    def __init__(self, points):
        self.root = self._build_tree(points)
    
    def _build_tree(self, points, depth=0):
        if not points:
            return None

        axis = depth % len(points[0])
        points.sort(key=lambda point: point[axis])
        median = len(points) // 2

        node = Node(
            point=points[median],
            axis=axis
        )
        node.left = self._build_tree(points[:median], depth + 1)
        node.right = self._build_tree(points[median + 1:], depth + 1)

        return node

    def _nearest_neighbor(self, node, target, best_point=None, best_dist=float('inf')):
        if node is None:
            return best_point

        current_dist = self._distance(target, node.point)
        if current_dist < best_dist:
            best_point, best_dist = node.point, current_dist

        axis = node.axis
        next_branch = node.left if target[axis] < node.point[axis] else node.right
        opposite_branch = node.right if target[axis] < node.point[axis] else node.left

        best_point = self._nearest_neighbor(next_branch, target, best_point, best_dist)
        best_dist = self._distance(target, best_point)

        if abs(target[axis] - node.point[axis]) < best_dist:
            best_point = self._nearest_neighbor(opposite_branch, target, best_point, best_dist)

        return best_point

    def nearest_neighbor(self, target):
        return self._nearest_neighbor(self.root, target)

    @staticmethod
    def _distance(point1, point2):
        return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5


