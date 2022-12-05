internal class Program
{
    private static void Main(string[] args)
    {
        string[] id_list = File.ReadAllLines("ids.txt");

        int contained = 0;
        int overlapped = 0;

        foreach(string id in id_list)
        {
            string[] id_line = id.Split(',', '-');

            int num1 = int.Parse(id_line[0]);
            int num2 = int.Parse(id_line[1]);
            int num3 = int.Parse(id_line[2]);
            int num4 = int.Parse(id_line[3]);

            if (num1 >= num3 && num2 <= num4 || num3 >= num1 && num4 <= num2)
            { 
                contained++;
            };

            if (num3 <= num1 && num1 <= num4 || num3 <= num2 && num2 <= num4 || num1 <= num3 && num3 <= num2 || num1 <= num4 && num4 <= num2)
            {
                overlapped++;
            }
        }

        Console.WriteLine(contained.ToString());
        Console.WriteLine(overlapped.ToString());
    }
}