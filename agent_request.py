from strands import Agent, tool
from strands_tools import file_read, file_write, python_repl, http_request
from strands.agent.conversation_manager import SlidingWindowConversationManager


@tool
def get_user_input(prompt: str = "Please provide input") -> str:
    """
    Get input from the user.

    Use this tool when you need to collect additional information from the user
    to complete a task or answer a question.

    Args:
        prompt: The question or instruction to show to the user

    Returns:
        str: The user's input response
    """
    # Implement the logic to prompt the user and get their input
    user_response = input(f"{prompt}: ")
    return user_response


# Create an agent that has the ability to read, write, run python code, and prompt for user input
agent = Agent(tools=[file_write, file_read, python_repl, http_request, get_user_input])

# Ask the agent a question that uses the available tools
message = """
Follow these instructions:


1. Call the companies house API 
2. Prompt the use for the API token to use
3. Prompt the user for a company name.
4. Ask the user to confirm whether the right company has been found. If not, search again.
5. For that company search and return its details


"""

agent(message)
