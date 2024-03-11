#include <iostream>
#include <string>
using namespace std;

int main(){
    int count = 0, i = 655, n;
    cin >> n;
    while(true){
        if(count == n){
            break;
        }
        if(to_string(i).find("666") != string::npos) count++;
        i++;
    }
    cout << i-1 << endl;
    return 0;
}