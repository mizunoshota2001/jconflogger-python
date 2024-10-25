# `jconflogger-python` のインストールガイド

## 前提条件

- **Python**: Python 3.11 で動作確認済み。
- **pip**: Python パッケージマネージャーである `pip` がインストールされている必要があります。

## インストール手順

### 1. GitHub から直接インストール

`jconflogger-python` パッケージは GitHub リポジトリから直接インストールすることができます。以下のコマンドを使用してください。

```bash
pip install git+https://github.com/mizunoshota2001/jconflogger-python.git
```

## 使い方

### 基本的な例

```python
from jconflogger import getLogger

logger = getLogger('my_logger')

logger.info('これは情報メッセージです')
logger.error('これはエラーメッセージです')
```

- サンプルは[こちら](/sample_usage.py)を参照してください。
