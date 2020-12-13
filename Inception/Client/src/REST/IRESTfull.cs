using System;
namespace RestfullApi
{
    public interface IRESTfull
    {
        string RestfullSimpleTest(string url,  string exceptionMessage);
        string RestfulImageClassificationBase64(string url, string imagePathName, string exceptionMessage);
        string RestSharpImageClassificationBase64(string url, string imagePathName, string exceptionMessage);


    }

}