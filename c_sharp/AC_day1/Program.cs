using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AC_day1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num;
            int addedNums = 0;
            string[] input = File.ReadAllLines(@"../../input.txt");
            int[] listedNumbers = new int[0];
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] != "")
                {
                    num = int.Parse(input[i]);
                    addedNums += num;
                }
                else
                {
                    listedNumbers = listedNumbers.Append(addedNums).ToArray();
                    addedNums = 0;
                }                
            }
            int a = int.MinValue;
            foreach (int i in listedNumbers)
            {
                int b = i;
                if (a < b)
                {
                    a = b;
                }               
            }            
            Console.WriteLine(a);
            Array.Sort(listedNumbers);
            Array.Reverse(listedNumbers);
            int threeBiggest = listedNumbers[0] + listedNumbers[1] + listedNumbers[2];
            Console.WriteLine(threeBiggest);

            Console.ReadKey();
        }
    }
}
