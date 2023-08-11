using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AC_day4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int number;
            string[] data = File.ReadAllLines("../../input.txt"); // Tiedoston aukaisu
            int[] ints= new int[0];
            foreach (string line in data) // Pyyhkii tiedostosta pilkut ja väliviivat pois sekä muuttaa arvot integeriksi.
            {
                string line1 = line.Replace("-", " ").Replace(",", " ");
                string[] individualNumbers = line1.Split(' ');
                foreach (string individual in individualNumbers)
                {
                    number = int.Parse(individual);
                    ints = ints.Append(number).ToArray();
                }
            }
            int count = 0; // laskee kuinka monta päällekkäisyyttä on. 
            for (int i = 0; i < ints.Length; i++) // vertailee indexin mukaan lukuja toisiinsa ja tarkoituksena on löytää päällekkäisyyksiä.
            {
                if (ints[i] <= ints[i + 2])
                {
                    if (ints[i + 1] >= ints[i + 3])
                    {
                        count++;
                    }
                }
                if (ints[i] >= ints[i + 2])
                {
                    if (ints[i + 1] <= ints[i + 3])
                    {
                        count++;
                    }
                }
                else if (ints[i + 2] <= ints[i])
                {
                    if (ints[i + 3] >= ints[i + 1])
                    {
                        count++;
                    }
                }
                else if (ints[i + 2] >= ints[i])
                {
                    if (ints[i + 3] <= ints[i])
                    {
                        count++;
                    }
                }
                else
                {
                    Console.WriteLine("Ei");
                }
                i += 3;
            }
            // Tulostaa väärän vastauksen...
            Console.WriteLine(count);
            Console.ReadKey();
        }
    }
}
