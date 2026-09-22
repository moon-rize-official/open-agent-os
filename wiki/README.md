# GitHub Wiki Source

This directory is the source of truth for the GitHub Wiki.

The GitHub Wiki itself is stored by GitHub in a separate repository:

`moon-rize-official/open-agent-os.wiki.git`

After enabling **Settings → Features → Wikis** and creating the first Wiki page, run:

```bash
./scripts/publish-wiki.sh
```

This keeps Wiki content reviewable in the main repository instead of editing important architecture pages only through the web UI.
