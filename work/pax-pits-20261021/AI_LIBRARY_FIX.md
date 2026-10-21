# AI起動時 Unexpected token '^' の修正

2026年10月21日。UNIVERSE v20を本番公開（succeeded）。

原因：scripts/build.mjs が String.replace の文字列置換を使っていたため、埋め込んだAIライブラリ内の `$&` が import 文に置換され、公開されたJavaScriptが壊れていました。スマートフォンの通信・容量不足が原因であるという証拠はありません。

修正：3か所のソース埋込みを置換関数へ変更し、内容を文字どおり保持。公開用Workerの実レスポンス経由で全JSのハッシュ一致とES module構文を検証する回帰テストを追加。旧ビルドで2件とも失敗することを確認してから、修正後は全38件成功。

公開後、実URLからライブラリを取得し、モジュール構文検査成功と正本との完全一致を確認。

SHA-256: aa5002b70e789798da263f5f99c62bd3e8fcd0c119258a493c40c180648365fa

Sites正本commit: 0c527d00210141043542c8b3d7c37f904a17475a
Deployment: appgdep_6ad7f815b7448191b8433e06421923db
URL: https://pax-pits-universe.tad-world.chatgpt.site/#ai

この修正は構文エラーの解消です。スマホ実機のWebGPU・モデル初回取得・推論完走を確認したという意味ではありません。鍵・DB・課金設定は変更していません。
