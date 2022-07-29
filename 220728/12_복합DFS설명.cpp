//#include <iostream>
//#include <vector>
//using namespace std;
//
//int arr[100][100];
//int cntNode, cntEdge;
//int b;
//int ans = 0;
//
////used와 path 알맞게 갱신
////1 >2 >5
////1 2 3 4 5 6 7
////1 1     1
////이렇게 갱신
//
//vector<int> path;
//int used[10] = { 0 };
////index : node번호, value:해당 점을 들렸는가?
//
//
//void dfs(int now) {
//
//
//	//끝나는 것에 대한 처리(기저조건)
//	//끝나면서 무언가 처리할 것
//
//
//	for (int next = 1; next <= cntNode; next++)
//	{
//		//애초에 갈 수 없다면(가지치기가 가능하다면)
//		if (arr[now][next] == 0) continue;
//
//
//		//--------------------------------------//
//		//now->next 갈때 무언가 처리, 기록
//		used[next] = 1; //next라는 점을 들린다
//		path.push_back(next);
//
//
//		//어떤 계산을 한후 다시 가지치기를 해야 한다면 이 부분에 추가
//
//
//		//--------------------------------------//
//		dfs(next);  //next로 가라
//		//--------------------------------------//
//		
//
//		//next갔다온 후
//		//갔다가 돌아왔으니 기록을 지우거나 복구해라(초기화)
//		path.pop_back();
//		used[next]=0
//	}
//
//
//}
//
//int main() {
//
//	cin >> cntNode >> cntEdge;
//	for (int i = 0; i < cntEdge; i++)
//	{
//		int from, to;
//		cin >> from >> to;
//		arr[from][to] = 1;
//	}
//
//	int a;
//	cin >> a >> b;
//	dfs(a);
//	cout << ans;
//
//}