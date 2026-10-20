# ENCY CAM ドキュメント

日本語ユーザーマニュアル、バージョン **3.1.13**。

- [目次](index.md)
- [HTML ドキュメント](https://docs.encycam.com/ENCY/3/ja/index.html)
- [PDF マニュアル](https://docs.encycam.com/ENCY/pdf/ENCY3manual-ja.pdf)
- [Markdown インデックス](llms.txt)
- [バージョンと言語](doc-profile.json)
- [翻訳への参加](TRANSLATING.md)

ブランチ CAM/ja/v3 には現在のドキュメントスナップショットが含まれます。

## ローカルでのビルドとプレビュー

`build.ps1` は DocFX で HTML ドキュメントを `_site` に生成し、
<http://127.0.0.1:8000/index.html> でプレビューを開始します。
ブラウザーは自動的に開きます。停止するには Ctrl+C を押してください。

DocFX が PATH にない場合、初回実行時に .NET SDK 8 以降とインターネット接続が必要です。
