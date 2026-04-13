#include <iostream>
using namespace std;
int main(){
    int A,count=0;
    char Temp , vowel[]={'A','E','I','O','U'};
    cin >> A;
    for(int i=0;i<A;i++){
        cin >> Temp;
        for(int j=0;j<5;j++){
            if(Temp == vowel[j])count++;
        }
    }
    cout << count;
}