import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from transformers import pipeline
classifier = pipeline('sentiment-analysis', framework='tf')
result = classifier("I love using transformers!")
print(result)