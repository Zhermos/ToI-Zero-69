#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;
int main(){
    int x=0,y=0,d;
    string n;
    cin >> n;
    int len = n.length();
    for(int i=0;i<len;i++){
        switch (n[i])
        {
        case 'N':
            y+=1;
            break;
        case 'S':
            y-=1;
            break;
        case 'E':
            x+=1;
            break;
        case 'W':
            x-=1;
            break;
        
        default:
            break;
        }
    }
    printf("%d %d %d",x,y,d=abs(x)+abs(y));

    
}
