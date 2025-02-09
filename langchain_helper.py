from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import gemini_api_key

import os
os.environ['GOOGLE_API_KEY'] = gemini_api_key

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Generate restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Generate menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return them as a comma-separated string."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine chains sequentially
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'cuisine': cuisine})
    return response
