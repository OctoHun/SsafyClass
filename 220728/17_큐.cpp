#include <iostream>
#include <stack>
#include<queue>
using namespace std;



//ť: �����Ҷ� �� ���� push()
// ������ �� �ո� front()
// ���ﶧ�� �� �պ��� pop()

int main() {

	queue<int> st;

	st.push(2);
	st.push(3);
	st.push(6);

	cout << st.front();

	st.pop();
	cout << st.front();

}