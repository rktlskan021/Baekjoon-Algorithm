#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        string a;
        int b;
        cin >> b >> a;
        a.erase(b-1, 1);
        cout << a << endl;
    }
    return 0;
}