using System;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");

            // Declare variables
            string uirWebAPI, exceptionMessage, webResponse;

            // Set the UIR endpoint link. It should go to the application config file 
            uirWebAPI = "http://localhost:5000/api/v1.0/csharp_python_restfulapi_json";
            exceptionMessage = string.Empty;

            // Get web response by calling the CSharpPythonRestfulApiSimpleTest() method
            webResponse = CSharpPythonRestfulApiSimpleTest(uirWebAPI, out exceptionMessage);

            if (string.IsNullOrEmpty(exceptionMessage))
            {
                // No errors occurred. Write the string web response     
                Console.WriteLine(webResponse.ToString());
            }
            else
            {
                // An error occurred. Write the exception message
                Console.WriteLine(exceptionMessage);
            }
        }

        public static string CSharpPythonRestfulApiSimpleTest(string uirWebAPI, out string exceptionMessage)
        {
            exceptionMessage = string.Empty;
            string webResponse = string.Empty;
            try
            {
                Uri uri = new Uri(uirWebAPI);
                WebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create(uri);
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";
                using (StreamWriter streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
                {
                    // Build employee test JSON objec
                    dynamic employee = new JObject();
                    employee.username = "theUserName";
                    employee.password = "thePassword";
                    streamWriter.Write(employee.ToString());
                }
                HttpWebResponse httpWebResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                using (StreamReader streamReader = new StreamReader(httpWebResponse.GetResponseStream()))
                {
                    webResponse = streamReader.ReadToEnd();
                }
            }
            catch (Exception ex)
            {
                exceptionMessage = $"An error occurred. {ex.Message}";
            }
            return webResponse;
        }
    }
}
