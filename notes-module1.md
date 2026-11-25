what is agentic AI?
- iterative - thinking/ research -> Revise
- LLM based app that makes multiple steps to complete a task
- Can add a human in a loop step
- Complexs task -> breaking it down to smaller steps for agentic workflows to complete one step at a time
- Reflective Research Agent

Degrees of automony? (eg: write an essay about black holes)
- Less autonomous
-- LLM (write web search queries) -> Web search -> Web fetch -> LLM (Write essay) -> essay
-- All steps predetermined
-- All tools use hard coded
-- Autonomyu is in text generation
- More autonomous
-- LLM (Search web - Tools (Websearch - news - arXiv)) -> Web Search -> LLM (Fetch 5 best sources - Tools (web fetch - pdf to text)) -> Web fetch -> LLM (write essay draft) -> LLM (reflect and improve draft) -> essay
-- Agent can make some decisions, choose tools
-- all tools predefined
- High autonomous
-- decides the sequence of steps themselves
-- Agent makes many decisions autonomouosly
-- can create new tools on the fly
-- a bit more unpredictable

Benefits?
- do tasks effectivily
- Paralellism Parallelization for speed
-- fetches topresults and each steps can be checked parallely
-- Each steps ion the LLM runs for multiple results parallely
- modularity
-- add/ swap out components
-- 3 parallel searchs/ use different components for each LLM serahc/ result search
