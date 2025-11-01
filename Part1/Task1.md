**Q1: Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?**

AI code generation tools reduce development time by autocompleting, suggesting entire functions, and generating unit tests from comments—cutting repetitive coding. 
They analyze context across millions of open-source repos to predict optimal code patterns instantly.

Limitations:
    Security risks (can suggest vulnerable code).
    Hallucinations (incorrect or outdated logic).
    Over-reliance reduces deep understanding.
    IP/legal concerns (trained on public code).
    Poor handling of niche domains or strict compliance rules.

**Q2: Compare supervised and unsupervised learning in the context of automated bug detection.**

Supervised learning uses labeled data to predict whether new code will contain bugs based on features like complexity, churn, or developer activity. It excels at detecting known bug patterns with high accuracy when sufficient labeled data is available.

In contrast, unsupervised learning operates on unlabeled code or system logs, identifying anomalies through clustering or outlier detection without prior knowledge of what a bug looks like. It is ideal for discovering novel or zero-day defects—such as unexpected memory spikes or rare crash patterns—that have not been previously documented.

While supervised methods offer precision for established issues, they require extensive labeled datasets and may miss new bug types. Unsupervised approaches uncover hidden issues but often generate false positives due to lack of context. The most effective automated bug detection systems combine both: supervised learning for known vulnerabilities and unsupervised learning for emerging threats.

**Q3: Why is bias mitigation critical when using AI for user experience personalization?**

Bias in AI-driven personalization systems can lead to discriminatory outcomes, such as recommending high-paying job ads only to certain demographics or excluding underrepresented groups from relevant content. This amplifies societal stereotypes and erodes user trust.

Without mitigation, biased models create unequal user experiences—alienating segments of the audience and increasing churn. It also poses significant legal and regulatory risks under laws like GDPR, CCPA, and anti-discrimination regulations.

Furthermore, biased personalization damages brand reputation, reduces engagement, and limits market reach. Effective mitigation—through diverse training data, fairness-aware algorithms, regular bias audits, and transparent decision-making—ensures equitable, inclusive, and trustworthy user experiences across all demographics.