//day 7

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection.Metadata;

internal class Program
{
    private static void Main(string[] args)
    {
        
            
        string[] data = File.ReadAllLines("E:\\Visual Studio\\repos\\Learning-path-cSharp\\Learning-path-cSharp\\data.txt");

        Dictionary<string, int> folders = new Dictionary<string, int>() { { "/", 0 } };

        List<string> path = new List<string>() { "/" };
        List<string> allFolders = new List<string>() { "/" };
        string current = "/";

        string newWord;

        foreach(string line in data)
        {
            line.Trim();
            var command= line.Split(' ');

            //handle cd command
            if (command[1] == "cd")
            {
                if (command[2] == "/")
                {               
                    path.Clear();                  
                    path.Add("/");     
                    current = "/";               
                }
                else if (command[2] == "..")
                {
                    // comes back
                    path.RemoveAt(path.Count - 1);
                    current = path[^1];
                }
                else
                {
                    //goes forward
                    current += command[2];
                    path.Add(current);
                }
            }
            
            //handle  dir
            if (command[0] == "dir")
            { 
                newWord = current + command[1];
                if ( !allFolders.Contains(newWord))
                    folders.Add(newWord, 0);
                    allFolders.Add(newWord);  
            }
            
            //handle file
            if (command[0] != "$" && command[0] != "dir")
            {
                int file = int.Parse(command[0]);
                
                foreach(string folder in path)
                {
                    folders[folder] += file;
                }
            }    
        }
        int firstStar = 0;
        foreach (KeyValuePair<string, int> folder in folders)
        {
            if (folder.Value <= 100000)
            {
                firstStar += folder.Value;
            }
        }
        

        //second star
        List<int> values = new List<int>();
        foreach (KeyValuePair<string, int> folder in folders)
        {
            values.Add(folder.Value);
        }

        values.Sort();
        int space_to_clean = folders["/"] - 40000000;
        int secondStar = 0;

        foreach(int numb in values)
        {
            if (numb >= space_to_clean) { secondStar = numb; break; } 
        }

        //show results
        Console.WriteLine($"First star: {firstStar}");
        Console.WriteLine($"\nSecond star: {secondStar}");
    }   
}