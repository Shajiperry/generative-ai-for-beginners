import os

from openai import OpenAI

# Read the key from your Codespace secret instead of typing it into the file
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
deployment_name = "gpt-5-nano"  # created once, at the top, before it is used

no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

# interpolate the number of recipes, ingredients and filter into the prompt
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used. Strict rule: the recipes must follow this filter: {filter}. Do not include any ingredient that breaks the filter."

print("Asking the model, please wait...")
response = client.responses.create(
    model=deployment_name,
    input=prompt,
)

print(response.output_text)

old_prompt_result = response.output_text
prompt_shopping = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

new_prompt = f"Ingredients I already have: {ingredients}. Generated recipes: {old_prompt_result}. {prompt_shopping}"

print("\nCreating your shopping list, please wait...")
response = client.responses.create(
    model=deployment_name, input=new_prompt, max_output_tokens=4000, store=False
)

# print response
print("\nShopping list:")
print(response.output_text)
