#include <iostream>
using namespace std;
int main(){
    int kap,clock,time;
    cin>>kap>>clock;
    time = kap*clock;
    if(time==0){
        cout<<"No teaching";
    }else{
        if((time/60)==0){
            cout<<time%60<<" minutes";
        }else if((time%60)==0){
            cout<<time/60<<" hours";
        }else{
            cout<<time/60<<" hours "<<time%60<<" minutes";
        }
    }
}