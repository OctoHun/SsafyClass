//#include <iostream>
//#include <vector>
//using namespace std;
//
//int main() {
//
//
//	//인접리스트
//	//벡터라는 기능은 헤더를 가져와야 함
//	vector<int> v[100];  // vector<벡터 안에 어떤 데이터 형태를 저장할 것인가>  정수를 넣을 거라서 int.
//	//데이터를 vector에 저장할 것. 현재 0번~99번의 배열 from이 만들어진것.
//	int n;
//	int edge;
//	cin >> n >> edge;
//	for (int i = 0; i < edge; i++)
//	{
//		int from, to;
//		cin >> from >> to;
//		//from번째의 벡터에 메모리 추가하고 값 넣기
//		v[from].push_back(to); //vector.push_back : vector의 맨 뒤에 공간을 추가하여 데이터를 저장. 입력받은 to를 넣을 것임.
//		v[to].push_back(from); //무방향
//	}
//
//	
//
//}
//
