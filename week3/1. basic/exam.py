# # 이진검색트리 값 삽입
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
        
# def insert_bst(root, value):
#     if root is None:
#         return TreeNode(value)
        
        
#     if root.value > value:
#         root.left = insert_bst(root.left, value)
#     elif root.value < value:
#         root.right = insert_bst(root.right, value)
        
#     return root


# # 이진검색트리 최솟값 찾기
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
# def find_min(root):
#     while root.left is not None:
#         root = root.left
    
#     return root


# # 이진검색트리 최댓값 찾기
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
# def find_max(root):
#     while root.right is not None:
#         root = root.right
        
#     return root


# # # 이진검색트리 삭제
# # class TreeNode:
# #     def __init__(self, value):
# #         self.value = value
# #         self.left = None
# #         self.right = None

# # def find_min(root):
# #     while root.left is not None:
# #         root = root.left

# #     return root

# def delete_bst(root, value):
#     if root is None:
#         return None

#     if value < root.value:
#         root.left = delete_bst(root.left, value)

#     elif value > root.value:
#         root.right = delete_bst(root.right, value)

#     else:
#         if root.left is None:
#             return root.right
#         if root.right is None:
#             return root.left
        
#         successor = find_min(root.right)
#         root.value = successor.value
#         root.right = delete_bst(root.right, successor.value)
        
#     return root

# # 그래프 생성
# def create_graph(vertices, edges, directed=False):
#     graph = {}
    
#     for i in range(vertices):
#         graph[i] = []
        
#     for u, v in edges:
#         graph[i].append(u)
#         if not directed:
#             graph[u].append(v)
    
#     return graph

# # 경로 존재 여부
# from collections import deque

# def has_path(graph, start, target):
#     seen = {start}
#     queue = deque([start])
    
#     while queue:
#         current = queue.popleft()
#         if current == target:
#             return True
        
#         for neighbor in graph[current]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)
    
#     return False



# """
# [위상 정렬 - Topological Sort]
# - 값의 크기순 정렬이 아니라 의존관계를 만족하는 순서 정렬
# - 정렬 순서
#     - 선행 조건이 없는 것부터 처리
#     - 처리한 작업은 그래프에서 제거
#     - 새롭게 선행 조건이 살진 작업을 또 처리
# - Indegree: 어떤 노드로 들어가는 간선의 개수

# - 장점:
#     - 선행 관계가 있는 작업들의 실행 순서를 만들 수 있다.
#     - 사이클이 있는지 감지 가능
#     - 전체 작업 순서를 효율적으로 계산
    
# - 한계:
#     - 방향 그래프만 의미 있다
#     - 사이클이 있으면 정렬 불가능
#     - 정답이 하나가 아닐 수 있다 (A->C/B->C => A,B,C/B,A,C) => A와 B는 직접적인 선후 관계가 없기 때문

# 문제 설명:
# - 방향 그래프에서 순서를 정합니다.
# - 선행 작업이 먼저 오도록 정렬합니다.
# - 예: 과목 선수과목, 작업 순서

# 입력:
# - graph: 방향 그래프
# - vertices: 정점 개수

# 출력:
# - 위상 정렬 순서

# 예제:
# 과목:
# 0(기초) → 1(중급) → 3(고급)
# 0(기초) → 2(응용)

# 위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

# 힌트:
# - 진입 차수(in-degree) 사용
# - 진입 차수가 0인 정점부터 시작
# - 큐 사용
# """

# from collections import deque

# def topological_sort(num_courses, edgprerequisiteses):
#     """
#     위상 정렬 (Kahn's Algorithm)
    
#     Args:
#         vertices: 정점 개수
#         edges: (출발, 도착) 간선 리스트
    
#     Returns:
#         위상 정렬 순서
#     """
#     # TODO: 그래프와 진입 차수 초기화
#     graph = {i: [] for i in range(num_courses)}
#     indegree = [0] * num_courses
    
#     # TODO: 그래프 구성 및 진입 차수 계산
#     for u,v in edgprerequisiteses:
#         graph[u].append(v)
#         indegree[v] += 1
        
    
#     # TODO: 진입 차수가 0인 정점들을 큐에 추가
#     queue = deque()
    
#     for i in range(num_courses):
#         if indegree[i] == 0:
#             queue.append(i)
        
#     result = []
    
#     # TODO: 큐가 빌 때까지 반복
#     ## 큐에서 정점 꺼내기
#     ## 인접한 정점들의 진입 차수 감소
#     while queue:
#         current = queue.popleft()
#         result.append(current)
        
#         for neighbor in graph[current]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 queue.append(neighbor)
                
            
#     return True if len(result) == num_courses else False


# # 테스트 케이스
# if __name__ == "__main__":
#     # 과목 선수과목 예제
#     vertices = 4
#     edges = [
#         (0, 1),  # 0 → 1
#         (0, 2),  # 0 → 2
#         (1, 3),  # 1 → 3
#     ]
    
#     print("=== 위상 정렬 ===")
#     print("과목 관계:")
#     print("  0(기초) → 1(중급) → 3(고급)")
#     print("  0(기초) → 2(응용)")
#     print()
    
#     result = topological_sort(vertices, edges)
#     print(f"수강 순서: {result}")

