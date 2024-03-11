#include <iostream>

using namespace std;

int main(){
    int n, five = 0, three = 0;
    cin >> n;
    while(true){
        if(n-5<0){
            break;
        }
        n-=5;
        five++;
    }
    if(n-5<0) cout << "-1" << endl; return 0;
    while(true){
        if(n-3<0){
            break;
        }
        n-=3;
        three++;
    }
    if(n-3<0) cout << "-1" << endl;
    else cout << five + three << endl;
    return 0;
}