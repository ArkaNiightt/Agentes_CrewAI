# Config Chave API

- Criar arquivo ENV: `OPENAI_API_KEY=INSIRA_AQUI_SUA_CHAVE_API`
- Instalar DOTENV: `pip install python-dotenv`
- Importar DOTENV: `from dotenv import load_dotenv`
- Importar OS: `import os`
- Carregar DOTENV: `load_dotenv()`

## Config MODELO LLM

- Atribuir API_KEY a uma variável: `openai_api_key = os.getenv('OPENAI_API_KEY')`
- Instalar LANGCHAIN: `pip install langchain langchain_community`
- Importar CHAT_MODEL: `from langchain_community.chat_models import ChatOpenAI`
- Atribuir LLM a uma variável: `openai_llm = ChatOpenAI(model_name='gpt-4-1106-preview', api_key=openai_api_key)`

## Class Agent()

- `role: str` =  Campo(descrição: "Função do agente")
- `goal: str` = Campo(descrição: "Objetivo do agete")
- `backstory: str` = Campo(descrição: "História de fundo do agente")
- `max_rpm: Optional(int)` = Campo(padrão: None, descrição: "Número máximo de requisições por minuto para execução do agente ser respeitada.")
- `memory: bool` = Campo(padrão: True, descrição: "Se o agente deve ter memória ou não")
- `verbose: bool` = Campo(padrão: False, descrição: "Modo verboso para a Execução do Agente")
- `allow_delegation: bool` = Campo(padrão: True, descrição: "Permitir delegação de tarefas)
- `tools: Optional[List(Any)]` = Campo(padrão: list, descrição: "Ferramenta à disposição dos agentes")
- `max_iter: Optional[int]` = Campo(padrão: 15, descrição: "Iterações máximas para um agente executar uma tarefa")
- `setp_callback: Optional[Any]` = Campo(padrão: None, descrição: "Callback a ser executado após cada passo de execução do agente")
- `llm: Any` = Campo(padrão: lambda: `ChatOpenAI(model=os.environ.get("OPEN_MODEL_NAME", "gpt-4"))`, descrição: "Modelo de linguagem que que executará o agente")
- `function_calling_llm: Optional[Any]` = Campo(descrição: "Modelo de linguagem que executará o agente", padrão: None)