# def create_graph(vertices, edges, directed=False):
#     """
#     그래프 생성 (인접 리스트)
    
#     Args:
#         vertices: 정점 개수
#         edges: (출발, 도착) 간선 리스트
#         directed: 방향 그래프 여부
    
#     Returns:
#         그래프 딕셔너리
#     """
#     # TODO: 빈 그래프 초기화
#     graph = {}
    
#     for i in range(vertices):
#         graph[i] = []
    
#     # TODO: 간선 추가
#     ## 간선 추가 (u에서 v로)
#     ## 무방향 그래프면 반대 방향도 추가
#     for u, v in edges:
#         graph[u].append(v)
        
#         if not directed:
#             graph[v].append(u)
    
#     return graph

# # 테스트 케이스
# if __name__ == "__main__":
#     # 테스트 케이스 1: 무방향 그래프
#     vertices = 4
#     edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    
#     print("=== 무방향 그래프 ===")
#     graph = create_graph(vertices, edges, directed=False)
#     for vertex, neighbors in graph.items():
#         print(f"{vertex} → {neighbors}")
#     print()
    
#     # 테스트 케이스 2: 방향 그래프
#     print("=== 방향 그래프 ===")
#     graph_directed = create_graph(vertices, edges, directed=True)
#     for vertex, neighbors in graph_directed.items():
#         print(f"{vertex} → {neighbors}")
        



# # 백준 1260번 문제
# # 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# # 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# # N: 정점의 개수
# # M: 간선의 개수
# # V: 탐색을 시작할 정점의 번호


# from collections import deque

# def dfs(graph, start, visited = None):
#     if visited is None:
#         visited = []
    
#     visited.append(start)
    
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)
    
#     return visited

# def bfs(graph, start):
#     visited = []

#     seen = {start}
#     queue = deque([start])

#     while queue:
#         current = queue.popleft()
#         visited.append(current)
        
#         for neighbor in graph[current]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)
    
#     return visited
    

# if __name__ == "__main__":
#     N, M, V = map(int, input().split())
    
#     graph = [[] for _ in range(N+1)]
        
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
        
#     for i in range(1, N+1):
#         graph[i].sort()
        

#     print(*dfs(graph, V))
#     print(*bfs(graph, V))


# # 백준 2606번 문제
# from collections import deque

# def virus(graph, start):
#     visited = []
            
#     seen = {start}
#     queue = deque([start])
    
#     while queue:
#         current = queue.popleft()
#         visited.append(current)
                
#         for neighbor in graph[current]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)
                
#     infection_com = len(visited) - 1
    
#     return infection_com

# if __name__ == "__main__":
#     n = int(input())
#     p = int(input())
    
#     graph = [[] for _ in range(n+1)]
        
#     for _ in range(p):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
        
#     for i in range(1, n+1):
#         graph[i].sort()
    
#     print(virus(graph, 1))


# # 백준 24479
# from collections import deque

# def dfs(current):
#     global count

#     order[current] = count
#     count += 1

#     for neighbor in graph[current]:
#         if order[neighbor] == 0:
#             dfs(neighbor)


# # 백준 24479
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())

# graph = [[] for _ in range(N + 1)]
# order = [0] * (N + 1)
# count = 1
    
# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
        
# for i in range(1, N+1):
#     graph[i].sort()

# def dfs(current):
#     global count
    
#     order[current] = count
#     count += 1
    
#     for neighbor in graph[current]:
#         if order[neighbor] == 0:
#             dfs(neighbor)
            
# dfs(R)

# for i in range(1, N+1):
#     print(order[i])


# # # 백준 24480
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())

# graph = [[] for _ in range(N + 1)]
# order = [0] * (N + 1)
# count = 1
    
# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
        
# for i in range(1, N+1):
#     graph[i].sort(reverse=True)

# def dfs(current):
#     global count
    
#     order[current] = count
#     count += 1
    
#     for neighbor in graph[current]:
#         if order[neighbor] == 0:
#             dfs(neighbor)
            
# dfs(R)

# for i in range(1, N+1):
#     print(order[i])


# # 백준 24444
# import sys
# from collections import deque

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())

# graph = [[] for _ in range(N+1)]
# order = [0] * (N + 1)

# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)


# for j in range(1, N+1):
#     graph[j].sort()
    

# def bfs(current):
#     order[current] = 1
#     cnt = 2
#     queue = deque([current])
    
#     while queue:
#         current = queue.popleft()
        
#         for neighbor in graph[current]:
#             if order[neighbor] == 0:
#                 order[neighbor] = cnt
#                 cnt += 1
#                 queue.append(neighbor)

# bfs(R)

# for i in range(1, N+1):
#     print(order[i])
    

# # 백준 24445
# import sys
# from collections import deque

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())

# graph = [[] for _ in range(N+1)]
# order = [0] * (N + 1)

# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)


# for j in range(1, N+1):
#     graph[j].sort(reverse = True)
    

# def bfs(current):
#     order[current] = 1
#     cnt = 2
#     queue = deque([current])
    
#     while queue:
#         current = queue.popleft()
        
#         for neighbor in graph[current]:
#             if order[neighbor] == 0:
#                 order[neighbor] = cnt
#                 cnt += 1
#                 queue.append(neighbor)

# bfs(R)

# for i in range(1, N+1):
#     print(order[i])