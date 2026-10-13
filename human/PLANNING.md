# PLANNING

What’s Missing: 
- Agent ergonomics
	- Could go in tools section
- Exploration into more complicated techniques like context injection…might be fine to define things like this earlier but don’t want to make chapter two too advanced
- “Agents are an environment problem” might need to be introduced earlier
- Some mention in the intro about how using LLMs in the SDLC is sometimes perceived as something that requires no engineering skill. When in reality, LLMs are a tool that can be controlled and used to produce incredible results when treated as such. (Might be too opinionated/divisive but it grinds my gears when people just say that llm coding leads to skill atrophy, lack of understanding, things like that.) This might be true. Like I’m not as good at writing code line by line as I was a few years ago. But I’m producing significantly more, higher-quality work than I ever have. Yeah, def too opinionated.  

- Always On/Proactive Agents
    - This requires a whole chapter for sure
        - What's it look like when we have agents who truly operate like coworkers? Because that's coming very, very soon
        - The anatomy of systems like this
            - How to build one

## Introduction

## Part One: Foundations

### Chapter One: The Agentic Loop
- How LLMs work
	- Mentioning multimodal models? Will be important for tool use…
- How the Agentic Loop works

### Chapter Two: The Agentic Primitives
- Model
	- Will have highest impact on agent performance
- Context
	- Everything that agent loop is aware of
	- Intelligence degradation
		- “Smart Zone” vs “Dumb Zone” (use different terminology)
	- Context Injection
		- Just-in-time retrieval systems (seems too advanced for Chapter 2…)
	- Context Compaction
	- Context management techniques used by harnesses
- Trigger
	- Prompts
	- Non-human triggers
		- Cron triggers, webhooks, event-based triggers
- Tools
	- How the agent takes action
	- Agent Ergonomics
		- Context usage within tools
		- Different ways to use tools:
			- Agent Ergonomics
				- Harness Level built-ins
				- CLI
				- MCP
- Harness
	- Congregation of the above four
	- Agent = model + harness
	- Context 

## Part Two: The Individual Ladder

### Chapter Three: Conversational Agents
- Commonly seen as harnesses which are based in chat applications as web apps/CLI
- Exclusively driven by human triggers (prompts)
	- Reactive systems, not proactive

### Chapter Four: Parallelization
- Multiple conversations at a time. Does this really need a whole chapter? 

### Chapter Five: Orchestration
- Having agents drive other agents. Agent-produced triggers create new agents rather than human based triggers

### Chapter Six: Autonomous Delegation
- Code driven, agent driven, and human driven triggers working together
- Code driven triggers:
	- Web hooks, cron jobs. Note that agent loop is still reactive, not proactive. Reactive systems can be chained to create proactive systems.

### Chapter Seven: Agents are an Environment Problem
- Where the agents are working matters just as much as the agent itself
	- Shaping codebases to treat agents as first class consumers
	- How do agents validate their work
	- Placing trust in the system that uses agents rather than agents themselves

### Chapter Eight: Automating the SDLC


## Part Three: The Organizational Ladder

### Chapter Nine: The Spectrum of Adoption
- Individual engineer conversational agents
- Shared tools, triggers, harness, context, model access at org/team level

