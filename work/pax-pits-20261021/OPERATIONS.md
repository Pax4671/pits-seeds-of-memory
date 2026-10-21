# PAX PITS / UNIVERSE — 2026-10-21

## Architecture and source

- PAX PITS APP: existing Sites project `appgprj_6a7b15df32d0819182d0d356b2b42728`; nurturing/play state in its own D1 and local device storage.
- PAX PITS UNIVERSE: existing Sites project `appgprj_6ac53b4e971c8191aaf530e9dbceac92`; social messages, approvals and Pits AI conversation in its own D1; imported avatar raster files in existing R2.
- Identity comes only from Sites dispatch's authenticated headers. Site-scoped IDs differ; no automatic user-data sharing across apps.
- Existing GitHub `Pax4671/pits-seeds-of-memory` is a historical Pits memory project, not either live app's source. Sites repositories are the deployment source of truth. A GitHub review branch carries the exact changes and verification notes without changing the historical files.

## Owner operation

1. Open `/#me`, sign in and save your 18+ profile. Verified owner email in secret `PITS_OWNER_EMAIL` grants owner operations. Existing `ADMIN_EMAIL` is preserved.
2. Open `/#admin`. Approve named test participants only. Reports and audit entries older than 180 days are lazily purged on the next throttled write operation. Every suspension, restoration and admission needs a written reason and creates an audit entry.
3. Users may create rooms; invite recipients request membership; only the host can approve. Cap is 20 active people including host, 40 active + pending requests. Invite tokens expire after 7 days; only hashes are stored.
4. Users report/block in a direct chat or group. Suspending stops sending, member lookup and group access. A suspended user can still export/delete their own account and appeal via `/#account`.
5. Closed groups are not listed; recent 100 messages are shown. Existing older history remains stored until deletion; full-history pagination is not implemented.

## Pits AI without an API bill

`/#ai` stores the caller's message. The owner’s Site-created PAX PITS plugin supplies `open_pax_pits` and `reply_pax_pits` to ChatGPT. ChatGPT generates the actual reply and writes it back to the same authenticated user. No timer, background agent or canned reply is represented as an AI reply. No external API is called. A pending message does not receive an automatic in-site response just by opening the app. Personal plugin distribution to other users is unverified. Existing Pits Capsule is linked as a separate AI companion; it does not share history.

Per-user limits: 20 AI submissions/day, 5 unanswered submissions, 30 saved replies/day. Existing image API endpoint now rejects before any provider request, even if a key exists. Existing secret keys are not changed.

## Backups and recovery

`/#admin` offers password-encrypted download (AES-256-GCM; PBKDF2-SHA256 310,000 iterations). Use a unique passphrase of 12+ characters. Owner chooses and keeps it; the application does not store it. D1 tables are read in one batch. R2 assets are fetched separately, so this is not an atomic D1/R2 snapshot. Stop participant writes before an operational snapshot. Export refuses any table above 5,000 rows or avatars totaling over 10 MB; it never labels a truncated file complete.

Offline verification from the UNIVERSE repository:

```
node scripts/restore-isolated.mjs pits-encrypted-backup.json /private/new-isolated-restore
```

Supply the passphrase on stdin using a secure interactive input method. Never put it in command arguments or commit a backup. The program refuses existing output paths, applies the committed migrations to a brand-new SQLite file, restores records and avatar files, and prints counts only. It has no network code or production restore route. A real production recovery requires owner authorization and platform-supported database/storage import access. Keep snapshots encrypted, restrict local filesystem access, and remove copies after 30 days. Deletion of an account cannot recall files previously downloaded by an owner or recipient.

Own-data export is separate, includes only one's own outgoing messages and AI history. Profile import restores editable display fields through the same authenticated profile endpoint; it cannot restore approval, suspension, messages or group membership. APP-side export/delete covers the nurturing cloud record and named local-storage keys. Existing billing-subscription references block automated deletion pending a billing check, to avoid deleting the information needed to stop recurring charges.

## Cost controls and limits

No paid AI API usage, new Cloudflare account, payment contract, app-store submission or paid upgrade was created. No Durable Object namespace is provisioned: text chat uses visible-tab polling every 15 seconds. Images: 5 MB/upload, 20 uploads/day globally, 200 stored images limit. Test admission stops at 200 member records. Content POST operations have a global 2,000/day guard plus existing per-user limits. These application guards do not cap anonymous request traffic, provider-account billing, read amplification, backups or operations shared with other Sites.

Cloudflare direct-account published free tiers, checked 2026-10-21:

| Product | Free allowance | Notes |
| --- | --- | --- |
| Workers | 100,000 requests/day, 10 ms CPU/invocation | Existing Sites is managed hosting; direct-account allowance is not a confirmed Sites entitlement. |
| D1 | 5 million rows read/day; 100,000 written/day; 5 GB total | Indexed scans and index writes also count; account-wide totals matter. |
| R2 Standard | 10 GB-month; 1 million class A and 10 million class B/month | Overages can be billable on the underlying account; no hard spending cap is confirmed for Sites. |
| Durable Objects SQLite | 100,000 requests/day; 13,000 GB-s/day | Available Free; not used in this implementation. |

Sources: https://developers.cloudflare.com/workers/platform/pricing/ ; https://developers.cloudflare.com/d1/platform/pricing/ ; https://developers.cloudflare.com/r2/pricing/ ; https://developers.cloudflare.com/durable-objects/platform/pricing/

The connected Sites surface does not expose the underlying billing plan, a hard currency cap, or full production D1/R2 restore controls. Zero future hosting cost is therefore **not verified**. If direct Workers Paid is selected later, its base subscription and metered overages need separate explicit approval. No such selection was made.

## Release gate: limited testing, no recruitment expansion

Automated tests exercise simulated trusted Sites identities on real isolated SQLite with the complete migrations and actual built handlers. They do not prove that physical iPhones/Android devices work or that the production identity edge rejects forged headers. No supported browser-control skill was available in this environment; no browser QA or device installation was performed.

Before general recruitment: two genuine participant identities must test sign-in, admission, unreadable third-party conversations, report/block, host approval/revocation, suspension, deletion, AI plugin connection and actual response return, iPhone Safari + Android Chrome PWA installation. Owner should create an actual encrypted production snapshot and verify a recovery copy. Full live recovery has not been done. E2EE is not implemented. Operating response staffing and legal review are not complete.

18+ is self-attestation, not verified proof of age. This is a hobby/creation discussion service; it does not offer romantic matching. NPA describes the regulated internet opposite-sex introduction business using four cumulative requirements, so actual operation and public messaging must be reviewed before any dating-oriented extension. Self-attestation alone must not be represented as compliance with a regulated age-verification regime.

PPC says overseas processing obligations depend on the service/provider arrangement and safeguards. Exact processing countries, processor/subprocessor terms and any necessary transfer consent remain to be confirmed with Sites; generic policy text is not proof of legal compliance. Public policy and support/appeal entry points were added, but the limited-test release is not certified worldwide legal compliance.

Primary references: https://www.npa.go.jp/policy_area/no_cp/deai/regulatory.html ; https://www.ppc.go.jp/all_faq_index/faq1-q10-24/
