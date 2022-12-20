using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

internal class Program
{
    private static void Main(string[] args)
    {
        static void Day5(int len) {

            string data = File.ReadAllText("E:\\Visual Studio\\repos\\Learning-path-cSharp\\Learning-path-cSharp\\data.txt");

            int star = 0;
            List<char> packet = new List<char>();
            foreach (char character in data)
            {
                
                if (packet.Count < len)
                {
                    star++;
                    packet.Add(character);
                }
                else
                {
                    if (packet.Distinct().ToList().Count == packet.Count) 
                    {
                        Console.WriteLine(star);
                        break;
                    }
                    else
                    {
                        star++;
                        packet.RemoveAt(0);
                        packet.Add(character);
                        
                    }
                }
            }
        }
        
        Console.WriteLine("First star: ");
        Day5(4);
        Console.WriteLine("\nSecond star:");
        Day5(14);  
    }   
}