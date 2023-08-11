using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace classes
{
    internal class Ball
    {
        private int radius;
        private string color;
        private int throwTracker;


        public Ball(int radius, string color)
        {
            this.radius = radius;
            this.color = color;
        }
        public Ball(int radius)
        {
            this.radius = radius;
        }
        
        public void Pop()
        {
            this.radius -= this.radius;
            Console.WriteLine("Ball is now popped. " + this.radius);
        }
        public void ShowBall()
        {
            Console.WriteLine("Pallon halkaisija: " + this.radius);
            Console.WriteLine("Pallon väri: " + this.color);
        }
        public void ThrowBall()
        {
            this.throwTracker += 1;
            Console.WriteLine(this.throwTracker);
        }
    }
}
