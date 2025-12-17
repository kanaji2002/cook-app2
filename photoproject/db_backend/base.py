"""
SQLite最適化設定を適用するカスタムデータベースバックエンド
"""
from django.db.backends.sqlite3.base import DatabaseWrapper as SQLiteDatabaseWrapper


class DatabaseWrapper(SQLiteDatabaseWrapper):
    """
    SQLiteデータベース接続時に最適化設定を自動適用する
    """
    def get_new_connection(self, conn_params):
        conn = super().get_new_connection(conn_params)
        
        # SQLite最適化設定を適用
        cursor = conn.cursor()
        try:
            # キャッシュサイズ: 10MB（負の値はKB単位）
            cursor.execute("PRAGMA cache_size = -10000;")
            
            # ページサイズ: 4KB（推奨値、既に設定されている場合は変更されない）
            cursor.execute("PRAGMA page_size = 4096;")
            
            # WALモード: Write-Ahead Logging（並行性向上）
            cursor.execute("PRAGMA journal_mode = WAL;")
            
            # 同期モード: NORMAL（バランス良い）
            cursor.execute("PRAGMA synchronous = NORMAL;")
            
            # ロックタイムアウト: 5秒
            cursor.execute("PRAGMA busy_timeout = 5000;")
            
            # 一時データをメモリに保存
            cursor.execute("PRAGMA temp_store = MEMORY;")
            
            # メモリマッピング: 256MB
            cursor.execute("PRAGMA mmap_size = 268435456;")
            
            # 統計情報を有効化（クエリプランナーの精度向上）
            cursor.execute("PRAGMA optimize;")
        finally:
            cursor.close()
        
        return conn

