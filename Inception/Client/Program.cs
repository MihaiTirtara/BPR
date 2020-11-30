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
            
            var rest = new RestfullApi.Restfull();

            Console.WriteLine(rest.RestSharpImageClassificationBase64(uirWebAPI,@"C:\Users\mihai\Documents\BPR\image.png","Image can't be transfered"));
            

        }
    }
}
