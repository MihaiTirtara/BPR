using System;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Drawing;
using RestSharp;

namespace RestfullApi
{
    public class Restfull : IRESTfull
    {
        public string RestfullSimpleTest(string url, string exceptionMessage)
        {
            exceptionMessage = string.Empty;
            string webResponse = string.Empty;
            try
            {
                Uri uri = new Uri(url);
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
        public string RestfulImageClassificationBase64(string url, string imagePathName, string exceptionMessage)
        {
            var base64Text = string.Empty;
            exceptionMessage = string.Empty;
            var webResponse = string.Empty;

            try
            {
                var uri = new Uri(url);
                var httpRequest = (HttpWebRequest)WebRequest.Create(uri);
                httpRequest.ContentType = "application/json";
                httpRequest.Method = "POST";
                base64Text = ImageFileTobase64String(imagePathName);
                using (var streamWriter = new StreamWriter(httpRequest.GetRequestStream()))
                {
                    dynamic imageJson = new JObject();
                    imageJson.content = base64Text;
                    streamWriter.Write(imageJson.ToString());
                }

                var httpResponse = (HttpWebResponse)httpRequest.GetResponse();

                using (StreamReader streamReader = new StreamReader(httpResponse.GetResponseStream()))
                {
                    webResponse = streamReader.ReadToEnd();
                }
            }
            catch (Exception ex)
            {
                exceptionMessage = $"An error occured.{ex.Message}";
            }

            return webResponse;
        }
        public string RestSharpImageClassificationBase64(string url, string imagePathName, string exceptionMessage)
        {
            var base64Text = string.Empty;
            var ImageJsonText = string.Empty;
            exceptionMessage = string.Empty;
            string responseContent = string.Empty;

            try
            {
                base64Text = ImageFileTobase64String(imagePathName);
                ImageJsonText = Base64ToJson(base64Text);
                RestRequest request = new RestRequest(Method.POST);
                var byteArray = File.ReadAllBytes(imagePathName);
                //request.AddHeader("content-type", "application/json");
                //request.AddParameter("application/json", ImageJsonText, ParameterType.RequestBody);
                
                request.AddFile("content",imagePathName);
                

                RestClient restClient = new RestClient(url);
                IRestResponse response = restClient.Execute(request);
                string errmsg = response.ErrorMessage;

                if (string.IsNullOrEmpty(errmsg))
                {
                    responseContent = response.Content;
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

        private string ImageFileTobase64String(string imagePath)
        {
            var base64Text = string.Empty;
            try
            {
                using (var image = Image.FromFile(imagePath))
                {
                    using (var memoryStream = new MemoryStream())
                    {
                        image.Save(memoryStream, image.RawFormat);
                        var imageBytes = memoryStream.ToArray();
                        base64Text = Convert.ToBase64String(imageBytes);
                    }
                }
            }
            catch (Exception e)
            {
                var exceptionMessage = $"An error occured.{e.Message}";
            }

            return base64Text;
        }

        private string Base64ToJson(string base64Text)
        {
            string ImageJsonText = string.Empty;
            try
            {
                dynamic imageJson = new JObject();
                imageJson.content = base64Text;
                ImageJsonText = imageJson.ToString();
            }
            catch (Exception ex)
            {
                string exceptionMessage = $"An error occured.{ex.Message}";
            }
            return ImageJsonText;
        }
    }
}