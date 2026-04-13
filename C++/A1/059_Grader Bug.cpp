#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    string from,to;
    bool check=true;
    int A,B;
    float C;
    cin >> from >> to >> C;
    string route = from + "-" + to;
    if(route == "BKK-CNX"){A=10;B=30;}
    else if(route == "CNX-UBP"){A=15;B=40;}
    else if(route == "UBP-BKK"){A=20;B=40;}
    else if(route == "BKK-PKT"){A=25;B=50;}
    else if(route == "PKT-CNX"){A=30;B=60;}
    else if(route == "UBP-PKT"){A=40;B=70;}
    else check = false;
    if(check)printf("%.2f",A+(B*C));
    else if(!check)cout << "Error";
}       