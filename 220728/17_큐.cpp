#include <iostream>
#include <stack>
#include<queue>
using namespace std;



//큐: 저장할땐 걍 저장 push()
// 읽을땐 맨 앞만 front()
// 지울때도 맨 앞부터 pop()

int main() {

	queue<int> st;

	st.push(2);
	st.push(3);
	st.push(6);

	cout << st.front();

	st.pop();
	cout << st.front();

}