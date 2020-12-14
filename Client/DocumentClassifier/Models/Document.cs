using System.Collections.Generic;

namespace DocumentClassifier.Models
{
    public abstract class Document
    {
        public IEnumerable<byte> FileContent { get; set; }
    }

    public class AutoClassificationDocument : Document
    {
    }

    public class ManualClassificationDocument : Document
    {
        public string GroupName { get; set; }
    }
}