//#include <iostream>
//using namespace std;
//
//
//int n;
//int used[15];
//int cnt=0;
//void run(int lev) {
//
//	ios::sync_with_stdio(false);
//	cin.tie(0);
//	cout.tie(0);
//
//	//Ã¼½º N Castle
//	if (lev == n) {
//		cnt++;
//		return;
//	}
//
//
//	for (int i = 0; i < n; i++)
//	{
//		if (used[i] == 1)continue;
//		used[i] = 1;
//		run(lev + 1);
//		used[i] = 0;
//	}
//
//}
//
//int main() {
//	cin >> n;
//	run(0);
//	cout << cnt;
//}