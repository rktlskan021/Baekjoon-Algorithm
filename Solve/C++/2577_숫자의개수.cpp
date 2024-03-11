#include <iostream>

using namespace std;

int main(){
    int a,b,c,arr[10] = {0,};
    cin >> a >> b >> c;
    a = a * b * c;
    while(a){
        arr[a%10]++;
        a/=10;
    }
    for(int i=0;i<10;i++) cout << arr[i] << endl;
    return 0;
}