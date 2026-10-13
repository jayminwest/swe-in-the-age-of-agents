# Interview: Agents are an environment problem

source: interview (Claude Code session), 2026-10-13
touches: gen/ Ch6, Agents are an Environment Problem

## Q1. Picture an agent that fails in a codebase that isn't prepared for it. What does that failure actually look like, and what about the environment caused it?

Sure. When an agent is failing in a code base, it's because, or what it looks like actually is agent writing code that is like slop, basically. It's not long-term. It's, you know, very short-sighted code that's pretty hacky. And it just is going to fail the test of being durable long-term. So it doesn't operate, or it's like writing tests that doesn't adhere to the linting rule. or style guides, you know, stuff like that. And the environment caused it because of a lack of checks on agent work where the agent, if it's able to just do it however it wants to do it, it's going to do it in a way that isn't being verified by the environment. Or if it's not being verified by the environment, it's going to become incredibly inconsistent over time. I think this is going down as models get better, but I do still think it's important, if it's a code basis where an agent can't just fit everything into its context window and it has to understand legacy code and millions of millions of lines of code, it's still important. I also think there's this common consolidation of functionality in agent-written code where you'll have these mega files or mega functions that are doing everything for code base. When really that should be, in my opinion at least, should be split up for healthier long-term maintenance. It just becomes pretty sloppy. There's a great Irindill post about this. This is sort of why I built out Trellis as well. I have some information on this. Don't mention it by name, but that's why I built the Trellis tool.

Steward notes (not Jaymin's words):
- "Irindill post": name unclear in transcription. Not looked up (no passive research). Awaiting the link or text in inbox/.
- Trellis: never named in gen/ prose. Its design is a candidate source once Jaymin points at the material.

## Q2. A prepared environment has checks the unprepared one lacks. What are they, concretely? Which one catches the mega-file/mega-function consolidation?

This is the post I was talking about: https://earendil.com/posts/measuring-code-sloppiness/

Okay, well, I understand that it's important to have some idea of the actual mechanisms. Like, I think you're getting a little bit low level here in terms of what I want to put in the book because I don't want to be like, you have to have this linter installed for your agents. Like, that's stupid. That's not relevant to anything at all. And the actual mechanisms, like, I have lists of hundreds of these things. So, like me, being able to just spout it off in text here is not a good idea. Very high level. What it looks like is, you know, ratcheting a code base. Ratchets only go up. So, you know, test coverage only goes up. File size only goes down. Or, you know, whatever that looks like. It's making sure that there's ratchets in place. And then there's linting, making sure that all the code is consistent, style guides, making sure that documentation is kept up to date. I mean, this is good to, like, work through this list. I mean, it's going to be talking about it. It's going to be, you know, lots and lots of lines. So, have a sub-agent go and look at the, like, templates. I think it's a template repo and projects. Let me find the name for you.

/Users/jayminwest/Projects/scaffold-project and /Users/jayminwest/Projects/os-eco/trellis

those will have the philosophy but again, this isn't like a "put these X things in your codebase and you'll be good!" it's about the mindset behind it, the philosophy behind it

Steward notes (not Jaymin's words):
- "Irindill" = Earendil. Post: inbox/2026-10-13-earendil-measuring-code-sloppiness.md.
- Book altitude: mindset and philosophy, never a checklist of tools. Mechanisms appear only as examples of a principle.
