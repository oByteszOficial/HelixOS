using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleUI
{
    internal class Program
    {

        public static void Space(string[] args)
        {
            Console.WriteLine(" \n \n \n \n \n \n ");
        }

        public static void Boot()
        {

            string Aarch = "cc64";

            Console.Clear();
            Thread.Sleep(500);
            Console.WriteLine("Hello World!");
            Thread.Sleep(3000);
            Space(args);

        }

        public static void Container(string[] args)
        {

            Console.WriteLine("Entering ConsoleContainer...");
            Console.WriteLine("Booting up...");
            Thread.Sleep(1000);
            Boot();

        }

        public static void Main(string[] args)
        {

            Container(args);

        }

    }
}
