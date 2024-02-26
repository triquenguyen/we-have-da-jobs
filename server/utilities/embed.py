from transformers import BertModel, BertTokenizer
import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig

class BERT_Embed():
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def get_embedding(self, String: input):
        '''
        Return a [768] tensor embedding
        '''

        # Tokenization and padding
        tokens = self.tokenizer(input, padding=True, truncation=True, return_tensors='pt')

        # Model inference
        with torch.no_grad():
            outputs = self.model(**tokens)

        # Extract embeddings (using mean pooling over tokens)
        text_embedding = outputs.last_hidden_state.mean(dim=1).squeeze()
        return text_embedding
