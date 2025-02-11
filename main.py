from crew import ResumeCrew
import os
import agentops
from agentops.session import EndState

import time


def run_crew():
    start_time = time.time()

    agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), auto_start_session=False)
    session = agentops.start_session()

    inputs = {
        "question": "what school did this candidate go to for undergraduate, and which degree(s) were earned?"
    }

    result = ResumeCrew().crew().kickoff(inputs=inputs)
    print(result)


    session.end_session(EndState.SUCCESS.value)


    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {round(elapsed_time, 2)} seconds")
    
run_crew()