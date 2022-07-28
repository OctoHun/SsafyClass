//#include <iostream>
//#include <vector>
//using namespace std;
//
//int arr[100][100];
//int cntNode, cntEdge;
//int b;
//int ans=0;
//void dfs(int now) {
//	cout << now << " ";
//	if (now == b) {
//		ans = 1;
//	}
//
//	for (int next = 1; next <= cntNode; next++)
//	{
//		if (arr[now][next] == 0) continue; // now에서 next 못가면 무시
//		dfs(next);
//	}
//
//
//}
//
//int main() {
//
//
//	//tree가 두 개
//	//node 7개 edge 5개
//	/*
//	7 5
//	1 2
//	2 4
//	2 5
//	3 6
//	6 7
//	1 3 <- A에서 B로 갈 수 있는가?
//	*/
//
//
//
//	cin >> cntNode >> cntEdge;
//	for (int i = 0; i < cntEdge; i++)
//	{
//		int from, to;
//		cin >> from >> to;
//		arr[from][to]=1;
//	}
//	//1부터 갈 수 있는데로 다 가보고 3에 갈 수 있는지 확인
//
//	int a;
//	cin >> a >> b;
//	dfs(a);
//	cout << ans;
//
//
//	//들리는 점을 기록하고 싶다면
//	//used[100] 만들어서 다음 dfs로 들어가기 직전에 기록
//	//used[next]=1;
//	//cout<<used[b] 하면 알 수 있음
//
//
//	//지금 내가 어떤 경로로 이동중인가
//	//vector<int> path //현재 경로를 기록
//	//path.pushback(next); next로 갈 것이니 경로에 추가해라
//	//vector.pop_back(); 가장 뒤에 있는 데이터 삭제, 공간도 지움.
//
//
//	
//}