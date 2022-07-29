//#include <iostream>
//#include <string>
//
//using namespace std;
//
//string arr;
//int c = 0;
//int gol, jum;
//void shape(int x, int y) {
//
//	if (x == 0 || y - 1 <= x) c++;
//	if (y == arr.size() - 1) c++;
//
//}
//
//void txt() {
//
//	for (int i = 0; i < arr.size(); i++)
//	{
//		if (i != gol && i != jum)
//		{
//			if (arr[i] >= 'A' && arr[i] <= 'Z') continue;
//			else if (arr[i] >= 'a' && arr[i] <= 'z') continue;
//			else if (arr[i] >= '0' && arr[i] <= '9') continue;
//			else c++;
//		}
//	}
//
//}
//
//int main() {
//
//	cin >> arr;
//	gol = arr.find('@', 0);
//	jum = arr.find('.', 0);
//
//	if (gol == -1) c++;
//	if (jum == -1) c++;
//	shape(gol, jum);
//
//	txt();
//
//	if (c > 0) cout << "불가능";
//	else cout << "가능";
//
//
//}