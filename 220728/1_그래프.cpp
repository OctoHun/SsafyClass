//#include <iostream>
//#include <string>
//#include <cstring>
//using namespace std;
//
//int main() {
//
//	//그래프  = 점과 선으로 이루어져있는 그림
//	//여러 객체(여기서는 사람)이 투표함
//	//가장 많은 표, 적은 표 받은 사람
//	//객체(사람)= node or vertex or 정점
//	//각각의 선은 간선 or edge
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