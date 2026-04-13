#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;
int main(){
    int x1,y1,z1,x2,y2,z2;
    cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
    double d = sqrt(pow(x2-x1,2)+pow(y2-y1,2)+pow(z2-z1,2));
    printf("%.2f",d);

}