#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main(){
    string original,reversed;
    cin >> original;
    reversed = original;
    reverse(reversed.begin(),reversed.end());
    int d1 = original[0]-'0',d2 = original[1]-'0',d3 = original[2]-'0',d4 = original[3]-'0',d5 = original[4]-'0',sum=d1+d2+d3+d4+d5,multiply=d1*d2*d3*d4*d5;
    if(d1>5)cout<<9;
    else if(d2>5)cout<<10;
    else if(d3>5)cout<<11;
    else if(d4>5)cout<<12;
    else if(d5>5)cout<<14;
    else cout << 13;

    if(original == reversed){
        if(d1+d5>5)cout<<1;
        else if(d2*d4>5)cout<<2;
        else cout<<0;
    }else{
        if(round((double)d5 / d1) > 5)cout<<1;
        else if(d2-d5>5)cout<<2;
        else cout<<0;
    }
    if(sum>25)cout<<1;
    else if(multiply>55)cout<<2;
    else cout<<0;
}