//#include <iostream>
//using namespace std;
//
//
//int arr[4][5] = { {5,6,7,8,9},{1,1,1,1,1},{2,2,2,2,2},{1,1,1,1,1} };
//
//int getJumsu(int a, int b) {
//	int x[5] = { 0,-1,+1,0,0 };
//	int y[5] = { 0,0,0,-1,+1 };
//	int rst=1;
//	for (int i = 0; i < 5; i++) {
//
//		int nx, ny;
//		nx = x[i] + b;
//		ny = y[i] + a;
//		if (nx < 0 || ny < 0 || nx >= 5 || ny >= 4)
//		{
//			rst = arr[nx][ny] * rst;
//		}
//	}
//	return rst;
//	
//	
//}
//
//int main() {
//	int maxi = 0;
//		for (int y = 0; y < 4; y++)
//		{
//			for (int x = 0; x < 5; x++)
//			{
//				int ret = getJumsu(y, x);
//				if (ret > maxi) maxi = ret;
//			}
//		}
//		cout << maxi;
//
//}