//#include <iostream>
//using namespace std;
//
//char path[4];
//void run(int x) {
//	//����ġ��= ���� ��ü�� ���ϵ���
//
//	//�� ��°, �ϴ� ���� �߸��������� �ٷ� ����
//	/*if (x == 1 && path[0] == '3') return;
//	if (x == 1 && path[0] == '4') return;*/
//
//	if (x == 3)
//	{
//		cout << path << endl;
//		return;
//	}
//	for (int i = 0; i < 4; i++)
//	{
//		//ù ��°, �� �ȿ� if���� �Ἥ �ϴ� ���
//		/*if (x == 0 && i == 2) continue;
//		if (x == 0 && i == 3) continue;*/
//		path[x] = '1' + i;
//		run(x + 1);
//		path[x] = '0';
//	}
//}
//
//int main() {
//	run(0);
//}