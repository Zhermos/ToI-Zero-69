#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B,sum=0,mx,mi;
    cin >> A;
    int lst[A];
    for(int i=0;i<A;i++)cin >> lst[i];
    mx = lst[0];
    mi = lst[0];
    for(int i=0;i<A;i++){
        sum += lst[i];
        if(mx < lst[i])mx = lst[i];
        if(mi > lst[i])mi = lst[i];
    }
    double avg = (double)sum/A;
    printf("%d\n%d\n%d\n%.1f",sum,mx,mi,avg);
}