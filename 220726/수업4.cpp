//#include <iostream>
//using namespace std;
//
//int map[4][5]{ {1,5,4,9,9},{1,1,5,4,9},{1,1,1,1,1,},{1,5,4,9,1} };
//int a[4] = { 1,5,4,9 };
//int b[2][2] = { {1,5},{1,1} };
//int isSame1(int y, int x)
//{
//	//�迭 a ������
//	for (int i = 0; i < 4; i++)
//	{
//		if (map[y][x + i] != a[i]) return 0;
//	}
//	return 1;
//}
//
//int isSame2(int y, int x) {
//	//2���� �迭 ������
//	for (int i = 0; i < 2; i++)
//	{
//		for (int j = 0; j < 2; j++)
//		{
//			if (map[i + y][j + x] != b[i][j]) return 0;
//		}
//	}
//	return 1;
//}
//
//int main() {
//	// �迭 a ������
//	/*int cnt = 0;
//	for (int i = 0; i < 4; i++)
//	{
//		for (int j = 0; j < 2; j++)
//		{
//			if (isSame1(i, j)) cnt++;
//		}
//	}
//	cout << cnt;*/
//
//
//	//2���� �迭 ������
//	int cnt = 0;
//	for (int i = 0; i < 3; i++)
//	{
//		for (int j = 0; j < 4; j++)
//		{
//			if (isSame2(i, j)) cnt++;
//		}
//	}
//	cout << cnt;
//
//}