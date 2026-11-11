# 青学 · HSK 4A study companion

A static, browser-only study website based on the supplied **New HSK Course 4A**. The ready-to-publish website is at the repository root. No npm install, build service, API key, account or database is needed.

## Publish on GitHub Pages

1. Use the current website files in this project’s root folder.
2. Put those files in the root of your GitHub repository. `index.html`, `app.js`, `data.js`, `styles.css`, `.nojekyll` and `assets/` should be at that root, not inside another `site` folder.
3. In the repository, open **Settings → Pages**. Choose **Deploy from a branch**, select your branch (usually `main`), select **/(root)**, then **Save**.
4. Open the address shown by GitHub Pages once deployment finishes.

All asset URLs are relative; chapter links use hashes, so repository subpaths and refreshed chapter links work without server rewrites.

See [GitHub's publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Preview on your computer

From this project folder:

```bash
python3 -m http.server 8874 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8874/`. Stop the server with Ctrl+C. An HTTP preview is preferable to opening the HTML file directly because browser storage behaviour for `file:` URLs varies.

## Included

- Home dashboard, ten-chapter Book library, Saved Words and Practice.
- 391 vocabulary entries, each with pinyin, meaning, a chapter-grammar example and an editable personal sentence.
- 58 original warm-up pictures. Chapter 5 has four dishes with separate flavour matches, as in the book; the other chapters have six pictures.
- 20 original discussion questions with three model answers each.
- 40 original texts with study translations, comprehension questions and retelling notes.
- 40 grammar explanations, 80 illustrative grammar sentences and 120 original grammar practice prompts.
- 80 original listening-choice questions usable with the book recordings or as reading questions; 100 vocabulary gaps; ten cloze passages; 30 picture-writing prompts.
- Speaking and writing tasks, model responses, a 120-character writing counter, and reflection checklists.
- Hover, focus or tap vocabulary details and save words for review. Saved words also appear at the top of a chapter.
- Independent pinyin, English and answer controls. Pinyin and English, including model answers, start hidden. Use each section’s Show controls to reveal them.
- Original chapter-page images for reference.

The 40 supplied MP3 recordings in `assets/audio/` are available in Listen / read & choose, with play/pause and replay controls for each text. Starting another recording pauses the previous one. Companion videos are not included. Video topics are included with a notes field. Objective exercises have a correct answer or model completion; open discussion questions have three alternatives. Generated responses are study examples, not the publisher's answer key.

## Saving and backups

Sentences, matching choices, section completion, saved words, display preferences and review results are stored in `localStorage` under `qingxue-hsk4a-v1`. There is no server sync. The Home page has **Export progress** and **Import progress**. Import merges the backup into current progress; matching note keys from the backup replace those notes.

Storage belongs to the browser profile and website origin. Local preview, GitHub Pages, another device and a custom domain have separate storage. Export before moving and import at the new address. Clearing browser data removes the local copy. The site reports a storage error if a write fails.

## Editing the course

- `app.js`: navigation, rendering and storage.
- `styles.css`: responsive design.
- `data.js`: complete deployable course data.
- `source/*.tsv`: editable Chinese/English authoring files.
- `source/page-*.json` and `.txt`: OCR working records; original scans remain the reference.
- `tools/build_*.py`: authoring scripts; not required for hosting.
- `tools/validate_site.py`: structural and asset checks.
- `tools/audit_vocabulary.py`: vocabulary screening of the 391 target examples, 60 discussion responses and 58 warm-up sentences against local Level 1–3 lists and earlier chapters. The target and current grammar are allowed in a target example. This segmentation check is a review aid, not a guarantee of linguistic difficulty or contextual pronunciation.

Run `python3 tools/validate_site.py` and `node --check app.js` after changes. The prepared site can be deployed directly without regenerating OCR or illustrations.

Audio mapping: Texts 1–4 use Lesson `CC-01`, `CC-03`, `CC-05` and `CC-07` respectively, with a two-digit chapter number. Publish the entire `assets/audio/` folder alongside the root website. Older ZIP exports do not contain this audio update; use the root files for deployment.
