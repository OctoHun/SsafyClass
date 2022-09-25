#include <iostream>
using namespace std;

int main() {
	int tc
	cin >> tc
	for(i=1, i<tc+1, i++){
		int n, ans, flag
		cin >> n
		ans = 1
		flag = 0
		int x[n] = {0}
		int y[n] = {0}
		int z[n] = {0}
		for(j = 0, j<n, j++){
			cin >> x[j] >> y[j] >> z[j]
		}
		if(n>=4){
			for(j = 2, j<n, j++){
				int a, b, c, d
				a = y[0]*(z[1]-z[k]) + y[1]*(z[k]-z[0]) + y[k]*(z[0]-z[1])
      	b = z[0]*(x[1]-x[k]) + z[1]*(x[k]-x[0]) + z[k]*(x[0]-x[1])
      	c = x[0]*(y[1]-y[k]) + x[1]*(y[k]-y[0]) + x[k]*(y[0]-y[1])
      	d = x[0]*(y[1]*z[k] - y[k]*z[1]) + x[1]*(y[k]*z[0] - y[0]*z[k]) + x[k]*(y[0]*z[1] - y[1]*z[0])
				if (a != 0 && b != 0 && c != 0){
					flag = 1
					break
				}
			}
			if(flag){
				for(k=j+1, k<n, k++){
					int func
					func = a*x[k] + b*y[k] + c*z[k]
					if (func != d){
						ans = 0
						break
					}
				}
			}
			
		}
		if(ans){
			cout << '#' << i << ' ' << 'TAK'
		}
		else{
			cout << '#' << i << ' ' << 'NIE'
		}
	}


}