using System.Collections.Generic;

//creating the dictionary with letter's values
string letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
Dictionary<char, int> lettersValues = new Dictionary<char, int>();

for (int i = 0; i< letters.Length; i++)
{
    lettersValues.Add(letters[i], i + 1);
}

//start reading the file with commands
string[] lines = File.ReadAllLines("day-3.txt");


int firstStar = 0;
int secondStar = 0;
string first = "";
string second = "";
string third;
int count = 0;
foreach (string line in lines)
{
    string l = line.Trim();

    //first star
    string firstHalf = l.Substring(0, l.Length / 2);
    string secondHalf = l.Substring(l.Length / 2, l.Length / 2);
    
    foreach(char letter in firstHalf){
        if (secondHalf.Contains(letter)){
            firstStar += lettersValues[letter];
            break;
        }
    }

    //second star
    count++;
    if (count == 1){
            first = l;
    }
    if (count == 2){
            second = l;
    }
    if (count == 3){
        third = l;
        foreach (char letter in first){
            if (second.Contains(letter) && third.Contains(letter)){  
                    secondStar += lettersValues[letter];
                    count = 0;
                    break;
            }
        }
    } 
}
//first star result
Console.WriteLine(firstStar);
//second star result
Console.WriteLine(secondStar);