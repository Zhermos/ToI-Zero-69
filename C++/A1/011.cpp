#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main(){
    string A;
    cin >> A;
    for(int i=0;i<A.length();i++){
        int count = 1;
        while(i+1<A.length()&&A[i]==A[i+1])
        {
            count++;
            i++;
        }
        cout << count << A[i];
        
    }
}