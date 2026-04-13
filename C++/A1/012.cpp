#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int number,reverse = 0,reminder,temp;
    char symbol;
    cin >> number >> symbol;
    temp = number;;
    while (temp != 0)
    {
        reminder = temp % 10;
        reverse = (reverse*10)+reminder;
        temp /= 10;
    }
    switch (symbol)
    {
    case '+':
        printf("%d + %d = %d",number,reverse,number+reverse);
        break;
    case '*':
        printf("%d * %d = %d",number,reverse,number*reverse);
        break;
    default:
        break;
    }

    
}