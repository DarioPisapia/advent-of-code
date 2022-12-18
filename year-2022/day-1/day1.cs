DAY1.day1();
class DAY1
{
    public static void day1()
    {
        string[] allLines = File.ReadAllLines("E:\\Visual Studio\\repos\\Learning-path-cSharp\\Learning-path-cSharp\\AOC\\day1\\day1-data.txt");

        List<int> elfAndCalories = new List<int>();

        int caloriesCount = 0;
        foreach(string line in allLines)
        {
            if(line != "")
            {
                caloriesCount = caloriesCount + int.Parse(line);
            }
            else
            {
                elfAndCalories.Add(caloriesCount);
                caloriesCount = 0;
            }
        }
       
        elfAndCalories.Sort();
        elfAndCalories.Reverse();
        Console.WriteLine($"first star: {elfAndCalories[0]}");

        //second part
        int secondStar = 0;
        for (int i = 0; i < 3; i++)
        {
            secondStar += elfAndCalories[i];
        }
        Console.WriteLine($"Second star: {secondStar}");
    }
}
