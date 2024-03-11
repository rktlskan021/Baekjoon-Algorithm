#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int sum = 0, arr[100] = {0,}, m, a, t = 0;
    for(int i=0;i<10;i++){
        cin >> a;
        sum += a;
        arr[a/10]++;
    }
    for(int i=1;i<100;i++){
        if(arr[i] > arr[t]) t = i;
    }
    cout << sum/10 << "\n" << t*10 << endl;
    return 0;
}