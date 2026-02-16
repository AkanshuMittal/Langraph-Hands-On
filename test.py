from langgraph.graph import StateGraph, MessagesState, START, END

# def mock_llm(state: MessagesState):
#     return {"messages": [{"role": "ai", "content": "hello world"}]}


def mock_llm(state: MessagesState):
    user_message = state["messages"][-1].content
    return {"messages": [{"role": "ai", "content": f"You said: {user_message}"}]}

def second_node(state: MessagesState):
    last_ai_message = state["messages"][-1].content
    return {"messages": [{"role": "ai", "content": f"Second node got: {last_ai_message}"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_node(second_node)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", "second_node")
graph.add_edge("second_node", END)
graph = graph.compile()

print(graph.invoke({"messages": [{"role": "user", "content": "hi!"}]}))








