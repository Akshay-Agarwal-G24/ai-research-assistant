BENCHMARK_DATASET = [
    {
        "id": "retrieval_001",
        "question": "What are the core components (e.g., planning, memory) that turn a standard generative AI model into an autonomous agent?",
        "expected_answer": "An autonomous AI agent consists of goal management, planning, memory, action execution and self-reflection, which together enable it to reason, learn and act autonomously.",
        "category": "knowledge_retrieval",
        "difficulty": "easy"
    },
    {
        "id": "retrieval_002",
        "question": "How does the handbook contrast advanced semantic retrieval from traditional pattern matching?",
        "expected_answer": "The textbook notes that traditional AI systems are largely limited to predictive analytics, static task execution, and basic keyword or pattern matching that simply reacts to immediate stimuli. In contrast, agentic pipelines leverage dense semantic frameworks—similar to those found in Retrieval-Augmented Generation (RAG) systems—to move beyond narrow text matching. This allows the model to map out a broader contextual understanding, enabling the agent to retain memory, decompose complex tasks, and run iterative reasoning loops over data fields rather than just scanning for literal words.",
        "category": "retrieval_reasoning",
        "difficulty": "easy"
    },
    {
        "id": "retrieval_003",
        "question": "How does an iterative execution pattern like ReAct help an agent manage real-world tool use and planning?",
        "expected_answer": "The handbook classifies ReAct as a core design pattern for digital personal assistants that bridges abstract reasoning with real-world action. It allows the LLM to actively combine autonomous multi-step planning with external tools, such as web browsers, code execution environments, or data processors. Rather than executing a rigid script, the agent uses this loop to dynamically select the best tool for a task, analyze the result, and autonomously alter its trajectory if it hits an obstacle, allowing it to navigate complex, non-linear workflows without crashing.",
        "category": "reasoning",
        "difficulty": "medium"
    },
    {
        "id": "retrieval_004",
        "question": "What is the main operational difference between a traditional, static RAG pipeline and an Agentic RAG system?",
        "expected_answer": "The main shift comes down to autonomy and control. In a conventional or naive setup, retrieval is treated as a rigid prompt engineering or preprocessing step to inject text before generation. An Agentic RAG system, however, treats retrieval modules as active tools handled directly by the model's planning layer. Instead of a hardcoded lookup, the agent autonomously decides if and when it needs to fetch information, generates its own search strategies, evaluates the results, and can perform multiple iterative data fetches adaptively to achieve a broader goal.",
        "category": "architecture",
        "difficulty": "medium"
    },
    {
        "id": "retrieval_005",
        "question": "What is the Model Context Protocol (MCP) and how does it structurally change how an agent interacts with external applications?",
        "expected_answer": "The Model Context Protocol (MCP) is an emerging architectural standard designed to provide a structured and secure way for agentic AI to interface with external APIs, databases, and enterprise tools. Its core advantage is that it completely eliminates the need to manually build and hardcode individual integrations for every new service. MCP introduces a universal protocol that enables an autonomous agent to dynamically discover, inspect, and utilize available tools and resources at runtime. This successfully abstracts away the underlying technical friction, allowing the AI to focus entirely on high-level reasoning and goal planning while relying on the protocol to handle safe, standardized external communications.",
        "category": "architecture",
        "difficulty": "hard"
    }
]
