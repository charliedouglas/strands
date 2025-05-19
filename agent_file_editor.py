from strands import Agent
from strands_tools import file_read, file_write, python_repl

# Create an agent that has the ability to read, write, and run python code
agent = Agent(tools=[file_write, file_read, python_repl])

# Ask the agent a question that uses the available tools
message = """
Create a python file with code that does the following:

1. Generate a random number between 1-1000
2. Divide that number by pi
3. Insert this number into the fibonacci sequence, showing the numbers before and afterwards.

Run the code and display the final output.

If there is a similar file already in existance then this should be used or modified.

"""

agent(message)
