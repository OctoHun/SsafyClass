//#include <iostream>
//using namespace std;
//
//
//int path[4];
//int n = 3;
//void run(int lev, int sum)
//{
//	if (lev == n) {
//		//ù ��°, ���⼭ �Ÿ���
//		/*if (sum > 10) return;*/
//		for (int i = 0; i < n; i++)
//		{
//			cout << path[i] << " ";
//		}
//		cout << sum << " ";
//		cout << "\n";
//
//		return;
//	}
//	for (int i = 0; i < 6; i++)
//	{
//		//�� ��°, ���� ���� �Ÿ���
//		if (sum + 1 + i >= 10) continue;
//		path[lev] = 1 + i;
//		run(lev + 1, sum+1+i);
//		path[lev] = 0;
//	}
//}
//
//int main() {
//	run(0, 0);
//
//
//}