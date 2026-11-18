#!/usr/bin/env python3
"""
reels-script-studio 进化助手 / Evolution helper.

用法 / Usage:
  python3 evolve.py record --type "产品种草型" --platform "Seedance" --motion "子弹时间" --lighting "逆光" --viral-lever "黄金3秒" --note "加强第2镜"
  python3 evolve.py feedback --text "第3镜摇移更快" --optimization "平滑→快速"
  python3 evolve.py feedback --text "改坏了" --optimization "深色背景" --rejected   # 标记失败优化
  python3 evolve.py rollback                                                       # 回滚最近一条已应用优化
  python3 evolve.py report
  python3 evolve.py stats

功能：将使用经验写入独立的 evolution.json（不修改核心 SKILL.md）。
"""
import argparse
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
EVOLUTION_PATH = os.path.join(HERE, "..", "evolution.json")


def load():
    with open(EVOLUTION_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save(data):
    with open(EVOLUTION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def bump(data):
    # 进化版本 +0.0.1（兼容任意位数版本号）
    parts = str(data["evolution_version"]).split(".")
    if not parts or not all(p.isdigit() for p in parts):
        raise ValueError(f"非法进化版本号: {data['evolution_version']}")
    parts[-1] = str(int(parts[-1]) + 1)
    data["evolution_version"] = ".".join(parts)
    data["last_updated"] = date.today().isoformat()


def _top(counter, last_used=None):
    """取最高频项；平局时按最近使用时间决胜（R3）。"""
    if not counter:
        return None
    hi = max(counter.values())
    tied = [k for k, v in counter.items() if v == hi]
    if len(tied) == 1:
        return tied[0]
    if last_used:
        tied.sort(key=lambda k: last_used.get(k, ""), reverse=True)
    return tied[0]


def _last_used_map(data):
    """从 experience_log 反推每个取值的最近使用日期。"""
    m = {}
    for e in data.get("experience_log", []):
        ts = e.get("timestamp", "")
        for field in ("type", "platform", "motion", "lighting", "viral_lever", "viral_levers"):
            v = e.get(field)
            if isinstance(v, list):
                for x in v:
                    m[x] = max(m.get(x, ""), ts)
            elif v:
                m[v] = max(m.get(v, ""), ts)
    return m


def record(data, stype=None, platform=None, motion=None, lighting=None, viral_lever=None, note=""):
    s = data.setdefault("usage_stats", {})
    p = data.setdefault("user_preferences", {})
    s.setdefault("by_type", {}); s.setdefault("by_platform", {})
    s.setdefault("by_viral_lever", {})
    s["total_generations"] = s.get("total_generations", 0) + 1

    today = date.today().isoformat()
    log_item = {"timestamp": today, "type": "使用记录"}
    for key, val in (("type", stype), ("platform", platform), ("motion", motion),
                     ("lighting", lighting), ("viral_lever", viral_lever)):
        if not val:
            continue
        bucket = "by_" + ("viral_lever" if key == "viral_lever" else key)
        s.setdefault(bucket, {})[val] = s[bucket].get(val, 0) + 1
        log_item[key] = val
    if note:
        log_item["note"] = note
    data.setdefault("experience_log", []).append(log_item)

    # 反推最近使用时间，用于平局决胜
    last = _last_used_map(data)
    if s["by_type"]:
        p["most_used_type"] = _top(s["by_type"], last)
    if s["by_platform"]:
        p["most_used_platform"] = _top(s["by_platform"], last)
    if s.get("by_motion"):
        p["most_used_motion"] = _top(s["by_motion"], last)
    if s.get("by_lighting"):
        p["most_used_lighting"] = _top(s["by_lighting"], last)
    if s["by_viral_lever"]:
        p["most_used_viral_levers"] = _top(s["by_viral_lever"], last)

    bump(data)
    save(data)
    print("✅ 已记录使用经验，进化版本 ->", data["evolution_version"])


def feedback(data, text, optimization, rejected=False):
    data.setdefault("experience_log", []).append({
        "timestamp": date.today().isoformat(),
        "type": "用户修改反馈",
        "original": text,
        "optimization": optimization,
        "applied": not rejected,
    })
    if rejected:
        # R1: 失败优化入 rejected_optimizations，防止重复踩坑
        data.setdefault("rejected_optimizations", []).append({
            "timestamp": date.today().isoformat(),
            "optimization": optimization,
            "reason": text,
        })
    bump(data)
    save(data)
    print(("✅ 已标记失败优化并归档：" if rejected else "✅ 已记录反馈优化：") + optimization)


def rollback(data):
    """R1: 撤销最近一条已应用的反馈优化，转入 rejected，实现回滚闭环。"""
    log = data.get("experience_log", [])
    idx = next((i for i in range(len(log)-1, -1, -1)
                if log[i].get("type") == "用户修改反馈" and log[i].get("applied")), None)
    if idx is None:
        print("⚠ 没有可回滚的已应用优化")
        return
    item = log[idx]
    item["applied"] = False
    item["rolled_back_at"] = date.today().isoformat()
    data.setdefault("rejected_optimizations", []).append({
        "timestamp": date.today().isoformat(),
        "optimization": item.get("optimization"),
        "reason": "自动回滚（效果下降）",
    })
    bump(data)
    save(data)
    print("✅ 已回滚优化：", item.get("optimization"))


def report(data):
    s = data["usage_stats"]
    print(f"🎯 进化报告 | Skill v{data['skill_version']} | 进化 v{data['evolution_version']}")
    print(f"累计生成：{s['total_generations']} 次")
    for label, key in (("类型", "by_type"), ("平台", "by_platform"),
                       ("运镜", "by_motion"), ("光影", "by_lighting"),
                       ("爆款杠杆", "by_viral_lever")):
        if s.get(key):
            top = _top(s[key], _last_used_map(data))
            print(f"最常用{label}：{top}（{s[key][top]} 次）")
    print(f"经验日志：{len(data['experience_log'])} 条 | "
          f"已回滚/拒绝：{len(data.get('rejected_optimizations', []))} 条")


def stats(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("record")
    pr.add_argument("--type"); pr.add_argument("--platform"); pr.add_argument("--motion")
    pr.add_argument("--lighting"); pr.add_argument("--viral-lever"); pr.add_argument("--note", default="")
    pf = sub.add_parser("feedback")
    pf.add_argument("--text", required=True); pf.add_argument("--optimization", required=True)
    pf.add_argument("--rejected", action="store_true", help="标记为失败优化，写入 rejected_optimizations")
    sub.add_parser("rollback")
    sub.add_parser("report")
    sub.add_parser("stats")
    args = p.parse_args()
    data = load()
    if args.cmd == "record":
        record(data, args.type, args.platform, args.motion, args.lighting, args.viral_lever, args.note)
    elif args.cmd == "feedback":
        feedback(data, args.text, args.optimization, args.rejected)
    elif args.cmd == "rollback":
        rollback(data)
    elif args.cmd == "report":
        report(data)
    elif args.cmd == "stats":
        stats(data)


if __name__ == "__main__":
    main()
