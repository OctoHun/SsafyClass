#include <iostream>
#include <string>
using namespace std;



int main() {
	string str = "ABC[3512]DEFGF[211]DSFSD[36346]";
	int x = 0;
	int sum = 0;
	int a, b;
	while (1)
	{
		//[]에 있는 수의 합 출력
		a = str.find("[", x);
		b = str.find("]", x);
		if (a == -1) break;
		sum += stoi(str.substr(a + 1, b - a - 1));
		x = b + 1;
	}
	cout << sum;

}