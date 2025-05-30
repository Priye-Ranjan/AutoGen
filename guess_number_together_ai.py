import os
from autogen import ConversableAgent

# Print the API key (for debugging, optional)
print("Using TOGETHER_API_KEY:", os.environ.get("TOGETHER_API_KEY"))

# Together.ai config
llm_config_together = {
    "api_type": "openai",  # OpenAI-compatible
    "base_url": "https://api.together.xyz/v1",
    "api_key": os.environ["TOGETHER_API_KEY"],
    "model": "meta-llama/Meta-Llama-3-70B-Instruct-Turbo"
}

# The number to guess
secret_number = 13  # you can change this to any number from 1 to 100

# Agent who *knows* the number and gives feedback
agent_with_number = ConversableAgent(
    name="agent_with_number",
    system_message=(
        f"You are playing a game of 'guess my number'. Your number is {secret_number}. "
        "When the other agent guesses:\n"
        "- If the guessed number > {secret_number}, reply with too high, guessed number\n"
        "- If the guessed number < {secret_number}, reply with too low, gussed numer\n"
        "- If the guessed number = {secret_number}, reply with 'correct'\n"
        "No other text. Just one of those phrases."
    ),
    llm_config={"config_list": [llm_config_together], "temperature": 0.0},
    is_termination_msg=lambda msg: "correct" in msg["content"].lower(),
    human_input_mode="NEVER",
)


# Agent who guesses the number using binary search
agent_guess_number = ConversableAgent(
    name="agent_guess_number",
    system_message=(
        "You're trying to guess a number between 1 and 100 using binary search. "
        "Binary search is an efficient algorithm that repeatedly divides a sorted range in half to quickly locate a target value. "
        "After each guess, the other agent will reply with 'too high', 'too low', or 'correct'. "
        "Based on that, adjust your range accordingly. Keep track of the min and max values.\n\n"
        "Respond only with the next number guess. Don't explain anything. "
        "Start with 50. After each response, update the guessing range appropriately and continue."
    ),
    llm_config={"config_list": [llm_config_together], "temperature": 0.1},
    human_input_mode="NEVER",
)

agent_guess_number.clear_history()
agent_with_number.clear_history()

# Run the interaction
result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)

print("Final result:")
print(result)
