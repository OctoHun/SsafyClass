//#include <iostream>
//#include <vector>
//using namespace std;
//
//int arr[100][100];
//int cntNode, cntEdge;
//int b;
//int ans = 0;
//
////used�� path �˸°� ����
////1 >2 >5
////1 2 3 4 5 6 7
////1 1     1
////�̷��� ����
//
//vector<int> path;
//int used[10] = { 0 };
////index : node��ȣ, value:�ش� ���� ��ȴ°�?
//
//
//void dfs(int now) {
//
//
//	//������ �Ϳ� ���� ó��(��������)
//	//�����鼭 ���� ó���� ��
//
//
//	for (int next = 1; next <= cntNode; next++)
//	{
//		//���ʿ� �� �� ���ٸ�(����ġ�Ⱑ �����ϴٸ�)
//		if (arr[now][next] == 0) continue;
//
//
//		//--------------------------------------//
//		//now->next ���� ���� ó��, ���
//		used[next] = 1; //next��� ���� �鸰��
//		path.push_back(next);
//
//
//		//� ����� ���� �ٽ� ����ġ�⸦ �ؾ� �Ѵٸ� �� �κп� �߰�
//
//
//		//--------------------------------------//
//		dfs(next);  //next�� ����
//		//--------------------------------------//
//		
//
//		//next���ٿ� ��
//		//���ٰ� ���ƿ����� ����� ����ų� �����ض�(�ʱ�ȭ)
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