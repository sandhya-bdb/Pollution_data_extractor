import json
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException

# Initialise the LLM
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

def extract_pollution_data(article_text: str):
    prompt = f"""
You are an expert data extractor. Read the following news article about environmental pollution in India.
Return the extracted information **ONLY in JSON format**, nothing else. Do not include any explanation or extra text.

Suggested keys (use if relevant): 
  "title", "location", "pollutant", "source", 
  "data_value", "standard_or_limit", "impact", 
  "policy_action", "key_points"

Article:
========
{article_text}
"""

    pt = PromptTemplate.from_template(prompt)
    chain = pt | llm
    response = chain.invoke({"article": article_text})
    text_output = response.content.strip()

    # Clean code-block wrappers if present
    if text_output.startswith("```"):
        # remove leading/trailing backticks and any markdown language hint
        text_output = text_output.strip("`")
        # remove optional "json" indicator
        if text_output.lstrip().startswith("json"):
            text_output = text_output.lstrip()[4:].strip()

    # Try to parse JSON
    try:
        result = json.loads(text_output)
        return result
    except json.JSONDecodeError:
        # attempt to extract JSON substring
        import re
        match = re.search(r"\{.*\}", text_output, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                raise OutputParserException("Model returned invalid JSON after cleaning.")
        raise OutputParserException("Model did not return valid JSON.")

