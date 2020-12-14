using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using DocumentClassifier.Models;

namespace DocumentClassifier
{
    public interface IDocumentClassifier
    {
        Task<IEnumerable<ClassificationResult>> AutomaticallyClassifyDocuments(IEnumerable<AutoClassificationDocument> autoClassificationDocuments);
        Task<IEnumerable<ClassificationResult>> ManuallyClassifyDocuments(IEnumerable<ManualClassificationDocument> manualClassificationDocuments);
    }
}