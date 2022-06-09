//Дано число N. Составить программу заполнения массива числами треугольника Паскаля и вывода этого массива.



#include <iostream>

using namespace std;

int main()
{
	int m;
	cout << "Size of arr: ";
	cin >> m;

	int v = 1;
	int g = 1;
	int arr[m][m] = {};

	for (int i = 0; i < m; i++)
	{
		arr[i][0] = v;
	}
	for (int i = 0; i < m; i++)
	{
		arr[0][i] = g;
	}
	for (int i = 1; i < m; i++)
	{
		for (int j = 1; j < m; j++)
		{
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1];
		}
	}
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << arr[i][j] << "\t";
		}
		cout << endl;
	}
}
