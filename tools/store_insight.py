from pypdf import PdfReader
from crewai.tools import BaseTool

import time


class Store_findings(BaseTool):
    name: str = "Storing findings"
    description: str = (
        "Useful to append and store the findings into an existing markdown file"
    )

    def _run(self, candidate_fullname: str, content: str) -> str:
        
        timestr = time.strftime("%Y%m%d-%H%M%S")

        file = open(f"./output/summary_{timestr}.md", "a")
        file.write(f"# {candidate_fullname} \n{timestr}\n\n")
        file.write(content)
        file.close()

        print("Insignts Stored into a Markdown!")

        # return text
