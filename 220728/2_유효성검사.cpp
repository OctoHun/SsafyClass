//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main() {
//	//��ȿ�� �˻�(valid check)
//	//�����Ͱ� ��Ģ�� �ش� �Ǵ��� �˻�
//	//�Լ��� ������ ���ִ°� ����.
//
//
//	//����ǥ����- Ż������ ���鶧 Ư�����ڸ� �̿��� �Ǵ��ϴ� ���
//	//���߿� ���� ������ ������ ����
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