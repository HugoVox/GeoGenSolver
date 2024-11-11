from reader import Reader
from ag import *
import os
from deep_translator import GoogleTranslator
os.environ["GROQ_API_KEY"]="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"
os.environ['GITHUB_TOKEN'] ="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"
reader = Reader(model='gpt-4o-mini') # or model='gemma2-9b-it'
input = "Cho tam giác cân ABC (AB = AC), các đường cao AD, BE, cắt nhau tại H. Gọi O là tâm đường tròn ngoại tiếp tam giác AHE. Chứng minh tứ giác CEHD nội tiếp."
translated = GoogleTranslator(source='vi', target='en').translate(text=input)
reader.main(translated)
run_ag()