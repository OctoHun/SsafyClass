//#include <iostream>
//#include <vector>
//using namespace std;
//
//int arr[100][100]={0};
//int node, edge;
//
////������ Ʈ���� �ƴ� ����
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
////��� ������� ��� ����Ǽ�(�ѹ� �������� ���� ����)
//vector<int> path; //���� ��θ� ���
//
//void dfs(int now) {
//
//	if (now == 5) //5�� �����̴�
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
//		//�پ��� ��θ� ���ؾ� �Ҷ� �ʱ�ȭ ����.
//		//�ܼ��� �� ���� ���, Ȥ�� ������⸸ �ϸ� �ȴٸ� �ʿ� ����
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
//	//�ѹ� �������� �ٽ� �������� �ѹ��� �� �����
//	used[1] = 1;
//	path.push_back(1);
//	dfs(1);
//
//}