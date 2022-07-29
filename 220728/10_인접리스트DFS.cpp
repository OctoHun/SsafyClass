//#include <iostream>
//#include <vector>
//using namespace std;
//
//vector<int> v[100];
//int cntnode;
//
//void dfs(int now) {
//	cout << now << " ";
//
//	for (int i = 0; i < v[now].size(); i++)
//	{
//		int next = v[now][i];
//		dfs(next);
//
//	}
//
//}
//
//int main() {
//
//	cin >> cntnode;
//	for (int i = 0; i < cntnode - 1; i++)
//	{
//		int parent, child;
//		cin >> parent >> child;
//		v[parent].push_back(child);
//	}
//	dfs(1);
//}