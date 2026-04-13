#include <iostream>
using namespace std;
int main(){
    int d,m;
    cin >> d >> m;
    string zodiac[] = {
        "capricorn", "aquarius", "pisces", "aries", "taurus", "gemini",
        "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"
    };
    int cutoff[] = {0, 20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 22, 22};
    if(d < cutoff[m])cout << zodiac[m-1];
    else cout << zodiac[m];


}
