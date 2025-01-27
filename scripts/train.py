#this chunk over here verifies that the
#set up can interact with hugginface lib
from transformers import pipeline

# Test a simple sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

result = classifier("I love using transformers!")
print(result)