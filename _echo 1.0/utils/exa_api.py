from exa_py import Exa
import json

with open("./keys.json") as file:
    data = json.load(file)

exa_key = data["EXA_KEY"]

exa = Exa(api_key = exa_key)

def web_search(prompt):
    print(f"I start searching {prompt}")

    result = exa.search_and_contents(
        f"{prompt}",
        type="auto",
        text=True,
        num_results=3
    )

    print(f"I end searching this is result:")

    answers = []
    for r in result.results:
        print(r.title)
        print(r.url)

        text = r.text[:200] + ("..." if len(r.text) > 200 else "")
        print(text)
        print()

        answers.append(f"{r.title}\n{text}\n{r.url}")

    final_answer = "\n---\n".join(answers)
    return final_answer
