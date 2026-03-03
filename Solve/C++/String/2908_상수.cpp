#include <iostream>

using namespace std;

int main(){
    string a, b;
    string result;
    cin >> a >> b;
    for(int i=0;i<3;i++){
        if(a[i] == b[i]) continue;

        if(a[i] > b[i]){
            result = a;
        }
        else{
            result = b;
        }
    }
    cout << result[2] << result[1] << result[0] << endl;
    return 0;
}