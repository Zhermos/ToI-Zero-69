#include <iostream>
using namespace std;
int main(){
    bool sale=false;
    int A,price;
    string B;
    cin >> A >> B;
    if(B == "Wed")sale = true;
    if(A<5)price = 0;
    else if(A<=18)price = 100;
    else if(A>=19)price = 150;
    if(sale)price /= 2;cout<< price;
}