#include <iostream>
using namespace std;
int main(){
    int n,A,B,Temp=0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> A >> B;
        if(A > B){
            cout << A; 
            Temp += A;
        }
        else{
            cout << B;
            Temp += B;
        }
        if(n==1)return 0;
        if(i!=n-1)cout << " + ";
        if(i==n-1)cout << " = ";
    }cout << Temp;
    
}
