using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace methodMan
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Syötä listan pituus: ");
            int askUser = Convert.ToInt32(Console.ReadLine()); // lukujen määrä listalle
            int numbersLen = GenerateNumbers(askUser).Length; // listan pituus
            int[] originalList = GenerateNumbers(askUser); // luo alkuperäinen lista
            PrintNumbers(originalList); // tulosta alkuperäinen lista
            int [] reversedList = Reverse(originalList, (numbersLen - 1)); // listan kääntö
            Console.WriteLine();
            PrintNumbers(reversedList); // tulosta käännetty lista
            Console.ReadKey();
        }
        static int[] GenerateNumbers(int listLength)
        {
            // luo listan käyttäjän asettamasta määrästä
            int[] list = new int[listLength];
            int countForList = 1;
            for (int i = 0; i < listLength; i++)
            {
                list[i] = countForList;
                countForList++;
            }
            return list;
        }
        static void PrintNumbers(int[] printNum)
        {
            // tulostaa listan
            foreach (int number in printNum)
            {
                Console.Write(number + " ");
            }
            Console.WriteLine();
        }
        static int[] Reverse(int[] numbers, int endIndex)
        {
            // kääntää listan korvaamalla listan ensimmäisen numeron viimeisellä siirtäen ensimmäisen temp paikkaan. Temp paikka sen jälkeen siirtyy viimeiseksi. 
            int startIndex = 0;
            int[] strings= new int[numbers.Length];
            while (startIndex < endIndex)
            {
                int temp = numbers[startIndex];
                numbers[startIndex] = numbers[endIndex];
                numbers[endIndex] = temp;
                startIndex++;
                endIndex--;
            }
            return numbers;
        }
    }
}
