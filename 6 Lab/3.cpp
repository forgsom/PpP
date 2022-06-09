//Дан целочисленный массив А[M, N]. Найти среднее арифметическое каждой строки.


#include <iostream>
#include <ctime>
using namespace std;


int main()
{
	int n, m;
	float arg;
	srand(time(NULL));
	cout << "Col: ";
	cin >> m;
	cout << "Row: ";
	cin >> n;


	int** arr = new int* [n];
	for (int i = 0; i < n; i++)
	{
		arr[i] = new int[m];
		for (int j = 0; j < m; j++)
		{
			arr[i][j] = rand() % 10;
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;


	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			arg += arr[i][j];
		}
		cout << "Average of " << i << " row " << arg / m << endl;
	}
}
