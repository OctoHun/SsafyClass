//#include <iostream>
//#include <string>
//#include <cstring>
//using namespace std;
//
//int main() {
//
//	//�׷���  = ���� ������ �̷�����ִ� �׸�
//	//���� ��ü(���⼭�� ���)�� ��ǥ��
//	//���� ���� ǥ, ���� ǥ ���� ���
//	//��ü(���)= node or vertex or ����
//	//������ ���� ���� or edge
//	int arr[10][10];
//	int max = 0;
//	int maxindex = 0;
//	int min = 100;
//	int minindex = 0;
//	int n;
//	cin >> n;
//	for (int i = 0; i < n; i++)
//	{
//		for (int j = 0; j < n; j++)
//		{
//			cin >> arr[i][j];
//		}
//	}
//	for (int i = 0; i < n; i++)
//	{
//		int cnt = 0;
//		for (int j = 0; j < n; j++)
//		{
//			if (arr[j][i] == 1) cnt++;
//		}
//		if (cnt > max)
//		{
//			max = cnt;
//			maxindex = i;
//		}
//		if (cnt < min)
//		{
//			min = cnt;
//			minindex = i;
//		}
//	}
//	cout << maxindex + 1<<"\n";
//	cout << minindex + 1;
//
//
//}