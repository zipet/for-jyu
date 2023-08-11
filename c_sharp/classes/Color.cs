using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace classes
{
    internal class Color
    {
        private byte red;
        private byte green;
        private byte blue;
        private byte alpha;
        private byte allColors;
        public byte Red
        {
            get
            {
                return red;
            }
            set
            {
                red = value;
            }
        }
        public byte Green
        {
            get
            {
                return green;
            }
            set
            {
                green = value;
            }
        }
        public byte Blue
        {
            get
            {
                return blue;
            }
            set
            {
                blue = value;
            }
        }
        public Color(byte red, byte green, byte blue, byte alpha)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.alpha = alpha;
        }
        public Color(byte red, byte green, byte blue)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            alpha = 255;
        }
        public Color(byte allColors)
        {
            this.allColors = allColors;
        }
        /// <summary>
        /// Palauttaa väri arvot rakennetulle muuttujalle.
        /// </summary>
        /// <returns>Väri arvot joko yhden arvon asetetulle tai jos on kaikille omat arvot asetettu string muodossa.</returns>
        public string GetColors()
        {
            if (allColors > 0)
            {
                this.red = allColors;
                this.green = allColors;
                this.blue = allColors;
                return red + "," + green + "," + blue;
            }
            else
            {
                string redS = this.red.ToString();
                string greenS = this.green.ToString();
                string blueS = this.blue.ToString();
                string alphaS = this.alpha.ToString();
                return redS + "," + greenS + "," + blueS + "," + alphaS;
            }
        }
        /// <summary>
        /// Asettaa uudelleen värit
        /// </summary>
        public void SetColor()
        {
            Console.WriteLine("Syötä uudet värit pallolle.\njärjestyksessä: punainen, vihreä, sininen, alpha");
            byte red, green, blue, alpha;
            red = 46;// Convert.ToByte(Console.ReadLine());
            green = 47;// Convert.ToByte(Console.ReadLine());
            blue = 48;// Convert.ToByte(Console.ReadLine());
            try
            {
                alpha = 49;// Convert.ToByte(Console.ReadLine());
            }
            catch
            {
                alpha = 0;
            }
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.alpha = alpha;
        }
        /// <summary>
        ///  Punaisen, vihreän ja sinisen arvojen keskiarvo lasketaan ja asetetaan se alpha muuttujaan
        /// </summary>
        /// <param name="red"></param>
        /// <param name="green"></param>
        /// <param name="blue"></param>
        /// <returns>Ottaa kolmen värin perusteella harmaan sävyn. Kait.</returns>
        public float SetGray(float red, float green, float blue)
        {
            float gray = (red + green + blue) / 3;
            this.red = (byte)red;
            this.green = (byte)green;
            this.blue = (byte)blue;
            this.alpha = (byte)gray;
            
            return alpha;
        }
        
    }
}
