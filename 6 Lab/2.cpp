//Создать массив A[N, N], значение каждого элемента которого равно произведению номера строки и столбца, на пересечении которых он находится.

#include <iostream>
using namespace std;

int main()
{
	int n;
	cout << "Size array" << endl;
	cin >> n;

	int** arr = new int* [n];
	for (int i = 0; i < n; i++)
	{
		arr[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			arr[i][j] = j * i;
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
}
