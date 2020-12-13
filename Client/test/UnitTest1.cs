using System;
using Xunit;

namespace Client
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            var uirWebAPI = "http://localhost:5000/api/v1.0/csharp_python_restfulapi";
            var exceptionMessage = string.Empty;

            var expectedOutput = @"""The document is a Letter""";

            var rest = new RestfullApi.Restfull();
            var webResponse = rest.RestSharpImageClassification(uirWebAPI,
             @"C:\Users\mihai\Documents\BPR4\letter.png",
             "Image can't be transfered");
            string cleanedResponse = webResponse.Replace("\n", "").Replace("\r", "");
            Assert.Equal(expectedOutput, cleanedResponse);
        }
    }
}
