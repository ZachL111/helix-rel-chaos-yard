"""Executable checks for the helix-rel-chaos-yard casebook."""

from __future__ import annotations

from collections import Counter

from . import helix_rel_chaos_yard_segment_00
from . import helix_rel_chaos_yard_segment_01
from . import helix_rel_chaos_yard_segment_02
from . import helix_rel_chaos_yard_segment_03
from . import helix_rel_chaos_yard_segment_04
from . import helix_rel_chaos_yard_segment_05
from . import helix_rel_chaos_yard_segment_06
from . import helix_rel_chaos_yard_segment_07
from . import helix_rel_chaos_yard_segment_08
from . import helix_rel_chaos_yard_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from helix_rel_chaos_yard_segment_00.iter_helix_rel_chaos_yard_00()
    yield from helix_rel_chaos_yard_segment_01.iter_helix_rel_chaos_yard_01()
    yield from helix_rel_chaos_yard_segment_02.iter_helix_rel_chaos_yard_02()
    yield from helix_rel_chaos_yard_segment_03.iter_helix_rel_chaos_yard_03()
    yield from helix_rel_chaos_yard_segment_04.iter_helix_rel_chaos_yard_04()
    yield from helix_rel_chaos_yard_segment_05.iter_helix_rel_chaos_yard_05()
    yield from helix_rel_chaos_yard_segment_06.iter_helix_rel_chaos_yard_06()
    yield from helix_rel_chaos_yard_segment_07.iter_helix_rel_chaos_yard_07()
    yield from helix_rel_chaos_yard_segment_08.iter_helix_rel_chaos_yard_08()
    yield from helix_rel_chaos_yard_segment_09.iter_helix_rel_chaos_yard_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def helix_rel_chaos_yard_summary() -> dict:
    return assert_expected()
