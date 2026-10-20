# PAX PITS：アプリ内AI会話への修正・公開

2026年10月21日

## 公開結果

- PAX PITS APP v53: https://pax-pits-app.tad-world.chatgpt.site/ — succeeded
- UNIVERSE v19 AI画面: https://pax-pits-universe.tad-world.chatgpt.site/#ai — succeeded
- APP正本commit: c7e450c56d595426d6e2292bd7fb24d15fa849ee
- UNIVERSE正本commit: 3fbedb639340bcd918e0cce605a8fbb93b54b1da
- APP deployment: appgdep_6ad7f2a6b7f48191bfd29f069b991130
- UNIVERSE deployment: appgdep_6ad7f2767eb081919185db67dda9b15c

以前の「ChatGPTを開いて返事を保存する」方式をAI画面の主導線から外し、端末内で生成→同画面へストリーミング→本人専用履歴へ保存する形に修正しました。生成の停止、失敗表示、再試行、保存だけの再試行、履歴削除を実装。第三者の返信先への書込みと、削除済みメッセージへの遅延保存を拒否します。MCP機能は既存互換用に保持し、アプリ内AIの利用にChatGPTでの会話操作は不要です。

## 無料運用と制約

- 有料推論API、新規キー、新規契約を使いません。推論は利用者の端末で行います。
- 標準：Qwen3-1.7B、初回約1.5GB。WebGPUとshader-f16対応が必要。
- 軽量：Qwen3-0.6B、初回約610〜650MB。対応GPU、またはWebAssembly CPUで実行。
- Wi-Fiと空き容量が必要。通信料金は利用者の契約によります。端末によりメモリ不足・非対応・低速で動作できない場合があります。
- 軽量モデルの日本語や会話の品質、キャラの一貫性には限界があります。ChatGPT相当の品質や専門判断の正確性を保証しません。
- モデル配信元へ会話本文を送らず、モデルファイルをダウンロードします。本人の会話履歴は既存の認証済みSite APIに保存します。
- モデルはHugging Face、WASM実行ファイルはjsDelivrから取得。版とモデルrevisionを固定。JavaScript配布物は正本のweb/vendorに同梱し、ライセンスとSHA-256を記録。

## 検証

- UNIVERSEの自動テスト36件成功。
- APPの自動テスト11件成功。計47件。
- 別実行で、Qwen3-1.7Bの実モデルをCPU q8で動かし、日本語の返信を生成。
- Qwen3-0.6BをWebAssembly実行プロバイダーで実際に動かし、日本語の返信を生成。
- モデル生成をスタブ化したテストだけで動作を完了扱いしていません。ただし、ブラウザ画面とWebGPUの実機確認は未完了です。CPUでの標準モデル確認は、WebGPU q4f16での確認を代替しません。
- wasm配信URLのHTTP 200・JavaScript MIME・CORS許可を確認。

実機スマートフォンのPWA・モデル初回取得・ブラウザGPU・本番の複数ユーザーでの会話確認は未確認のままです。アプリ全体の一般募集拡大条件を満たしたとは扱いません。

in-app-ai.patchはUNIVERSE v18からv19へのアプリコード差分です。vendorとpackage-lockは差分ファイルから除外しています。完全な変更状態は上記Sites正本commitにあります。旧Pits記憶リポジトリのmainや既存資産は変更していません。
