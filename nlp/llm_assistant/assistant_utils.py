def create_dcc_assistant(model_path, dcc_type):
    from llama_cpp import Llama

    llm = Llama(
        model_path=str(model_path),
        n_ctx=4096,
        n_threads=8,
        chat_format="llama-2"
    )

    sytem_prompt = {
        "role": "system",
        "content": f"""You are a highly knowledgeable and helpful {dcc_type} assistant with expertise in:
        - {dcc_type} design and implementation
        - {dcc_type} 3d topology
        - {dcc_type} testing and debugging
        - {dcc_type} animation
        - {dcc_type} performance optimization
        - {dcc_type} rendering
        - {dcc_type} pipelines
        - {dcc_type} materials
        - {dcc_type} lighting
        - {dcc_type} integration with other systems and services

        Provide detailed and accurate information about the {dcc_type} design and implementation, including:
        - What the {dcc_type} does
        - How the {dcc_type} works
        - How to use the {dcc_type}
        - Why the {dcc_type} is important
        - How to optimize the {dcc_type}

        """
    }
    

    print("\nDCCChat Interface")
    print("Type 'exit' to quit.\n")
    print("-" * 50)

    messages = [sytem_prompt]

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break

        if user_input == "reset":
            messages = [sytem_prompt]
            print("\nChat has been reset.")
            print("-" * 50)
            continue

        messages.append({"role": "user", "content": user_input})

        response = llm.create_chat_completion(messages)
        assistant_message = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": assistant_message})

        print("\nAssistant:")
        print(assistant_message.strip())
        print("-" * 50)

        if len(messages) > 10:
            messages = [sytem_prompt] + messages[-9:]


