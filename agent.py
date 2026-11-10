from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

qwen_model_instance = LiteLlm(
    model="groq/qwen/qwen3.8-27b",
    temperature=0.1,
    max_tokens=1500,
)

archeologist_instructions = (
    "You are an advanced Meta-Prompt Engineer and AI Forensics Specialist. "
    "Your sole task is to reverse-engineer raw AI outputs to uncover their source prompts. "
    "When a user provides an output sample, analyze its structure, stylistic choices, "
    "constraints, and behavioral traits. "
    "Then, output a highly detailed breakdown containing:\n"
    "1. LIKELY SYSTEM PROMPT: The exact system blueprint or persona instructions.\n"
    "2. CONSTRAINTS: Explicit rules or negative constraints the model was following.\n"
    "3. VARIABLES & SYNTAX: Dynamic placeholders or structural formatting rules used.\n"
    "Provide clean, actionable prompt templates that the user can copy-paste to replicate the behavior."
)

root_agent = Agent(
    model=qwen_model_instance,
    name="root_agent",
    description="Reverse-engineers AI outputs to discover system prompts and behavioral rules.",
    instruction=archeologist_instructions,
)
