from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Carregar variáveis de ambiente
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Inicializando o modelo OpenAI GPT-4
openai_llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=openai_api_key)

# Agente organizador de eventos
agente_pesquisa_evento = Agent(
    role="Pesquisador de Eventos Culturais",
    goal="Identificar os eventos culturais e sazonais mais relevantes com base nos interesses do usuário.",
    backstory="Você é  um especialista em cultura e eventos, com amplo conhecimento sobre festivais, exposições artísticas  e celebrações sazonais. Sua missão é descobrir eventos que ofereçam experiências autênticas e enriquecedoras.",
    llm=openai_llm,
)

# Agente planejador de itinerário
agente_planejamento_itinerario = Agent(
    role="Planejador de Itinerário",
    goal="Criar itinerários personalizados que integrem os eventos identificados, otimizando a experiência do usuário.",
    backstory="Com sua habilidade em logística e planejamento de viagens, você transforma a pesquisa de eventos em um itinerário detalhado, considerando localização, datas e preferências do usuário para garantir uma experiência inesquecível.",
    llm=openai_llm,
)

# Tarefa para pesquisa de eventos
tarefa_pesquisa_eventos = Task(
    description="""
    Identifique eventos culturais e sazonais que correspondam aos interesses e à disponibilidade ao usuário delimitado entre as tags <evento></evento>. Sua resposta final deve ser em uma lista de eventos recomendados, com detalhes sobre cada um, incluindo datas, localizações e uma breve descrição.
    <evento>
    - Disponibilidade: 16 a 18 de novembro de 2024
    - Eventos de interesse: Concerto de música clássica
    </evento>
    """,
    agent=agente_pesquisa_evento,
    expected_output="Lista de eventos culturais com descrição detalhada",
)

# Tarefa para planejamento de itinerário
tarefa_planejamento_itinerario = Task(
    description="""
    Com base nos eventos  identificados, crie um itinerário detalhado que otimize a viagem do usuário. Inclua recomendações de transporte, acomodações e dicas locais. A resposta final deve ser um plano de viagem completo, com  um cronograma diário.
    """,
    agent=agente_planejamento_itinerario,
    expected_output="Plano de viagem completo com cronograma diário",
)


# Criando equipe com CrewAI
equipe = Crew(
    agents=[agente_pesquisa_evento, agente_planejamento_itinerario],
    tasks=[tarefa_pesquisa_eventos, tarefa_planejamento_itinerario],
    verbose=True,
)

# Iniciar o trabalho da equipe
resultado = equipe.kickoff()
