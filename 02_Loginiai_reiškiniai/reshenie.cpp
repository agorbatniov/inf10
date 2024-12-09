#include <iostream>
using namespace std;

int main() {
    // Входные данные: A - движение, B - свет
    int A, B;
    cout << "Введите движение (1 - есть, 0 - нет): ";
    cin >> A;
    cout << "Введите свет (1 - есть, 0 - нет): ";
    cin >> B;

    // Расчёт результата
    bool result = (A && B) || (A && !B);

    // Вывод результата
    if (result) {
        cout << "Сигнал включён" << endl;
    } else {
        cout << "Сигнал выключен" << endl;
    }

    return 0;
}