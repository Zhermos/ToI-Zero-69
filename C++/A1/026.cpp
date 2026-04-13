#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A[3],odd=0,even=0;
    cin >> A[0] >> A[1] >> A[2];
    for(int i=0;i<3;i++){
        if(A[i]%2==0){
            even+=1;
        }else odd+=1;
    }
    printf("even %d\nodd %d",even,odd);
}