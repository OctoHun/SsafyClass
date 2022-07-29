#include <iostream>
#include <vector>
using namespace std;

int main() {


	vector<vector<int>> v(6);
	//얼제이전씨 리스트 = 인접리스트
	//v(4) 4칸이 전부 0으로 채워짐
	//v(4, 1) 4칸이 전부 1로 채워짐
	//배열과는 다르게 선언 후 초기화해도 됨

	v[1] = { 3,4,5 };
	v[3] = { 4 };
	v[4] = {2,5 };
	v[5] = { 2 };

	int a;
	cin >> a;
		for (int i = 0; i < v[a].size(); i++)
		{
			cout << v[a][i] << " ";
		}

}