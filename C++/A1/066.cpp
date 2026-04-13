#include <iostream>
using namespace std;
int main(){
    int A,B,Temp=0,i=0;
    cin >> A >> B;
    while (true)
    {
        Temp += A;
        A -= 2;
        i++;
        if(Temp>=B){cout<<i;break;}
        else if(A<=0&&Temp<B){cout<<i;break;}
    }
    
}