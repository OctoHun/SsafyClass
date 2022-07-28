//#include <iostream>
//#include <vector>
//using namespace std;
//
//int arr[100][100]={0};
//int node, edge;
//
////무방향 트리가 아닌 구조
//
///*
//5
//6
//1 2
//1 3
//1 4
//2 5
//3 4
//4 5
//*/
//
//int used[10] = { 0 };
//
////경로 기록으로 경로 경우의수(한번 갔던곳은 가지 않음)
//vector<int> path; //현재 경로를 기록
//
//void dfs(int now) {
//
//	if (now == 5) //5가 끝점이다
//	{
//		for (int i = 0; i < path.size(); i++)
//			cout << path[i] << " ";
//		cout << "\n";
//		return;
//	}
//	for (int next = 1; next <= node; next++)
//	{
//		if (arr[now][next] == 0)continue;
//		if (used[next] == 1) continue;
//
//		used[next] = 1;
//		path.push_back(next);
//
//		dfs(next);
//
//
//		//다양한 경로를 구해야 할때 초기화 해줌.
//		//단순히 한 개의 경로, 혹은 들려보기만 하면 된다면 필요 없음
//		path.pop_back();
//		used[next] = 0;
//
//	}
//
//
//
//}
//
//
//int main() {
//
//
//	cin >> node >> edge;
//	for (int i = 0; i < edge; i++)
//	{
//		int start, end;
//		cin >> start >> end;
//		arr[start][end] = 1;
//		arr[end][start] = 1;
//	}
//	//한번 갔던곳은 다시 가지말고 한번씩 다 들려라
//	used[1] = 1;
//	path.push_back(1);
//	dfs(1);
//
//}