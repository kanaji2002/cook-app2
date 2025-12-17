#!/usr/bin/env python
"""
SQLiteデータベースの現在の設定を確認するスクリプト
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photoproject.settings')
django.setup()

from django.db import connection

# データベース接続を確立（最適化設定が適用される）
connection.ensure_connection()

with connection.cursor() as cursor:
    # 現在の設定を確認
    settings_to_check = [
        ('cache_size', 'メモリキャッシュサイズ（負の値はKB単位）'),
        ('page_size', 'ページサイズ（バイト単位）'),
        ('journal_mode', 'ジャーナルモード（WAL推奨）'),
        ('synchronous', '同期モード（NORMAL推奨）'),
        ('busy_timeout', 'ロックタイムアウト（ミリ秒）'),
        ('temp_store', '一時データの保存場所'),
        ('mmap_size', 'メモリマッピングサイズ（バイト単位）'),
    ]
    
    print("=" * 70)
    print("SQLite データベース設定の現在値")
    print("=" * 70)
    
    for setting, description in settings_to_check:
        try:
            cursor.execute(f"PRAGMA {setting};")
            result = cursor.fetchone()
            value = result[0] if result else 'N/A'
            
            # 値を読みやすくフォーマット
            if setting == 'cache_size' and isinstance(value, int) and value < 0:
                value_str = f"{abs(value)} KB ({value})"
            elif setting == 'mmap_size' and isinstance(value, int):
                mb = value / (1024 * 1024)
                value_str = f"{mb:.0f} MB ({value:,} bytes)"
            elif setting == 'busy_timeout' and isinstance(value, int):
                value_str = f"{value} ms ({value/1000:.1f} seconds)"
            else:
                value_str = str(value)
            
            print(f"{setting:20s}: {value_str:30s} # {description}")
        except Exception as e:
            print(f"{setting:20s}: エラー - {e}")
    
    print("=" * 70)
    print("\n最適化設定の説明:")
    print("- cache_size: メモリ内のページキャッシュサイズ。大きいほど高速だがメモリを消費")
    print("- page_size: データベースページサイズ。4KBが一般的に最適")
    print("- journal_mode: WALモードは読み書きの並行性を向上させる")
    print("- synchronous: NORMALは安全性とパフォーマンスのバランスが良い")
    print("- busy_timeout: データベースがロックされている場合の待機時間")
    print("- temp_store: MEMORYは一時データをメモリに保存して高速化")
    print("- mmap_size: メモリマッピングを使用してI/Oを高速化")

