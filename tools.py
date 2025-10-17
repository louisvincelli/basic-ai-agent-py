#one for looking up Wikipedia, one for going to DuckDuckGo and searching something,
#and one custom tool i wrote myself for a python function
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

#tool import helps us wrap or create our own custom tool. SAVING AS CUSTOM FILE. save_to_file
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

#once you have function wrap it as a tool. dont call function just write name of it no ().
#you can make  a tool that calls an api
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    #name cant have space search_web. Description is a must more detailed even.
    name="search",
    func=search.run,
    description="Search the web for information",
)

#Wikipedia tool
#limit to 1 result from wikipedia but can change to 5, etc. max characters
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)