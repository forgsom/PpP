/*Алгоритм игры :
1.  Компьютер загадывает N - значное число(длина числа задаётся
    пользователем при старте игры и, очевидно, не может превышать 10),
    состоящее из неповторяющихся цифр
    (никакая цифра не может присутствовать в числе дважды, число не может начинаться с нуля).
    Для генерации случайного числа необходимо использовать методы библиотечного класса Random.
    2. Затем пользователь, пытаясь угадать загаданное число, вводит N значное число число.
    3. Компьютер выводит сообщение о том, сколько цифр(коров) угадано, но находится на своих местах.
    4. После чего пользователь переходит к п.2.Раунды продолжаются до тех
    пор, пока пользователь не отгадает загаданное число(т.е.получит четыре “быка”).*/


#include <iostream>
#include <set>
#include <stdlib.h>
using namespace std;

int main()
{
    system("title Быки и Коровы");
    srand(time(0));
    setlocale(0, "");
    int n, chis, fl = 0, ran, win = 0, c = 1;
    set <int> nmb;
    cout << "Введите длину числа: ";
    cin >> n;
    int* cmpt = new int[n];
    int* vsh = new int[n];
    ran = rand() % 9 + 1;
    cmpt[0] = ran;
    nmb.insert(ran);
    for (int i = 1; i < n; i++)
    {
        while (fl != 1)
        {
            ran = rand() % 10;
            if (nmb.find(ran) == nmb.end())
            {
                cmpt[i] = ran;
                nmb.insert(ran);
                fl = 1;
            }
        }
        fl = 0;
    }
    cout << "Раунд #" << c;
    while (win != 1)
    {
        int cow = 0, ox = 0;
        cout << "\nВведите число: ";
        cin >> chis;
        for (int i = n - 1; i >= 0; i--)
        {
            vsh[i] = chis % 10;
            chis = chis / 10;
        }
        for (int i = 0; i < n; i++)
        {
            if (cmpt[i] == vsh[i])
            {
                ox++;
            }
            else
            {
                if (nmb.find(vsh[i]) != nmb.end())
                {
                    cow++;
                }
            }
        }
        if (ox == n)
        {
            cout << "!WIN!";
            win++;
        }
        else
        {
            cout << "Быков: " << ox << "; ";
            cout << "Коров: " << cow;
            cout << "\nTRY AGAIN";
            c++;
            cout << "\nРаунд #" << c;
        }
    }


    getchar();

}
