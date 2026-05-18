---
description: Use when the user asks to find or suggest sources for a term or topic.
---

The user wants to find sources. The search topic is either:
- Provided after the slash command (treat as $ARGUMENTS if present), OR
- The most recently discussed term or topic in this conversation

Search the web for academic papers, articles, rulebooks, or transcripts
relevant to that topic in the context of Japanese gaming language. For each result:
- Title, author, date, URL
- One-sentence summary of relevance
- Suggested raw/ subdirectory (papers/, articles/, transcripts/, manuals/)
- Whether it appears freely available or paywalled

Append results to queries/source-suggestions.md under a ## heading with today's date and the search topic. Do not download or write anything to raw/.
