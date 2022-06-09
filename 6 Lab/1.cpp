//Дан целочисленный массив А[M, N]. Вывести на экран элементы массива, кратные 6, и их индексы

#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian"); //подключение поддержки русского языка
    int Ar[20][20]; //обьявление матрицы
    int i, j, min_num = 0, max_num = 0, min = 0, max = 0, sum = 0, m, n; //обьявление переменных
    cout << "Введите число строк ";
    cin >> m;
    cout << "Введите число столбцов ";
    cin >> n;
    srand(time(NULL));
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            Ar[i][j] = rand() % 10;
        }
    }
    cout << " Матрица \n";
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
            cout << Ar[i][j] << "\t"; // вывод матрицы
        cout << endl;
    }
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            if ((Ar[i][j] % 6 == 0) && (Ar[i][j] != 0))
            {
                cout << endl << Ar[i][j] << endl;
                cout << "строка №" << i << "\t" << "столбец №" << j << endl;
            }
        }
    }
}
