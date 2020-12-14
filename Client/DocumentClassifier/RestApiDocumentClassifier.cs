using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using DocumentClassifier.Models;

namespace DocumentClassifier
{
    public class RestApiDocumentClassifier : IDocumentClassifier
    {
        private readonly HttpClient _httpClient;

        public RestApiDocumentClassifier(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<IEnumerable<ClassificationResult>> AutomaticallyClassifyDocuments(IEnumerable<AutoClassificationDocument> autoClassificationDocuments)
        {
            var requestBody = new StringContent(JsonSerializer.Serialize(autoClassificationDocuments), Encoding.UTF8, "application/json");
            HttpResponseMessage response = await _httpClient.PostAsync("csharp_python_restfulapi", requestBody);
            response.EnsureSuccessStatusCode();
            string jsonResponse = await response.Content.ReadAsStringAsync();
            return JsonSerializer.Deserialize<IEnumerable<ClassificationResult>>(jsonResponse);
        }

        public Task<IEnumerable<ClassificationResult>> ManuallyClassifyDocuments(IEnumerable<ManualClassificationDocument> manualClassificationDocuments)
        {
            throw new System.NotImplementedException();
        }
    }
}