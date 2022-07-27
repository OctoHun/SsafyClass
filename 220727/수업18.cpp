//#include <iostream>
//#include <string>
//using namespace std;
//
//
//int main() {
//
//	string strs = "ABC[3512]DEFG";
//	//문자열 안에 있는 []한세트, 이 안에 있는 숫자 발굴하고 77을 더해 출력
//
//	int start = strs.find("[", 0);
//	int end = strs.find("]", 0);
//	string ans = strs.substr(start+1, end - start-1);
//	cout << stoi(ans) + 77;
//}