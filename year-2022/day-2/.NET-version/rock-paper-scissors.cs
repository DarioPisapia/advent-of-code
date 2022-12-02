internal class Program
{
    private static void Main(string[] args)
    {
        string[] strategy = File.ReadAllLines("../strategy.txt");

        int sum = 0;
        int sum2 = 0;

        //First part
        foreach (string round in strategy){

            if (round[2] == 'X')
            {
                sum += 1;
                if (round[0] == 'A')
                {
                    sum += 3;
                }
                if (round[0] == 'C')
                {
                    sum += 6;
                }
            }

            if (round[2] == 'Y')
            {
                sum += 2;
                if (round[0] == 'B')
                {
                    sum += 3;
                }
                if (round[0] == 'A')
                {
                    sum += 6;
                }
            }

            if (round[2] == 'Z')
            {
                sum += 3;
                if (round[0] == 'C')
                {
                    sum += 3;
                }
                if (round[0] == 'B')
                {
                    sum += 6;
                }
            }

        }

        //Second part
        foreach (string round in strategy)
        {
            if (round[0] == 'A')
            {
                if (round[2] == 'X')
                {
                    sum2 += 3;
                }
                if (round[2] == 'Y')
                {
                    sum2 += 4;
                } 
                if (round[2] == 'Z') 
                {
                    sum2 += 8; 
                }
                    
            }
            if (round[0] == 'B')
            {
                if (round[2] == 'X')
                {
                    sum2 += 1;
                }
                if (round[2] == 'Y')
                {
                    sum2 += 5;
                }
                if (round[2] == 'Z')
                {
                    sum2 += 9;
                }

            }
            if (round[0] == 'C')
            {
                if (round[2] == 'X')
                {
                    sum2 += 2;
                }
                if (round[2] == 'Y')
                {
                    sum2 += 6;
                }
                if (round[2] == 'Z')
                {
                    sum2 += 7;
                }

            }
        }
       Console.WriteLine($"La prima somma è: {sum}\nLa seconda somma è: {sum2}");
    }
}