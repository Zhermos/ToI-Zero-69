#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A=0,Total=0;
    while (A != 5)
    {
        cin >> A;
        switch (A)
        {
        case 1:
            Total +=100;
            break;
        case 2:
            Total +=120;
            break;
        case 3:
            Total +=200;
            break;
        case 4:
            Total +=60;
            break;
        default:
            break;
        }
    }
    printf("Bye Bye\nTotal Calories: %d",Total);
}