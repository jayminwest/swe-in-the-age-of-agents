# Chapter 2: The Primitives

An agent is built from five primitives: the model powering the loop, the  tokens that are input to and outputted by the model (the context), the tools the agent has access to, the initial trigger for the agentic loop, and the harness in which these are all defined. Put simply: model, context, tools, trigger, and harness. 

## Model

The model powering the agent will have the largest impact on what that agent is capable of, and how effective it is. Different models have different underlying weights and will therefore have different behaviors. 

## Context

## Tools

## Triggers

Triggers initiate the agentic loop. The most common trigger is a user submitted prompt, as seen in every chat-based system. As agentic systems become more advanced, long running, and autonomous, triggers begin to take a different shape. 

Scheduled triggers using cron jobs move towards agentic loops that can begin without any user intervention. An example use case would be to do a regular security review of a repo, where the instructions for the agent are supplied by the scheduled trigger. 

Another popular trigger system is done by providing an agent with a tool to trigger children agents, known as “subagents”. These agent loops run within the top level loop and return their results back to the base top level agent. 

## Harness

