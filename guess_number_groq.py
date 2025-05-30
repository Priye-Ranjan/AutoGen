import os
from autogen import ConversableAgent

# Set up Groq config
llm_config_agent_player = {
    "api_type": "openai",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": os.environ["GROQ_API_KEY"],  
    "model": "llama3-70b-8192",
    # "temperature": 0.7
}

llm_config_agent_number = {
    "api_type": "openai",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": os.environ["GROQ_API_KEY"],
    "model": "llama3-70b-8192",
    # "temperature": 0.9
}

# agent_with_number = ConversableAgent(
#     "agent_with_number",
#     system_message="You are playing a game of guess-my-number. "
#     "In the first game, you have the "
#     "number 53 in your mind, and I will try to guess it. "
#     "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
#     llm_config={"config_list": llm_config_agent_number},
#     max_consecutive_auto_reply=1,  # maximum number of consecutive auto-replies before asking for human input
#     is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
#     human_input_mode="TERMINATE",  # ask for human input until the game is terminated
# )

# agent_guess_number = ConversableAgent(
#     "agent_guess_number",
#     system_message="I have a number in my mind, and you will try to guess it. "
#     "If I say 'too high', you should guess a lower number. If I say 'too low', "
#     "you should guess a higher number. ",
#     llm_config={"config_list": llm_config_agent_player},
#     human_input_mode="NEVER",
# )

# result = agent_with_number.initiate_chat(
#     agent_guess_number,
#     message="I have a number between 1 and 100. Guess it!",
# )


# Automatic game play without human intervention

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="You are playing a game of guess-my-number. You have the "
    "number 53 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. You remember all past guesses of the guesser and respond properly. ",
    llm_config={"config_list": llm_config_agent_player},
    is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config={"config_list": llm_config_agent_player},
    human_input_mode="NEVER",
)


result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)
