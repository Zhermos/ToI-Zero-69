#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int N,A,sum=0,even=0,odd=0;
    cin >> N;
    for(int i=0;i<N;i++){
        cin  >> A;
        sum += A;
        if(A%2==0)even++;
        else odd++;
    }
    printf("SUM %d\nEVEN %d\nODD %d",sum,even,odd);
}