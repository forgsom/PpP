using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication8
{
    internal class Game
    {
        private readonly string _secretNumber;
        private readonly int _length;

        public Game() : this(4) //В конструкторе по-умолчанию вызываем конструктор с int параметром, куда передаем 4
        {
        }

        public Game(int length)
        {
            _length = length;
            var r = new Random();
            var sb = new StringBuilder();
            var set = new HashSet<int>();
            while (sb.Length != length)
            {
                int x = r.Next() % 10; //Генерируем число и берем остаток от деления по 10. То есть получаем цифру 0-9
                if (set.Contains(x)) continue; //Если мы это число уже генерировали, то генерируем заново
                sb.Append(x); //Иначе добавляем в строку
                set.Add(x);   //И в список использованных цифр
            }
            _secretNumber = sb.ToString();
        }

        public bool Try(string inputedNumber, out string result)
        {
            result = "";
            if (inputedNumber == _secretNumber) //Если число угадано, то возвращаем true
                return true;
            result = GetCowsAndTaurs(_secretNumber, inputedNumber, _length); //Иначе считаем количество угаданного
            return false; //И возвращаем, что число, в целом, не угадано
        }

        private static string GetCowsAndTaurs(string secretNumber, string inputedNumber, int length)
        {
            int cows = 0, taurs = 0;
            for (int i = 0; i < length; i++)
                if (secretNumber[i] == inputedNumber[i]) //Если число в точности стоит на том же месте, увеличиваем кол-во быков
                    taurs++;
                else if (secretNumber.Contains(inputedNumber[i])) //Иначе если число в принципе есть в загаданном слове, то увеличиваем коров
                    cows++;
            return string.Format("Быков : {0}\nКоров : {1} ", taurs, cows);
        }
    }

    internal class Program
    {
        private static void Main()
        {
            int length;
            do
            {
                Console.WriteLine("Введите длину загаданного слова");
            } while (!int.TryParse(Console.ReadLine(), out length));
            var game = new Game(length);
            while (true)
            {
                int x; //Нужен просто для проверки, является ли числом
                string inputedNumber;
                do
                {
                    Console.WriteLine("Введите предполагаемое число");
                    inputedNumber = Console.ReadLine();
                } while (!int.TryParse(inputedNumber, out x) ||
                         (!string.IsNullOrEmpty(inputedNumber) && inputedNumber.Length != length));
                /* Цикл, пока введенное число не является непустой строкой,
                 * которое можно преобразовать в число, 
                 * и длина которого соответствует длине нашего слова 
                 */
                string outString;
                if (!game.Try(inputedNumber, out outString))
                    Console.WriteLine(outString);
                else break;
            }
            Console.WriteLine("Вы угадали!!");
            Console.ReadKey();
        }
    }
}
