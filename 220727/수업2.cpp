//#include <iostream>
//using namespace std;
//
//int path[4];
//void run(int x) {
//	if (x == 3)
//	{
//		for (int i = 0; i < 3; i++)
//		{
//
//			cout << path[i] << " ";
//		}
//		cout << "\n";
//		return;
//	}
//	for (int i = 0; i < 4; i++)
//	{
//		if (x > 0 && path[x - 1] == 1 + i) continue;
//		path[x] = 1 + i;
//		run(x + 1);
//		path[x] = 0;
//
//	}
//
//}
//
//
//
//int main() {
//	run(0);
//}