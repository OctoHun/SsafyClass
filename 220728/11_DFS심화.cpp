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
//		if (arr[now][next] == 0) continue; // now���� next ������ ����
//		dfs(next);
//	}
//
//
//}
//
//int main() {
//
//
//	//tree�� �� ��
//	//node 7�� edge 5��
//	/*
//	7 5
//	1 2
//	2 4
//	2 5
//	3 6
//	6 7
//	1 3 <- A���� B�� �� �� �ִ°�?
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
//	//1���� �� �� �ִµ��� �� ������ 3�� �� �� �ִ��� Ȯ��
//
//	int a;
//	cin >> a >> b;
//	dfs(a);
//	cout << ans;
//
//
//	//�鸮�� ���� ����ϰ� �ʹٸ�
//	//used[100] ���� ���� dfs�� ���� ������ ���
//	//used[next]=1;
//	//cout<<used[b] �ϸ� �� �� ����
//
//
//	//���� ���� � ��η� �̵����ΰ�
//	//vector<int> path //���� ��θ� ���
//	//path.pushback(next); next�� �� ���̴� ��ο� �߰��ض�
//	//vector.pop_back(); ���� �ڿ� �ִ� ������ ����, ������ ����.
//
//
//	
//}