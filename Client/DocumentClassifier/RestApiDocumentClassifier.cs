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
            return await MakePostRequest<IEnumerable<ClassificationResult>>("documents/classification/automatic", autoClassificationDocuments);
        }

        public Task<IEnumerable<ClassificationResult>> ManuallyClassifyDocuments(IEnumerable<ManualClassificationDocument> manualClassificationDocuments)
        {
            throw new System.NotImplementedException("Not supported yet.");
        }

        private async Task<T> MakePostRequest<T>(string url, object input)
        {
            var requestBody = new StringContent(JsonSerializer.Serialize(input), Encoding.UTF8, "application/json");
            HttpResponseMessage response = await _httpClient.PostAsync(url, requestBody);
            response.EnsureSuccessStatusCode();
            string jsonResponse = await response.Content.ReadAsStringAsync();
            return JsonSerializer.Deserialize<T>(jsonResponse);
        }
    }
}