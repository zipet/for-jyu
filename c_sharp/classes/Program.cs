using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace classes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine("Syötä värit pallolle järjestyksessä: punainen, vihreä, sininen, alpha");
            byte red, green, blue, alpha;
            red = 26;//Convert.ToByte(Console.ReadLine());
            green = 27;//Convert.ToByte(Console.ReadLine());
            blue = 28;//Convert.ToByte(Console.ReadLine());
            try
            {
                alpha = 29;//Convert.ToByte(Console.ReadLine()); 
            }
            catch
            {
                alpha = 0;
            }
            Color color1 = new Color(red, green, blue, alpha);
            Color allColor = new Color(77);
            string colorForBall = color1.GetColors();
            Ball ball1 = new Ball(84, colorForBall);

            ball1.ShowBall();
            ball1.Pop();
            ball1.ThrowBall();
            ball1.ThrowBall();
            ball1.ThrowBall();
            Color color2 = new Color(red, green, blue) { Red = 32, Green = 33, Blue = 34 };
            Console.WriteLine(color2.Red);
            Console.WriteLine(color2.Green);
            Console.WriteLine(color2.Blue);
            Console.WriteLine(color2.GetColors());
            Console.ReadKey();
        }
    }
}
