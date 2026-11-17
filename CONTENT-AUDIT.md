# Textbook coverage audit — 12 November 2026

Scope: compared the extracted text for all ten chapters (printed pages 1–119) with the current root data.js and app.js. Visually checked representative original pages 1, 3, 11, 28, 48, 74 and 90. This is a section/exercise coverage audit, not a line-by-line certification of transcription, translation or answer accuracy. Original page scans available through the site do not count as fully implemented learning activities.

## Confirmed omissions and incomplete implementations

| Item | Finding | Source evidence |
| --- | --- | --- |
| Chapter objectives | Missing from the main learning interface in all ten chapters. | Chapter opening pages 1, 12, 23, 35, 47, 59, 71, 83, 95, 107. |
| Role-play the dialogue | Explicit activity instructions omitted for Texts 1 and 2 (20 activities). Dialogue content itself exists. | All chapters; e.g. printed pages 2 and 5. |
| Read the text aloud | Explicit activity instructions omitted for Texts 3 and 4 (20 activities). Reading content itself exists. | All chapters; e.g. printed pages 6 and 8. |
| Xiaoyu’s Tips / 小语助力 | Margin explanations are not implemented as study content. Word dictionary definitions do not replace these explanations. | Printed pages 28, 36 (two tips), 47, 48, 52, 74, 75, 76, 84, 86, 90. |
| Learning Summary | Current interface has four grammar confidence checkboxes and notes, but omits the original chapter-specific vocabulary/communication goals and the three ratings: No problem / It’s OK / Need to improve. | All chapters; e.g. printed pages 11, 22, 33–34. |
| Grammar source examples | All 40 grammar topics and their 120 practice items exist, but the book’s original example sets are replaced by two generated examples per topic. Explanations are summaries. | Example: printed page 3 has three original 任何 examples; the site supplies two different sentences. |
| Retelling accessibility — resolved 17 November 2026 | All 20 prompts now render as selectable text with pinyin, English, dictionary word controls, and independently hidden model answers. Existing notes are preserved. | Texts 1 and 3 in every chapter. |

## Additional quality issue

Chapter 8 speaking task asks whether people should have pressure, but its generated sample answers discuss weekend leisure choices rather than addressing that debate. The task itself is present; the model responses need revision. Other model responses have not been exhaustively audited for relevance or language level.

## Present in the current course

- 391 vocabulary entries; 58 warm-up pictures; 20 paired discussion questions.
- 40 texts; 80 multiple-choice questions; 80 reading-comprehension questions.
- 40 grammar points and 120 grammar practice prompts.
- 100 vocabulary gaps; 10 cloze passages with 40 gaps; 30 picture-writing prompts.
- 10 speaking/group tasks and 10 writing tasks.
- 20 original retelling prompt exercises (Texts 1 and 3).
- 7 bonus-video topics, corresponding to chapters 4–10. Videos themselves are not supplied in the PDF and are not embedded.

No website content was modified during this audit. Existing tools/validate_site.py checks the legacy source/course.json and site/ directory, rather than the active root website; its success alone cannot establish current textbook coverage.
