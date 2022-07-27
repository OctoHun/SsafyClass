//#include <iostream>
//using namespace std;
//
//
//int path[4];
//int n = 3;
//void run(int lev, int sum)
//{
//	if (lev == n) {
//		//첫 번째, 여기서 거르기
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
//		//두 번째, 들어가기 전에 거르기
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