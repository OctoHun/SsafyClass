//#include <iostream>
//using namespace std;
//
//char path[4];
//void run(int x) {
//	//가지치기= 수행 자체를 못하도록
//
//	//두 번째, 일단 들어가고 잘못들어왔으면 바로 리턴
//	/*if (x == 1 && path[0] == '3') return;
//	if (x == 1 && path[0] == '4') return;*/
//
//	if (x == 3)
//	{
//		cout << path << endl;
//		return;
//	}
//	for (int i = 0; i < 4; i++)
//	{
//		//첫 번째, 이 안에 if문을 써서 하는 방법
//		/*if (x == 0 && i == 2) continue;
//		if (x == 0 && i == 3) continue;*/
//		path[x] = '1' + i;
//		run(x + 1);
//		path[x] = '0';
//	}
//}
//
//int main() {
//	run(0);
//}