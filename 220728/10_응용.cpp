#include <iostream>
#include <vector>
using namespace std;



struct Node {
	int a, b;
};



vector<vector<Node>> alist;
int used[5];


void run(int now, int sum) {
	for (int i = 0; i < alist[now].size(); i++) {
		Node next = alist[now][i];

		//next.loc : ���� �� �� ��ġ
		//next.price : ���� �� ���� ����
	}
}



int main() {

	alist[1] = { {2,7} };
	alist[2] = { {3,5},{4,10} };
	alist[3] = { {4,2} };
	




}