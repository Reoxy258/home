import os
import re
from typing import Any, Dict, List

try:
    import yaml
except ImportError:
    yaml = None


def define_env(env) -> None:
    """
    MkDocs Macros entry point.

    当前只提供一个宏：
    - collect_notifications()：收集 Notification/ 目录下所有页面的 cards，
      返回一个扁平的 cards 列表，供通知中心统一展示。

    具体的卡片样式与按 ddl 倒序排序逻辑由 Jinja 模板
    docs/macros/card_macro.html 中的 render_cards 宏负责。
    """

    @env.macro
    def collect_notifications() -> List[Dict[str, Any]]:
        """
        收集所有通知卡片。从 docs/Notification/ 下各 .md 文件的 YAML front matter 中读取 cards，
        合并为扁平列表。卡片格式需包含 title, detail, href，可选 ddl、tags。
        """
        all_cards: List[Dict[str, Any]] = []

        if yaml is None:
            return all_cards

        conf = getattr(env, "conf", None) or {}
        config_file = conf.get("config_file_path")
        if config_file:
            project_dir = os.path.dirname(os.path.abspath(config_file))
        else:
            project_dir = os.getcwd()
        docs_dir = conf.get("docs_dir", "docs")
        docs_path = os.path.join(project_dir, docs_dir)
        notification_dir = os.path.join(docs_path, "Notification")

        if not os.path.isdir(notification_dir):
            return all_cards

        for root, _dirs, files in os.walk(notification_dir):
            for name in files:
                if not name.lower().endswith(".md"):
                    continue
                path = os.path.join(root, name)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        raw = f.read()
                except OSError:
                    continue

                # 解析 YAML front matter（--- ... ---）
                fm_match = re.match(r"^---\s*\n(.*?)\n---", raw, re.DOTALL)
                if not fm_match:
                    continue

                try:
                    meta = yaml.safe_load(fm_match.group(1))
                    if meta and isinstance(meta.get("cards"), list):
                        for card in meta["cards"]:
                            if isinstance(card, dict) and _valid_card(card):
                                all_cards.append(card)
                except Exception:
                    pass

        return all_cards


def _valid_card(c: Dict[str, Any]) -> bool:
    """卡片至少需要 title, detail, href（与 card_macro 一致）。"""
    return (
        isinstance(c.get("title"), str)
        and isinstance(c.get("detail"), str)
        and isinstance(c.get("href"), str)
    )

