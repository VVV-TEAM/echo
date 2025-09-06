from exa_py import Exa
import json

with open("./keys.json") as file:
    data = json.load(file)

exa_key = data["EXA_KEY"]

exa = Exa(api_key = exa_key)

# web search for important information
def web_search(prompt):

    print(f"I start searching {prompt}")

    # search
    result = exa.search_and_contents(
        f"{prompt}",
        type="auto",
        text=True,      
        num_results=3
    )

    print(f"I end searching this is result:")

    for r in result.results:
        print(r.title)
        print(r.url)
        print()

        result = r.title

        print(result)

    return(result)

# I working on search. Just please wait <3