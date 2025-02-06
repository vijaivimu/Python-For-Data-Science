from transformers import pipeline
classifier = pipeline(task="sentiment-analysis", model="ProsusAI/finbert")
preds = classifier("outstanding")
print(preds)

#preprocessing - tokenizer



#apply model
#post processing