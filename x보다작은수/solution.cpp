#include<iostream>
using namespace std;

int main(){
    cout << "되고 있어?" <<endl;
    
    int N, X;

    cin >> N >> X ;

    int a[N];
    for(int i = 0 ; i < N ; i++){
        cin >> a[i];
    }

    for(int i = 0; i < N; i++){
        if(a[i] > X){
            cout << a[i] << '\t' ;
        }
    }
}