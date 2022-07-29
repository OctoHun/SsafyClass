//#include <iostream>
//#include <vector>
//using namespace std;
////그래프 데이터를 전역변수로 <- 모든 함수에서 공통적으로 볼 수 있도록
//int arr[6][6] = { 0 };
//int cntnode;
//void dfs(int now) { //지금 now라는 노드에 있다.
//
//	cout << now << " ";
//	//now에서 갈 수 있는 next라는 node로 가라!
//	//next는 어떤 data를 확인해야할까? -> arr[6][6]
//	//arr[now][??] == 1 이면 갈 수 있음
//
//	// 기저조건이 필수가 아님. 없어도 재귀 끝남
//
//	for (int next = 1; next <= cntnode; next++)
//	{
//		if (arr[now][next] == 0) continue;
//		dfs(next);
//	}
//
//
//}
//
//int main() {
//	// 임의의 노드를 한번씩만 들려서 연결 - 1가지밖에 나오지 않는 경우 > 트리
//	// 트리형의 경우 node의 개수가 N개일때 edge의 개수는 N-1개
//	// 트리형의 루트-뿌리지점(정해질때도 있고 안정해질때도 있음)
//	// 어떤 노드에서 위로 가면 parent(부모) 아래로는 child(자식)
//	// 부모보다 위면 조상
//	// 큰 트리 안에서 main루트가 아니라도 어떤 일부에서 임시 root를 보았을때
//	// 트리구조. 일부만 보아도 항상 트리구조.
//	 
//	// 인접 행렬 저장
//
//
//	cin >> cntnode;
//	for (int i = 0; i < cntnode - 1; i++)
//	{
//		int parent, child; //parent에서 child로 갈 수 있다는 정보
//		cin >> parent >> child;
//		arr[parent][child] = 1;
//	}
//
//	// DFS : Depth First Search(깊이 우선 탐색) <- 재귀
//	//		- 완전탐색 <- 모든것을 다 확인한다.
//	// 1. 트리에서 모든 노드를 다 확인한다.
//
//	dfs(1);
//
//}