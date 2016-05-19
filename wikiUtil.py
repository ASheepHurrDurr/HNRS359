import re

def idify(text):
    return text.strip().replace(" ", "_")
categoryRE = re.compile(r"\[\[(Category:.+?)(?:\|.*)*\]\]")
refRE = re.compile(r"(?:{{[cC]ite ([a-zA-Z\s]+))|{{([cC]itation).*}}")
wikiRE = re.compile(r"^(((Wikipedia)|(Category)|(Template)|(File)|(Portal)):)|(.+\(disambiguation\)\s*$)")
