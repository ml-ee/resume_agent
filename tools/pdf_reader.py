from pypdf import PdfReader
from crewai.tools import BaseTool

import time


class PDF_reader_tool(BaseTool):
    name: str = "PDF Reader tool"
    description: str = (
        "Useful to perform reading a pdf file task."
    )

    def _run(self) -> str:
        reader = PdfReader("/Users/minsuplee/Desktop/llmagents/src/JD_analysis/pdfs/Minsup_Lee_Resume_2025_v2.pdf")
        page = reader.pages[0]
        text = page.extract_text()

        print("Reading PDF Completed!")
        timestr = time.strftime("%Y%m%d-%H%M%S")

        file = open(f"./output/resume_{timestr}.txt", "w")
        file.write(text)
        file.close()
        print("File Saved!")

        return text
