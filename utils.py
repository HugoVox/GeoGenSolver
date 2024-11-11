import subprocess, os
from deep_translator import GoogleTranslator
def get_grog_api():
    os.environ["GROQ_API_KEY"]="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"
def get_github_token():
    os.environ['GITHUB_TOKEN'] ="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"
def translate(input:str) -> str:
    translated = GoogleTranslator(source='vi', target='en').translate(text=input)
    return translated
def run_ag():
    subprocess.run(["ag4masses/utils/run.sh"])