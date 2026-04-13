#include <iostream>
using namespace std;
int main(){
    int A,B;
    cin >> A >> B;
    for(int i=0;i<A;i++){
        for(int j=0;j<B;j++){
            if(A%2==0){
                if(i+1<=A/2)cout<<"A";
                if(i+1>A/2)cout<<"K";
                cout<<" ";
            }
            else if(A%2!=0){
                if(i+1<=A/2+1)cout<<"A";
                if(i+1>A/2+1)cout<<"K";
                cout<<" ";
            }
        }cout<<endl;
    }
}