//#include <iostream>
//using namespace std;
//
//int arr[4][5] = { {4,5,1,-3,2},{1,-1,3,-1,5},{4,2,-5,6,-9},{-1,-1,-2,5,7} };
//int mini = 21e8; //21¾ï
//int used[10];
//
//void run(int lev, int gop) {
//	if (lev == 4)
//	{
//		if (gop < mini)
//		{
//			mini = gop;
//		}
//		cout << gop<<"\n";
//		return;
//	}
//	for (int i = 0; i < 5; i++)
//	{
//		if (used[i] == 1) continue;
//		used[i] = 1;
//		/*path[i] = arr[x][i];*/
//		run(lev + 1, gop * arr[lev][i]);
//		/*path[i] = 0;*/
//		used[i] = 0;
//
//
//	}
//}
//
//int main() {
//
//	run(0, 1);
//
//}