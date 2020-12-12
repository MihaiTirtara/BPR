using System;
using System.Net;
using RestSharp;

namespace RestfullApi
{
    public class Restfull : IRESTfull
    { 
        public string RestSharpImageClassification(string url, string imagePathName, string exceptionMessage)
        {
            exceptionMessage = string.Empty;
            string responseContent = string.Empty;
            
            try
            {
               
                RestRequest request = new RestRequest(Method.POST);
                request.AddFile("content",imagePathName);
                

                RestClient restClient = new RestClient(url);
                IRestResponse response = restClient.Execute(request);
                string errmsg = response.ErrorMessage;

                if (string.IsNullOrEmpty(errmsg))
                {
                    responseContent = response.Content.ToString();
                }
                else
                {
                    responseContent = errmsg;
                }

            }
            catch (Exception ex)
            {
                exceptionMessage = $"An error occured.{ex.Message}";
            }
            return responseContent;
        }


    }
}