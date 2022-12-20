
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

internal class Program
{
    private static void Main(string[] args)
    {
        
        string[] data = File.ReadAllLines("E:\\Visual Studio\\repos\\Learning-path-cSharp\\Learning-path-cSharp\\data.txt");

        //first star
        static string FirstStar(string[] data)
        {
            List<List<char>> crates = new List<List<char>>
                {
                    new List<char>{'B', 'W', 'N' },
                    new List<char>{ 'L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'},
                    new List<char>{ 'Q', 'H', 'Z', 'W', 'R'},
                    new List<char>{ 'W', 'D', 'V', 'J', 'Z', 'R'},
                    new List<char>{ 'S', 'H', 'M', 'B'},
                    new List<char>{ 'L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'},
                    new List<char>{ 'J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'},
                    new List<char>{ 'W', 'F', 'S', 'J', 'G', 'Q', 'B'},
                    new List<char>{ 'Z', 'W', 'M', 'S', 'C', 'D', 'J'}
                };

            foreach (string line in data)
            {
                string[] command = line.Split(' ');
                int numOfCrates = int.Parse(command[1]);
                int from = int.Parse(command[3]) - 1;
                int to = int.Parse(command[5]) - 1;

                while (numOfCrates > 0)
                {
                    char lastCrate = crates[from].Last();
                    crates[from].RemoveAt(crates[from].Count - 1);
                    crates[to].Add(lastCrate);
                    numOfCrates--;
                }
            }

            string firstStar = "";
            foreach (List<char> t in crates)
            {
                firstStar += t.Last();
            }
            return firstStar;

        }
        
        //second star
        static string SecondStar(string[] data)
        {
            List<List<char>> crates = new List<List<char>>
                {
                    new List<char>{'B', 'W', 'N' },
                    new List<char>{ 'L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'},
                    new List<char>{ 'Q', 'H', 'Z', 'W', 'R'},
                    new List<char>{ 'W', 'D', 'V', 'J', 'Z', 'R'},
                    new List<char>{ 'S', 'H', 'M', 'B'},
                    new List<char>{ 'L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'},
                    new List<char>{ 'J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'},
                    new List<char>{ 'W', 'F', 'S', 'J', 'G', 'Q', 'B'},
                    new List<char>{ 'Z', 'W', 'M', 'S', 'C', 'D', 'J'}
                };
            foreach (string line in data)
            {
                string[] command = line.Split(' ');
                int numOfCrates = int.Parse(command[1]);
                int from = int.Parse(command[3]) - 1;
                int to = int.Parse(command[5]) - 1;


                List<char> cratesRemoved = crates[from].GetRange(index: crates[from].Count - numOfCrates, numOfCrates);
                crates[to].AddRange(cratesRemoved);
                crates[from].RemoveRange(crates[from].Count - numOfCrates, numOfCrates);

            }

            string secondStar = "";
            foreach (List<char> t in crates)
            {
                secondStar += t.Last();
            }
            return secondStar;
        }
        //results
        Console.WriteLine($"First star: {FirstStar(data)}");
        Console.WriteLine($"Second star: {SecondStar(data)}");
    }
}