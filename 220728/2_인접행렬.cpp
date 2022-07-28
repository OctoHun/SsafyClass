//#include <iostream>
//#include <string>
//#include <cstring>
//using namespace std;
//
//
//int main() {
//	//인접행렬로 어마무시하게 많은 node와 edge 저장하면 메모리 초과
//	//선에 대한 정보이므로 실질적으로 중요한 int의 개수는 edge의 개수
//	//낭비되는 int의 개수는 node의 개수*node의 개수-edge의 개수 (많은 낭비)
//	//1 대신 to 의 숫자를 넣어주면 됨. 압축해서 저장할 수 있음. edge개수만큼
//	//인접행렬방식 압축방식 장단점 있음. 특정해서 접근할대 인접행렬이 더 좋음.
//	//압축방식의 이름 = 인접 리스트
//	//인접리스트 방식에서 데이터 추가되면 메모리도 더 추가해줘야함 -> vector
//
//	//입력정보 4 <- node 개수     6<- edge 개수
//	//from과 to에 대한 정보가 edge 개수만큼 주어짐. 1 2, 2 3, 2 4, 3 4, 4 2, 4 3
//
//	int n;
//	cin >> n;
//	int edge;
//	cin >> edge;
//	int x, y;
//	int arr[100][100] = { 0 };
//	for (int i = 0; i < edge; i++)
//	{
//		cin >> y >> x;
//		arr[y - 1][x - 1] = 1;
//	}
//	for (int i = 0; i < 4; i++)
//	{
//		for (int j = 0; j < 4; j++) cout << arr[i][j] << " ";
//		cout << "\n";
//	}
//
//
//}