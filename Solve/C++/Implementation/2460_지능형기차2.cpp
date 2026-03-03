#include <iostream>

using namespace std;

int main(){
    int a, b;
    int m = 0, h = 0;
    
    for(int i=0;i<10;i++){
        cin >> a >> b;
        h = h - a + b;
        if(m<h) m = h;
    }
    cout << m << endl;

    return 0;
}