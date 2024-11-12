import subprocess, os
import regex as re
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
def read_solution():
    with open('solution.out', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        paragraphs = ''.join(lines).split('\n\n')
        theorem_premises = paragraphs[0].strip()
        auxiliary_constructions = paragraphs[1].strip()
        proof_steps = paragraphs[2].strip()
        proof_steps = re.sub(r'\d+\. ', '- Ta có:\n', proof_steps)
        proof_steps = re.sub(r' & ', '\n', proof_steps)
        proof_steps = re.sub(r' ⇒ ', '\n⇒ ', proof_steps)
        result = {
            theorem_premises.split('\n')[0]: GoogleTranslator(target='vi').translate(text='\n'.join(theorem_premises.split('\n')[1:])),
            auxiliary_constructions.split('\n')[0]: GoogleTranslator(target='vi').translate(text='\n'.join(auxiliary_constructions.split('\n')[1:])),
            proof_steps.split('\n')[0]: GoogleTranslator(target='vi').translate(text='\n'.join(proof_steps.split('\n')[1:]))
        }
    return result