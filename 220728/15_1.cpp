#include <iostream>
#include <vector>
using namespace std;

int main() {


	vector<vector<int>> v(6);
	//���������� ����Ʈ = ��������Ʈ
	//v(4) 4ĭ�� ���� 0���� ä����
	//v(4, 1) 4ĭ�� ���� 1�� ä����
	//�迭���� �ٸ��� ���� �� �ʱ�ȭ�ص� ��

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