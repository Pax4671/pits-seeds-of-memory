# PAX PITS 承認制テスト版 公開記録 — 2026-10-21

本体v52とUNIVERSE v18の本番公開が成功。全機能の一般公開受入完了ではありません。

| 項目 | 記録 |
| --- | --- |
| APP | https://pax-pits-app.tad-world.chatgpt.site/ |
| UNIVERSE | https://pax-pits-universe.tad-world.chatgpt.site/ |
| 管理画面 | https://pax-pits-universe.tad-world.chatgpt.site/#admin |
| Pits AI | https://pax-pits-universe.tad-world.chatgpt.site/#ai |
| 本体正本commit | c1a83503c9abd7e45357336e586270181e04a7d4 |
| UNIVERSE正本commit | a0caba0541dbccbc62871a5981e34dc4a51b00cb |
| 本体deployment | appgdep_6ad7ea8f07e081918627582963d9ae67 / succeeded |
| UNIVERSEdeployment | appgdep_6ad7ea1c82c48191acec0200bce0023f / succeeded |
| テスト | UNIVERSE31件、本体11件、計42件成功 |
| 本番DB | 既存10テーブルを残し、ai_messages / audit_log追加確認 |

このGitHub PRは既存の歴史的Pits資産を変更せず、Sites正本に適用した差分と運営手順を保存するものです。このリポジトリが本番デプロイ元になったという意味ではありません。app.patch / universe.patchは各正本の元コミットからの差分です。

実装：承認制参加、既存の1対1・最大20人チャットの保護、主催者の参加承認、通報・ブロック・退出、管理者承認・停止・復旧と理由記録、相談・異議申立て、自己データ保存・削除、暗号化バックアップと隔離復元ツール、Pits AIの個別履歴とChatGPT MCP連携、PWA構成、ACADEMYへの直接導線。

AIは有料APIを使わず、ChatGPTが返事を生成して本人の履歴へ戻す方式です。サイト単独では自動返信しません。新プラグインはSitesから発行され、プラグイン管理はインストール済みと応答しましたが、この会話に新しいツールはまだ露出していません。実接続と返信往復は未検証です。

未完了：スマートフォン実機・PWAインストール、複数の本物のアカウントでの本番受入、プラグインの一般利用者への配布と返信往復、本番バックアップの取得・実データの復元、処理国・委託契約・年齢確認等の法務確認、Sitesの基盤課金上限の確認。自己申告18+を本人確認済みとは表示しません。一般募集拡大は保留。

秘密鍵の変更、既存サイト削除、DB初期化、新規課金契約、有料API利用は実施していません。既存ADMIN_EMAILを保持し、検証済みOWNERメールを別名の秘密環境変数として追加しました。

無料枠の数値・上限・復元手順・運営方法はOPERATIONS.md参照。Cloudflare直接契約の無料枠は、Sitesで同じ枠が保証される証拠ではありません。将来の完全無料運営や世界各国の法令遵守を完了扱いしません。
