using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using DocumentClassifier;
using DocumentClassifier.Models;
using Xunit;

namespace TestClient
{
    public class TestClient
    {
        private readonly RestApiDocumentClassifier _documentClassifier;

        public TestClient()
        {
            var httpClient = new HttpClient()
            {
                BaseAddress = new Uri("http://localhost:5000/api/v1.0/")
            };

            // In actual NoblyDoc project the implementation would be dependency injected for the interface, instead of hardcoding the implementation, as here.
            _documentClassifier = new RestApiDocumentClassifier(httpClient);
        }
        
        
        [Fact]
        public async Task Test_AutomaticallyClassifyDocuments()
        {
            var documents = new List<AutoClassificationDocument>
            {
                new AutoClassificationDocument {FileContent = await File.ReadAllBytesAsync(@"letter.png")}
            };
            List<ClassificationResult> classificationResults = (await _documentClassifier.AutomaticallyClassifyDocuments(documents)).ToList();
            
            Assert.Equal("Letter", classificationResults[0].GroupName);
        }
    }
}