#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main(){
    string name,surname;
    int age;
    cin >> name >> surname >> age;
    int lenname = name.length() , lensurname = surname.length();
    if(lenname >= 5 && lensurname >= 5) printf("%c%c%c%d",name[0],name[1],surname[lensurname-1],age%10);
    else printf("%c%d%c",name[0],age,surname[lensurname-1]);
}