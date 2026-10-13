# Chapter One

## Introduction (Pre-Chapter One?)
The advent of large language models (LLMs) has revolutionized software engineering. The process of building software projects is unrecognizable  compared to any other point in the industry’s history. 

The intention of this book is to formalize a guide for understanding this new paradigm. The content is anchored to concepts which have proven to be largely immune from the fast flowing, constantly shifting stream of developments and updates in the agentic space. Names for specific tools, models, and providers will be omitted in an effort to establish this book as a durable asset. 

Models and tooling will continue maturing and growing in intelligence, effectiveness, and reliability. Their underlying primitives will remain the same as long as LLMs and code are what power them. 

It is assumed that readers of this book have at least basic experience with using agentic tooling in the process of writing code. 

## Chapter One: Foundations and The Agentic Loop

Every agentic application is built on the same foundation: the agentic loop. The agentic loop is defined as an autonomous execution cycle where a model repeatedly reasons, acts, and observes results until reaching a defined goal or stopping condition. 

This loop is how LLMs are able to produce meaningful work. Chapter two will discuss the primitives of the loop. To develop a shared understanding of how this loop is driven, we must understand how LLMs work at a high level.

The dominant architecture for modern Large Language Models is the transformer. The transformer architecture is well documented and while generally useful, a detailed understanding of such models is not required for understanding how to use agents effectively. As such, this book will not attempt to explain this in detail. 

What is important for working with agents is understanding that LLMs are next token predictors. Given a string of tokens, the model will produce the next most statistically probable token. For example, given the sentence “The capital of France is” the next most likely token will be “Paris” assuming the model has been trained on accurate data. However, given this process is non-deterministic, there is a small chance that the model outputs an inaccurate token like “London”. These inaccuracies are commonly referred to as “hallucinations”. 

At the scale of modern LLMs, next token prediction produces results which are coherent and increasingly intelligent. The assumption of the industry is that continuing to scale and refine training runs will create more intelligent models, a trend which has held true since the first LLMs were developed. 

The agentic loop relies on models outputting the correct tokens to continue driving the loop. Their outputs are fed as inputs for the next model call until the task has been completed. An instance of a running agentic loop is referred to as an “agent”. Although the term “agent” has been used in various contexts, for this book it is defined as an instance of the agentic loop powered by an LLM. 

The next chapter will explore the primitives of the agentic loop in more detail.  
