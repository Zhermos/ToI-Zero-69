#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int totalSeat, age, amount;
    cin >> totalSeat;
    while (cin >> age >> amount){
        if (age < 15) {
            printf("-1\n");
        }
        else if (amount > totalSeat) {
            printf("-2\n");
            break;
        } 
        else {
            int pricePerTicket = 0;
            if (age >= 15 && age <= 22) pricePerTicket = 120;
            else if (age >= 60) pricePerTicket = 75;
            else pricePerTicket = 150;
            totalSeat -= amount;
            printf("%d %d\n", pricePerTicket * amount, totalSeat);
        }
    }
}