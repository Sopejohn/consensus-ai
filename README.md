# Consensus AI

Consensus AI is a platform designed to enhance the reliability and accuracy of AI-generated responses by fostering collaboration between multiple large language models (LLMs) like GPT, Claude, and Llama. By leveraging the strengths of each model, Consensus AI delivers more accurate and consistent results, reducing the likelihood of hallucinations.

## Features

- **Collaborative AI**: Integrates GPT, Claude, and Llama to analyze user queries and provide the most accurate response.
- **Voting System**: Each model votes on the best response, and the one with the highest votes is presented to the user.
- **Multi-Model Memory**: Tracks conversation history across models, allowing for context-aware responses.
- **User-Friendly Interface**: Built with React, HTML, CSS, and JavaScript to ensure an optimal user experience.

## Demo

Watch our [demo video](https://vimeo.com/966142111) to see Consensus AI in action. Here’s what you’ll see:

1. **Greeting Query**: See how Consensus AI handles a basic query.
2. **Fictional Episode Query**: Discover how the voting system filters out hallucinated responses.
3. **Memory Feature**: Experience how Consensus AI recalls previous conversations for context-aware interactions.

## How It Works

1. **Frontend**: Developed using React, HTML, CSS, and JavaScript.
2. **Backend**: Built with Python and Flask, managing API calls, response storage, and the voting system.
3. **LLM Integration**: Queries are distributed among multiple LLMs, each generating a response.
4. **Voting System**: Models vote on each other’s responses, and the highest-voted answer is selected.

## Challenges

- API setup complexities
- Parallelizing API calls for improved response times
- Deciding on the optimal system architecture

## Accomplishments

- Successfully integrated multiple LLMs to create a more accurate and reliable AI response system.
- Implemented a memory feature that stores conversation history across models.

## Lessons Learned

- Full-stack development
- Working with LLM APIs
- Parallelizing processes for efficiency

## Future Plans

- Expand support to include more web API models.
- Allow users to plug-and-play their own models.
- Implement user authentication and chat history storage.
