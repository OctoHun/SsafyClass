//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main() {
//	//유효성 검사(valid check)
//	//데이터가 규칙에 해당 되는지 검사
//	//함수로 무조건 빼주는게 좋다.
//
//
//	//정규표현식- 탈락조건 만들때 특수문자를 이용해 판단하는 방법
//	//나중에 쓰고 지금은 일일이 구현
//
//
//	string arr;
//	cin >> arr;
//	int c = 0;
//
//	for (int i = 0; i < arr.size(); i++)
//	{
//		if (arr.size() >= 8)
//		{
//			c++;
//			break;
//		}
//		if (i == 0 && arr[i] < 'A' || arr[i]>'Z')
//		{
//			c++;
//			break;
//		}
//		else if (i>0) {
//			if (arr[i] < 'A' && arr[i] > 'Z')
//			{
//				if (arr[i] < '0' && arr[i]>'9')
//				{
//					c++; break;
//				}
//			}
//		}
//	}
//	if (c > 0) cout << "no";
//	else cout << "yes";
//
//}