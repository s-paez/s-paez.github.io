# Personal website

Bilingual Hugo site, deployed to GitHub Pages from `main`.

## Publishable content

Only put material intended to be public in `content/`, `static/` and `assets/`.
The home page contains the introduction; background, projects, publications and
blog posts each have their own section. The homepage background and white text
are intentional. One source portrait, `assets/media/avatar.jpg`, is mounted into
the author bundles for both languages.

Private personal posts are archived locally under `.private/`, which is ignored
by Git and is not mounted by Hugo. It is not part of a fresh clone; keep a separate
backup. Do not use hidden names, `private: true`, menus, or sitemap exclusions as
privacy controls. Drafts are for future public content, not confidential storage.

Removing a file from new commits does not remove it from Git history or an
existing deployment. The old public site is replaced only after deployment.
If sensitive content was already pushed, Git history, forks and cached copies
need separate attention before treating it as private.

## Build and verify

Use Hugo **0.136.5 Extended**, Go **1.23.12**, and Node **22**.

```sh
npm ci
hugo --minify --cleanDestinationDir
npm run search
npm run verify
```

The verification checks public sources and the entire artifact, including feeds
and search assets, for excluded personal posts and template material. It also
checks internal page/resource links and the removal of Analytics. The deploy
workflow runs verification before uploading the Pages artifact.

To preview locally:

```sh
hugo server --disableFastRender
```

Dependencies are pinned in `go.mod`, `go.sum`, `package.json` and
`package-lock.json`. Update these intentionally and rebuild both languages.
