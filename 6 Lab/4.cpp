//Дан целочисленный массив А[M, N]. Поменять местами минимальный и максимальный элементы.


#include <iostream>
#include <ctime>
using namespace std;


int main()
{
    srand(time(NULL));
    bool flag = false;
    int Ar[20][20];
    int i, j, k = 0, m, n, max_ = 0, min_ = 999;
    cout << "Row: ";
    cin >> m;
    cout << "Col: ";
    cin >> n;


    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            Ar[i][j] = rand() % 10;
        }
    }


    cout << "Original" << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
            cout << Ar[i][j] << "\t";
        cout << endl;
    }


    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (Ar[i][j] > max_)
            {
                max_ = Ar[i][j];
            }
            if (Ar[i][j] < min_)
            {
                min_ = Ar[i][j];
            }
        }   
        cout << endl;
    }


    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (Ar[i][j] == max_)
            {
                Ar[i][j] = min_;
                continue;
            }
            if (Ar[i][j] == min_)
            {
                Ar[i][j] = max_;
            }
        }
        cout << endl;
    }


    cout << endl << "RESULT" << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
            cout << Ar[i][j] << "\t";
        cout << endl;
    }
}
