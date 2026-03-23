"""
根据论文标题搜索 Semantic Scholar，返回最佳 URL。

用法:
    python search_paper.py "Attention Is All You Need"
    python search_paper.py "ProgPrompt" --limit 3

优先使用 semanticscholar 库，未安装则 fallback 到 requests + API。
"""

import json
import sys
import urllib.parse
import urllib.request


def search_via_api(query: str, limit: int = 5):
    """直接调用 Semantic Scholar API（无需额外依赖）。"""
    encoded = urllib.parse.quote(query)
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={encoded}&limit={limit}"
        f"&fields=title,authors,year,externalIds,url"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "hpq-xray-paper/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    return data.get("data", [])


def search_via_library(query: str, limit: int = 5):
    """使用 semanticscholar 库搜索。"""
    from semanticscholar import SemanticScholar

    sch = SemanticScholar()
    return sch.search_paper(query, limit=limit)


def print_api_results(results):
    """打印 API 返回的结果。"""
    for i, paper in enumerate(results):
        ext = paper.get("externalIds", {}) or {}
        arxiv_id = ext.get("ArXiv")
        doi = ext.get("DOI")
        ss_url = paper.get("url", "")
        authors = ", ".join(a.get("name", "") for a in (paper.get("authors") or []))

        print(f"[{i+1}] {paper.get('title', '?')}")
        print(f"    authors: {authors}")
        print(f"    year: {paper.get('year', '?')}")
        print(f"    semantic_scholar: {ss_url}")
        if arxiv_id:
            print(f"    arxiv: https://arxiv.org/abs/{arxiv_id}")
        if doi:
            print(f"    doi: https://doi.org/{doi}")
        print()


def print_library_results(results):
    """打印 semanticscholar 库返回的结果。"""
    for i, paper in enumerate(results):
        ext = paper.externalIds or {}
        arxiv_id = ext.get("ArXiv")
        doi = ext.get("DOI")
        ss_url = f"https://www.semanticscholar.org/paper/{paper.paperId}"

        print(f"[{i+1}] {paper.title}")
        print(f"    authors: {', '.join(a.name for a in (paper.authors or []))}")
        print(f"    year: {paper.year}")
        print(f"    semantic_scholar: {ss_url}")
        if arxiv_id:
            print(f"    arxiv: https://arxiv.org/abs/{arxiv_id}")
        if doi:
            print(f"    doi: https://doi.org/{doi}")
        print()


def main():
    if len(sys.argv) < 2:
        print(f"用法: python {sys.argv[0]} \"论文标题\" [--limit N]")
        sys.exit(1)

    query = sys.argv[1]
    limit = 5
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    # 优先用库，失败时 fallback 到 API。
    try:
        results = search_via_library(query, limit)
        if not results:
            print(f"未找到匹配: {query}")
            return
        print_library_results(results)
        return
    except ImportError:
        print("(semanticscholar 未安装，使用 API fallback)\n")
    except Exception as exc:
        print(f"(semanticscholar library search failed, using API fallback: {ascii(exc)})\n")

    results = search_via_api(query, limit)
    if not results:
        print(f"未找到匹配: {query}")
        return
    print_api_results(results)


if __name__ == "__main__":
    main()