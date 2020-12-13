using System;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;

namespace Client
{
    class Client
    {
        static void Main(string[] args)
        {
            string uirWebAPI, exceptionMessage, webResponse;
            
            // Set the UIR endpoint link. It should go to the application config file 
            uirWebAPI = "http://localhost:5000/api/v1.0/csharp_python_restfulapi";
            exceptionMessage = string.Empty;
            
            var rest = new RestfullApi.Restfull();
            webResponse = rest.RestSharpImageClassification(uirWebAPI,@"C:\Users\mihai\Documents\BPR4\output-1.png","Image can't be transfered");

            Console.WriteLine(webResponse);
            

        }
    }
}
