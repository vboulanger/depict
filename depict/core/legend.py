"""Utilities to position legends without overlapping plotted data."""

from __future__ import annotations

from typing import Iterable, List, Sequence

import numpy as np
from bokeh.models import Range1d


def _as_array(values: Iterable) -> np.ndarray:
    arr = np.array(values)
    if arr.dtype.kind == "M":
        return arr.astype("datetime64[ns]")
    return arr


def _numeric_view(values: np.ndarray) -> np.ndarray:
    if values.dtype.kind == "M":
        return values.astype("datetime64[ns]").astype("int64")
    return values.astype(float)


def _compute_bounds(arrays: Sequence[Iterable]):
    flattened = np.concatenate([_as_array(a) for a in arrays])
    numeric = _numeric_view(flattened)
    arr_min = flattened.min()
    arr_max = flattened.max()
    span = arr_max - arr_min
    return {
        "raw_min": arr_min,
        "raw_max": arr_max,
        "numeric": numeric,
        "span": span,
        "is_datetime": flattened.dtype.kind == "M",
    }


def _padding(span, is_datetime: bool):
    if is_datetime:
        span_ns = int(span.astype("timedelta64[ns]").astype(int)) if span != 0 else 0
        span_ns = span_ns if span_ns else 1
        return np.timedelta64(int(span_ns * 0.1) or 1, "ns")
    span = float(span)
    span = span if span != 0 else 1.0
    return span * 0.1


def _choose_corner(x_numeric: np.ndarray, y_numeric: np.ndarray):
    x_mid = (x_numeric.min() + x_numeric.max()) / 2
    y_mid = (y_numeric.min() + y_numeric.max()) / 2

    quadrants = {
        "top_left": (x_numeric < x_mid) & (y_numeric > y_mid),
        "top_right": (x_numeric >= x_mid) & (y_numeric > y_mid),
        "bottom_left": (x_numeric < x_mid) & (y_numeric <= y_mid),
        "bottom_right": (x_numeric >= x_mid) & (y_numeric <= y_mid),
    }
    counts = {name: int(mask.sum()) for name, mask in quadrants.items()}
    best_corner = min(counts, key=counts.get)
    return best_corner, counts[best_corner] == 0


def place_legend_without_overlap(fig, x_arrays: List[Iterable], y_arrays: List[Iterable],
                                 user_defined_x_range: bool, user_defined_y_range: bool):
    if not fig.legend:
        return

    x_bounds = _compute_bounds(x_arrays)
    y_bounds = _compute_bounds(y_arrays)

    corner, empty_corner = _choose_corner(x_bounds["numeric"], y_bounds["numeric"])

    for legend in fig.legend:
        legend.location = corner

    if empty_corner:
        return

    if not user_defined_x_range:
        x_pad = _padding(x_bounds["span"], x_bounds["is_datetime"])
        left = x_bounds["raw_min"]
        right = x_bounds["raw_max"]
        if corner.endswith("right"):
            right = right + x_pad
        else:
            left = left - x_pad
        fig.x_range = Range1d(left, right)

    if not user_defined_y_range:
        y_pad = _padding(y_bounds["span"], y_bounds["is_datetime"])
        bottom = y_bounds["raw_min"]
        top = y_bounds["raw_max"]
        if corner.startswith("top"):
            top = top + y_pad
        else:
            bottom = bottom - y_pad
        fig.y_range = Range1d(bottom, top)
