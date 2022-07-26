#include <iostream>
using namespace std;
int main() {
	// cin의 속도를 높이기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie();
	cout.tie();

	/*
	
		#include <iostream>
			using namespace std;
			int main() {
				int arr[] = { 1, 3, 5, 1, 1, 4, 9 };
				int n = 7;
				int dat[10] = { 0 };
				for (int i = 0; i < n; i++) {
					dat[arr[i]]++;
				}
				int cnt = 0;
				for (int i = 0; i < 10; i++) {
					if (dat[i] > 0) cnt++;
				}
				cout << cnt;
				return 0;
			}
			*/

	int arr[7] = { 15,30,15,15,30,5,9 };
	int arr1[100] = { 0 }, max = 0, a;;
	for (int i = 0; i < 7; i++)
	{
		arr1[arr[i]]++;
	}
	for (int i = 0; i < 100; i++)
	{
		if (arr1[i] > max)
		{
			a = i;
			max = arr1[i];
		}

	}
	cout << a;

	/*
	#include <iostream>
using namespace std;
int main() {
	int arr[] = { 15, 30, 15, 15, 30, 5, 9 };
	int n = 7;
	int dat[101] = { 0 };
	//dat 채우기
	for (int i = 0; i < n; i++) {
		dat[arr[i]]++;
	}
	int max = 0;
	int maxIndex = 0;
	for (int i = 0; i < 101; i++) {
		if (dat[i] > max) {
			max = dat[i];
			maxIndex = i;
		}
	}
	cout << maxIndex;
	return 0;
}*/

}