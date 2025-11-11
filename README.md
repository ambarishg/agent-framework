## Agent Framework Playground

This repository is a lightweight playground for experimenting with the `agent-framework-core`
package and Azure OpenAI. It contains a simple Python chat client plus a set of companion
notebooks that demonstrate how to build and orchestrate agents with the magnetic workflow
building blocks.

### Repository layout

| Path | Description |
| --- | --- |
| `chat_client.py` | Minimal agent chat loop that connects to Azure OpenAI via `AzureOpenAIChatClient`. |
| `config.py` | Loads configuration from `.env` and exposes Azure-specific constants. |
| `requirements.txt` | Runtime dependencies for the Python scripts and notebooks. |
| `simple_agent.ipynb` / `supervisor.ipynb` / `tool*.ipynb` | Notebook experiments that accompany the agent framework. |
| `.env.sample` | Template for the environment variables required by `config.py`. |

### Prerequisites

- Python 3.10 or newer
- Azure OpenAI resource with a GPT‑4o (or compatible) deployment
- (Optional) Jupyter Notebook or VS Code for exploring the notebooks

### Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure secrets by copying the sample and filling in your values:
   ```bash
   cp .env.sample .env
   ```

   Required variables:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_DEPLOYMENT_GPT_4O_ID`
   - `AZURE_OPENAI_DEPLOYMENT_ID` (used by `config.py`, add this entry to `.env` as needed)

### Running the chat client

After setup, execute:

```bash
python chat_client.py
```

The script instantiates `AzureOpenAIChatClient`, wires it into a `MagenticBuilder`, and streams
agent responses to the console. Adjust logging levels inside `chat_client.py` if you need more
verbose tracing.

### Working with the notebooks

1. Launch Jupyter (or VS Code’s notebook interface).
2. Open any of the `*.ipynb` files:
   - `00.install.ipynb` walks through environment bootstrap steps.
   - `magentic_one.ipynb` and `simple_agent.ipynb` illustrate basic agent patterns.
   - `supervisor.ipynb`, `tool.ipynb`, and `tools.ipynb` demonstrate orchestration examples.
3. Ensure the notebook kernel uses the same virtual environment that has the dependencies
   installed and the `.env` file available so that `config.py` can resolve credentials.

### Troubleshooting

- **Auth failures**: Double-check that the `.env` file contains the exact deployment IDs and
  endpoint/key for the Azure resource region you created.
- **Package import errors**: Re-run `pip install -r requirements.txt` inside the active
  environment to ensure `agent-framework-core` and friends are available.
- **Notebook cannot find variables**: Restart the kernel after editing `.env`, or call
  `load_dotenv()` manually at the top of a notebook cell.

### Contributing

This is still a personal sandbox, so feel free to fork or adapt to your own Azure OpenAI setup.
If you expand the framework usage (e.g., add tools or workflows), document them here to keep the
README in sync.
