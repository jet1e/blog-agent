---
title: 'Researching the Web with AI: The Good, the Bad and the Hallucinations'
date: '2024-11-20'
picture: '/blog/researchWeb/main.png'
author: 'Samuel Cunningham'
author_image: '/blog/authors/sam.jpg'
keywords: ['OpenAI','Copilots','Microsoft365','GPT Search', 'Perplexity AI']
---

## Introduction
The rise of AI-powered search tools has transformed how we gather information from the web, promising faster, smarter, and more accurate results. With tools like Microsoft 365 Copilot, OpenAI’s GPT Search, and Perplexity AI competing to redefine research workflows, I decided to put them to the test.

The challenge was simple:
- Identify AI companies based in Perth.
- List their top three services.
- Provide their website and address.
- Compile all this information into a CSV file.

This experiment not only highlights the potential of AI tools to streamline research but also exposes their challenges, such as hallucinations, inconsistent performance, and tool functionality.

## Microsoft 365 Copilot
My initial tests with 365 Copilot showed promising results. Copilot was able to search the web and correctly create an up-to-date list of AI companies in Perth. 

![Microsoft365 Copilot searching the web](/blog/researchWeb/copilot1-worked.png)
_Figure 1: Microsoft365 Copilot searching the web._

### What Copilot did well:
- Correctly listed the websites for each company.
- Did a great job summarising the top 3 services for each company.
- Did a decent job of retrieving addresses.

Whilst my initial tries with Copilot were relatively successful, further testing revealed that Copilot was still lacking in quite a few areas.

### What went wrong:
- **Refusal to search the web:** despite using the exact same query, Copilot started to tell me that it was unable to search web, even though it had correctly done it earlier and is officially stated as a Copilot capability ([source](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals)).

![Microsoft365 Copilot refusing to search the web](/blog/researchWeb/copilot2.png)
_Figure 2: Microsoft365 Copilot refusing to search the web._

- **Poor use of tools:** asking Copilot to turn the data into a downloadable CSV led to inconsistent results. Sometimes, Copilot would simply output a comma-separated list without creating the file. At times it even claimed it had output a CSV file, despite not even putting the data into a comma-separated format. 

- **Linking to references:** despite correctly identifying the websites of each company in the CSV, the links in the chat all lead to the same website. 

- **Hallucinations:** - When it came to retrieving search data, hallucinations were fairly minimal apart from a few errors with the company addresses. The real hallucination issues came from Copilot incorrectly thinking it had created a CSV, even going as far as to tell the user to “hold on for a moment” while it prepares the file, despite this being an impossibility with current LLM architecture.


## GPT Search
GPT Search is the newest AI Search competitor coming from OpenAI. What's interesting about GPT search is it integrates directly into ChatGPT. Whilst GPT Search does not have all the tooling functionality available in ChatGPT, you can toggle it off after searching to continue your conversation with ChatGPT as normal.

![GPT Search from OpenAI](/blog/researchWeb/gptSearch1.png)
_Figure 3: GPT Search from OpenAI._

### What GPT Search did well:
- Correctly listed the websites.
- The overview was fairly accurate.
- Able to create CSVs easily by toggling off Search mode.

Unfortunately that is where the positives for GPT Search ended and the hallucinations began.

### What went wrong:
- **Hallucinations:** whilst the services listed by GPT are largely accurate, the addresses were completely fabricated. This was also true for founding dates and demonstrates a fundamental weakness where GPT Search struggles to say it could not find the information.
![GPT Search from OpenAI](/blog/researchWeb/gpt2.png)
_Figure 4: GPT Search hallucinating addresses._
- **Information Relevance:** whilst all companies listed did use AI in some form or another, many of the companies in the list were not AI companies and did not line up well with what a user would find in a normal google search. It is very unlikely that a user searching for ‘ai companies perth’ would be looking for both space exploration companies and personal health coaching, highlighting that GPT Search still has a long way to go when it comes to understanding user intent. 
- **Redundancy in sources:** an examination of the sources used by GPT explains a lot about where these poor results are coming from. Despite being asked to perform research for each company, we can see the results are overwhelmingly made up by sources from Icetana. 
![Irrelevant search results](/blog/researchWeb/gpt4.png)
_Figure 5: References are dominated by a single company._


## Perplexity AI
Perplexity was an interesting case as it seemed to be less likely to hallucinate compared to Copilot and GPT Search and much more likely to say that the information was not avaliable. When it comes to getting exact results you can trust, this may indicate a step in the right direction for Perplexity, though this did come at the cost of missing some information we would expect it to retrieve correctly.
![Searching the web with Perplexity AI](/blog/researchWeb/perplexity1.png)
_Figure 6: Searching the web with Perplexity AI._

### What Perplexity did well:
- **Reduced Hallucinations:** Perplexity tended to avoid giving specific answers when it was unsure, even going as far as to put the addresses as just “Perth, Western Australia”. This was a task that Copilot and GPT Search really struggled with as many websites won’t list their address at all so hallucinations are a real problem. If avoiding hallucinations is a priority for you, it may be worth considering Perplexity even if it may be more likely to miss things.
![Perplexity AI answering vaguely when it is unsure.](/blog/researchWeb/perplexity2.png)
_Figure 7: Perplexity AI answering vaguely when it is unsure._

Whilst Perplexity clearly hallucinated the least, it also missed the most information by far.

### What went wrong 
- **Missed websites and services:** despite the sources used by perplexity containing links to each company website, it was only able to output 2 website URLs in our final CSV. It also claimed that the services for many companies were ‘not provided’ despite this not being true.
![Perplexity AI missing website links and services.](/blog/researchWeb/perplexity3.png)
_Figure 8: Perplexity AI missing website links and services._
- **Overly vague:** as mentioned, Perplexity set all addresses to Perth, Western Australia despite many of the companies list having their address publicly available. Services listed were also vague and missed nuances of what each company specialises in.
- **Unable to create CSV file:** Perplexity was unable to directly create the CSV file, instead requiring the user to copy and paste the data. Whilst this is not a big deal it does limit Perplexity’s ability to be helpful when performing deep web research.

## Conclusion
Each tool brought something unique to the table, with distinct strengths and weaknesses:
- **Microsoft 365 Copilot:** when it worked well, Copilot was clearly the best at finding accurate references on the web. It is an ideal choice for users who need an AI tool integrated with existing Microsoft workflows and are willing to tolerate occasional inconsistencies in functionality.
- **GPT Search:** GPT Search presents an innovative user interface that integrates directly in ChatGPT. It is ideal for users who want to take advantage of ChatGPT's existing tooling, but users should verify details due to a higher risk of hallucinated data.
- **Perplexity AI:** whilst Perplexity missed the most information it was also the most cautious and reliable for avoiding hallucinations, making it ideal for those who prioritise accuracy over completeness in results.

Ultimately AI search still has a long way to go and the accuracy of responses is heavily limited by the sources provided to the LLM. For truly accurate search, more agentic workflows are needed, where AI is able to dig further into the links it finds when examining sources.