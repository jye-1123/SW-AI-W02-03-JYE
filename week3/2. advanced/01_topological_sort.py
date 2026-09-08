"""
[위상 정렬 - Topological Sort]
- 값의 크기순 정렬이 아니라 의존관계를 만족하는 순서 정렬
- 정렬 순서
    - 선행 조건이 없는 것부터 처리
    - 처리한 작업은 그래프에서 제거
    - 새롭게 선행 조건이 살진 작업을 또 처리
- Indegree: 어떤 노드로 들어가는 간선의 개수

- 장점:
    - 선행 관계가 있는 작업들의 실행 순서를 만들 수 있다.
    - 사이클이 있는지 감지 가능
    - 전체 작업 순서를 효율적으로 계산
    
- 한계:
    - 방향 그래프만 의미 있다
    - 사이클이 있으면 정렬 불가능
    - 정답이 하나가 아닐 수 있다 (A->C/B->C => A,B,C/B,A,C) => A와 B는 직접적인 선후 관계가 없기 때문

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    graph = {i: [] for i in range(vertices)}
    indegree = [0] * vertices
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for u,v in edges:
        graph[u].append(v)
        indegree[v] += 1
        
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    queue = deque()
    
    for i in range(vertices):
        if indegree[i] == 0:
            queue.append(i)
        
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(result) != vertices:
        return []
            
    return result


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
