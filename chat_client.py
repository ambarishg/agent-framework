from config import *
from agent_framework import (
    ChatAgent,
    MagenticAgentMessageEvent,
    MagenticBuilder,
    MagenticCallbackEvent,
    MagenticCallbackMode,
    MagenticOrchestratorMessageEvent,
    WorkflowOutputEvent,
)
from agent_framework.azure import AzureOpenAIChatClient
import random
from pydantic import Field
from typing import Annotated
from datetime import datetime, timedelta
import logging

AZURE_OPENAI_API_VERSION = "2024-12-01-preview"

chat_client = AzureOpenAIChatClient(
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    deployment_name=AZURE_OPENAI_DEPLOYMENT_GPT_4O_ID,
)


logging.basicConfig(level=logging.WARNING, force=True, format="%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

