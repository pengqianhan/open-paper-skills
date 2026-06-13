"""
从笔记文件的 YAML frontmatter 中提取字段，追加条目到 paper_memory.md。

用法:
    python append_to_memory.py <笔记文件路径>

示例:
    python append_to_memory.py notes/20260314T220000-paper-nca-language-model-pretraining.md
"""

import re
import sys
from pathlib import Path

# 不出现在 paper_memory 条目列表中的字段（title 用作标题，其余无需展示）
SKIP_FIELDS = { "tags","title","date"}


def find_template(script_path: Path) -> Path:
    """定位 template.md（与本脚本同级的 ../references/template.md）。"""
    return script_path.parent.parent / "references" / "template.md"


def parse_yaml_frontmatter(text: str) -> dict:
    """解析 YAML frontmatter（--- 包裹的部分），返回有序字段字典。"""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError("未找到 YAML frontmatter")
    fields = {}
    for line in m.group(1).splitlines():
        match = re.match(r'^(\w+)\s*:\s*"?(.*?)"?\s*$', line)
        if match:
            key, value = match.group(1), match.group(2)
            value = value.strip('"')
            fields[key] = value
    return fields


def get_template_field_order(template_path: Path) -> list[str]:
    """从 template.md 的 YAML 中提取字段名顺序。"""
    text = template_path.read_text(encoding="utf-8")
    fields = parse_yaml_frontmatter(text)
    return list(fields.keys())


def build_entry(fields: dict, note_filename: str, template_path: Path) -> str:
    """根据 template 字段顺序和笔记 YAML 值生成 paper_memory 条目。"""
    title = fields.get("title", "")
    display_title = re.sub(r"^paper-", "", title)

    # 从 template 读取字段顺序
    field_order = get_template_field_order(template_path)

    # 构建条目
    lines = [f"\n---\n\n## [{display_title}](../notes/{note_filename})\n"]
    for key in field_order:
        if key in SKIP_FIELDS:
            continue
        value = fields.get(key, "")
        if key == "source":
            lines.append(f"- **{key}**: [{value}]({value})")
        else:
            lines.append(f"- **{key}**: {value}")
    lines.append("")  # 末尾空行

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(f"用法: python {sys.argv[0]} <笔记文件路径>")
        sys.exit(1)

    note_path = Path(sys.argv[1])
    if not note_path.exists():
        print(f"错误: 文件不存在 — {note_path}")
        sys.exit(1)

    # 定位 repo 根目录（从笔记文件往上找 know/ 目录）
    repo_root = note_path.resolve().parent
    while repo_root != repo_root.parent:
        if (repo_root / "know" / "paper_memory.md").exists() or (repo_root / "notes").is_dir():
            break
        repo_root = repo_root.parent
    else:
        print("错误: 未找到 repo 根目录（需要 know/ 或 notes/ 目录）")
        sys.exit(1)

    memory_path = repo_root / "know" / "paper_memory.md"

    # 定位 template.md
    script_path = Path(__file__).resolve()
    template_path = find_template(script_path)
    if not template_path.exists():
        print(f"错误: 未找到模板 — {template_path}")
        sys.exit(1)

    # 解析笔记 YAML（字段顺序与 template.md 保持一致，例如 description/topics）
    text = note_path.read_text(encoding="utf-8")
    fields = parse_yaml_frontmatter(text)

    # 生成条目
    entry = build_entry(fields, note_path.name, template_path)

    # 如果 paper_memory.md 不存在或为空，先写文件头
    if not memory_path.exists() or memory_path.stat().st_size == 0:
        memory_path.parent.mkdir(parents=True, exist_ok=True)
        memory_path.write_text("# Paper Memory\n\n论文阅读注册表。每篇条目标题链接→笔记全文，source 链接→原始论文。\n", encoding="utf-8")

    # 追加条目
    with memory_path.open("a", encoding="utf-8") as f:
        f.write(entry)

    print(f"✓ 已追加到 {memory_path.relative_to(repo_root)}")
    print(f"  标题: {fields.get('title', '?')}")


if __name__ == "__main__":
    main()
