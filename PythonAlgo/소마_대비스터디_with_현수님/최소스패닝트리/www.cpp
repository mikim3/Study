#include <iostream>
#include <queue>
#include <vector>
using namespace std;
struct Edge {
  int to;
  int isDown;
};

// 스패닝 트리에 실제로 포함되는 간선을 기준으로 오르막길의 수 세어야함
// 우선순위 큐에 간선을 넣을 때가 아니라, 
// 노드를 큐에서 꺼내어 방문할 때 그 노드로 연결된 간선의 정보를 사용하여 count를 증가시켜야 합니다.
int primBest(vector<vector<Edge>>& graph, int N) {
  priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;
  vector<bool> visited(N, false);
  int count = 0;
  pq.push({0, 0});
  while (!pq.empty()) {
    int currCost = pq.top().first; // 간선의 오르막길 여부
    int currNode = pq.top().second;
    pq.pop();
    if (visited[currNode]) continue;
    visited[currNode] = true;
    if (currNode != 0 && currCost == 0) { // 시작 노드는 제외하고 계산
      count++; // 현재 노드로 오는 간선이 오르막길인 경우
    }
    for (Edge& edge : graph[currNode]) {
      if (!visited[edge.to]) {
        pq.push({edge.isDown, edge.to});
      }
    }
  }
  return count;
}

int primWorst(vector<vector<Edge>>& graph, int N) {
  priority_queue<pair<int, int>, vector<pair<int, int>>,
                 greater<pair<int, int>>>
      pq;
  vector<bool> visited(N, false);
  int count = 0;
  pq.push({0, 0});
  while (!pq.empty()) {
    int curr = pq.top().second;
    pq.pop();
    if (visited[curr]) continue;
    visited[curr] = true;
    for (Edge& edge : graph[curr]) {
      if (!visited[edge.to]) {
        pq.push({edge.isDown, edge.to});
        if (edge.isDown == 0) count++;
      }
    }
  }
  return count;
}
int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<Edge>> graph(n + 1);
  int from, to, isDown;
  for (int i = 0; i < m; i++) {
    cin >> from >> to >> isDown;
    graph[from].push_back({to, isDown});
    graph[to].push_back({from, isDown});
  }
  int worst = primWorst(graph, n + 1);
  int best = primBest(graph, n + 1);
  cout << worst << ' ' << best << '\n';
  //   cout << worst * worst - best * best << '\n';
  return 0;
}