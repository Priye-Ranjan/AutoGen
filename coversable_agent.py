import os
from autogen import ConversableAgent

# Set up Groq config
llm_config_cathy = {
    "api_type": "openai",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": os.environ["GROQ_API_KEY"],  
    "model": "llama3-70b-8192",
    # "temperature": 0.7
}

llm_config_joe = {
    "api_type": "openai",
    "base_url": "https://api.groq.com/openai/v1",
    "api_key": os.environ["GROQ_API_KEY"],
    "model": "llama3-70b-8192",
    # "temperature": 0.9
}


cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of Hindi comedians.",
    llm_config={"config_list": llm_config_cathy},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of Hindi comedians.",
    llm_config={"config_list": llm_config_joe},
    human_input_mode="NEVER",  # Never ask for human input.
)

cathy.initiate_chat(joe, message="Hello Joe, Tell me joke in Hindi",max_turns=2)