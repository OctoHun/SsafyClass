//#include <iostream>
//#include <string>
//using namespace std;
//
//
//
//int cnt = 0;
//
//void findGold(string a) {
//	int index = 0;
//	while (1) {
//		int ret = a.find("GOLD", index);
//		if (ret == -1) return;
//		cnt++;
//		index = ret + 1;
//	}
//}
//int main() {
//	string strs[4] = {
//		"GOLD#GOLD##",
//		"#GOL#GOLE#GOLED",
//		"GOLD",
//		"GGGGOLD#GOLD"
//	};
//
//
//	for (int i = 0; i < 4; i++)
//	{
//		findGold(strs[i]);
//	}
//	cout << cnt;
//
//
//}