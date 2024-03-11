#include <iostream>

using namespace std;

int main(){
    int n, m, result=100;
    cin >> n >> m;
    string board[n];
    for(int i=0;i<n;i++){
        cin >> board[i];
    }

    for(int i=0;i<n-7;i++){
        for(int j=0;j<m-7;j++){
            int B = 0, W = 0;
            for(int a=i;a<i+8;a++){
                for(int b=j;b<j+8;b++){
                    if((a+b)%2==0){
                        if(board[a][b] != 'B') W++;
                        if(board[a][b] != 'W') B++;
                    }
                    else{
                        if(board[a][b] != 'B') B++;
                        if(board[a][b] != 'W') W++;
                    }
                }
            }
            if(result > min(B, W)) result = min(B, W);
        }
    }
    cout << result << endl;
}