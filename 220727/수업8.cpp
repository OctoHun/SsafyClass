//#include <iostream>
//using namespace std;
//
//int N;
//int path[10];
//int used[10];
//void run(int x) {
//
//	if (x == N)
//	{
//		for (int i = 0; i < N; i++) cout << path[i] << " ";
//		cout << "\n";
//		return;
//	}
//	for (int i = 0; i < 6; i++)
//	{
//		path[x] = i + 1;
//		run(x + 1);
//		path[x] = 0;
//	}
//
//
//}
//void run1(int x, int start) {
//
//	if (x == N)
//	{
//		for (int i = 0; i < N; i++) cout << path[i] << " ";
//		cout << "\n";
//		return;
//	}
//	for (int i = start; i <= 6; i++)
//	{
//		path[x] = i;
//		run1(x + 1, i);
//		path[x] = 0;
//	}
//
//
//
//
//}
//
//void run2(int x) {
//	if (x == N)
//	{
//		for (int i = 0; i < N; i++) cout << path[i] << " ";
//		cout << "\n";
//		return;
//	}
//	for (int i = 0; i < 6; i++)
//	{
//		if (used[i] == 1) continue;
//		used[i] = 1;
//		path[x] = i + 1;
//		run2(x + 1);
//		path[x] = 0;
//		used[i] = 0;
//	}
//
//
//}
//
//
//
//int main() {
//
//	int M;
//	cin >> N >> M;
//	if (M == 1)	run(0);
//	else if (M == 2) run1(0, 1);
//	else if (M == 3) run2(0);
//
//
//}