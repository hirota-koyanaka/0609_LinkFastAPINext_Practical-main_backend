# LinkFastAPINext_Practical-main の「create機能」プロセスフロー図

## 🎯 全体プロセスフロー

```mermaid
flowchart TD
    A[ユーザーが顧客作成フォームを開く] --> B[フォームに情報を入力]
    B --> C[作成ボタンをクリック]
    C --> D[フロントエンド: データ収集・検証]
    D --> E[フロントエンド: JSONデータに変換]
    E --> F[フロントエンド: POSTリクエスト送信]
    F --> G[バックエンド: FastAPIエンドポイント受信]
    G --> H[バックエンド: データ検証]
    H --> I{検証OK?}
    I -->|No| J[エラーレスポンス]
    I -->|Yes| K[データベース接続]
    K --> L[データベース: 新規レコード挿入]
    L --> M{挿入成功?}
    M -->|No| N[エラーレスポンス]
    M -->|Yes| O[データベース: 挿入データ取得]
    O --> P[バックエンド: JSONレスポンス作成]
    P --> Q[フロントエンド: レスポンス受信]
    Q --> R[フロントエンド: 確認画面表示]
    R --> S[ユーザー: 作成完了確認]
    
    style A fill:#e1f5fe
    style S fill:#c8e6c9
    style J fill:#ffcdd2
    style N fill:#ffcdd2
```

## 📋 詳細プロセスフロー

### 🔄 フロントエンド処理フロー

```mermaid
flowchart TD
    A[page.jsx: フォーム表示] --> B[ユーザー入力]
    B --> C[handleSubmit関数実行]
    C --> D[FormDataでデータ収集]
    D --> E{customer_id空チェック}
    E -->|空| F[アラート表示]
    E -->|OK| G[createCustomer関数呼び出し]
    G --> H[createCustomer.js: データ変換]
    H --> I[JSON形式に変換]
    I --> J[fetch APIでPOST送信]
    J --> K[レスポンス受信]
    K --> L{成功?}
    L -->|No| M[エラー処理]
    L -->|Yes| N[確認画面へ遷移]
    
    style A fill:#e3f2fd
    style N fill:#c8e6c9
    style F fill:#ffcdd2
    style M fill:#ffcdd2
```

### 🖥️ バックエンド処理フロー

```mermaid
flowchart TD
    A[app.py: POST /customers受信] --> B[Customerモデルでデータ検証]
    B --> C{customer_id検証}
    C -->|NG| D[HTTPException 400]
    C -->|OK| E[crud.myinsert関数呼び出し]
    E --> F[crud.py: データベース接続]
    F --> G[Session作成]
    G --> H[INSERT文実行]
    H --> I{挿入成功?}
    I -->|No| J[IntegrityError処理]
    I -->|Yes| K[crud.myselect関数呼び出し]
    K --> L[SELECT文で挿入データ取得]
    L --> M[JSON形式に変換]
    M --> N[フロントエンドにレスポンス送信]
    
    style A fill:#e8f5e8
    style N fill:#c8e6c9
    style D fill:#ffcdd2
    style J fill:#ffcdd2
```

### 🗄️ データベース処理フロー

```mermaid
flowchart TD
    A[connect_MySQL.py: 接続設定] --> B[MySQLデータベース接続]
    B --> C[engine作成]
    C --> D[crud.py: myinsert関数]
    D --> E[Session作成]
    E --> F[INSERT文構築]
    F --> G[トランザクション開始]
    G --> H[execute実行]
    H --> I{成功?}
    I -->|No| J[rollback]
    I -->|Yes| K[commit]
    K --> L[myselect関数呼び出し]
    L --> M[SELECT文実行]
    M --> N[結果をJSON変換]
    N --> O[セッション終了]
    
    style A fill:#fff3e0
    style O fill:#c8e6c9
    style J fill:#ffcdd2
```

## 📊 データ変換フロー

```mermaid
flowchart LR
    A[フォーム入力] --> B[FormData]
    B --> C[JSON文字列]
    C --> D[HTTPリクエスト]
    D --> E[FastAPI受信]
    E --> F[Pydanticモデル]
    F --> G[辞書形式]
    G --> H[SQLAlchemy]
    H --> I[MySQLテーブル]
    I --> J[SELECT結果]
    J --> K[JSONレスポンス]
    K --> L[フロントエンド表示]
    
    style A fill:#e1f5fe
    style I fill:#fff3e0
    style L fill:#c8e6c9
```

## 🔧 ファイル別処理フロー

### 📁 フロントエンドファイル

```mermaid
flowchart TD
    A[page.jsx] --> B[フォーム表示]
    B --> C[handleSubmit]
    C --> D[createCustomer.js]
    D --> E[fetch API]
    E --> F[confirm/page.jsx]
    F --> G[完了画面表示]
    
    style A fill:#e3f2fd
    style G fill:#c8e6c9
```

### 📁 バックエンドファイル

```mermaid
flowchart TD
    A[app.py] --> B[エンドポイント定義]
    B --> C[データ検証]
    C --> D[crud.py]
    D --> E[データベース操作]
    E --> F[connect_MySQL.py]
    F --> G[MySQL接続]
    
    style A fill:#e8f5e8
    style G fill:#fff3e0
```

## ⚠️ エラーハンドリングフロー

```mermaid
flowchart TD
    A[エラー発生] --> B{エラーの種類}
    B -->|customer_id空| C[フロントエンド: アラート]
    B -->|バリデーションエラー| D[バックエンド: HTTP 400]
    B -->|データベースエラー| E[IntegrityError]
    B -->|ネットワークエラー| F[fetch API エラー]
    
    C --> G[フォーム再入力]
    D --> H[エラーレスポンス]
    E --> I[rollback処理]
    F --> J[エラーメッセージ表示]
    
    style A fill:#ffcdd2
    style G fill:#e1f5fe
    style H fill:#ffcdd2
    style I fill:#ffcdd2
    style J fill:#ffcdd2
```

## 🎓 プロセスフロー図の説明

### 🔄 **フロントエンド処理**
1. **フォーム表示** → ユーザーが入力できる画面を表示
2. **データ収集** → フォームの情報を集める
3. **検証** → 必須項目が入力されているかチェック
4. **送信** → バックエンドにデータを送信

### 🖥️ **バックエンド処理**
1. **受信** → フロントエンドからのリクエストを受け取る
2. **検証** → データの形式や内容をチェック
3. **保存** → データベースに情報を保存
4. **取得** → 保存したデータを取得
5. **返送** → フロントエンドに結果を返す

### 🗄️ **データベース処理**
1. **接続** → MySQLデータベースに接続
2. **挿入** → customersテーブルに新しい行を追加
3. **取得** → 挿入したデータを取得
4. **終了** → 接続を閉じる

### ⚠️ **エラー処理**
- 各段階でエラーが発生した場合の処理も含まれています
- ユーザーに適切なエラーメッセージを表示
- データベースの整合性を保つための処理

このプロセスフロー図により、create機能の全体の流れと各段階での処理内容が視覚的に理解できるようになっています。 