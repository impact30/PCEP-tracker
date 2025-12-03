from datetime import date

# ------------------------------------------------------
# Text summary progress bar
# ------------------------------------------------------
def render_progress_bar(done, total):
    ratio = done / total if total else 0
    filled = int(ratio * 30)
    bar = "#" * filled + "-" * (30 - filled)
    return f"[{bar}] {done}/{total} ({ratio*100:.1f}%)"


# ------------------------------------------------------
# Header progress bar (animated)
# ------------------------------------------------------
def render_expander_header_style(section_id, fill_percent):
    fill_color = "#ffd9b3"     # warm pastel
    empty_color = "#ffffff"    # white

    css = f"""
    <style>
    /* Find the expander whose body contains our marker */
    div[data-testid="stExpander"]:has(div[section-marker='{section_id}']) summary {{
        background: linear-gradient(
            to right,
            {fill_color} {fill_percent}%,
            {empty_color} {fill_percent}%
        );
        border: 1px solid #e0c4a8;
        border-radius: 6px;
        padding: 6px;

        /* Smooth animation */
        transition: background 0.4s ease-in-out, border-color 0.4s;
    }}
    </style>
    """
    return css


# ------------------------------------------------------
# Timeline helper
# ------------------------------------------------------
def calculate_timeline(start, end):
    today = date.today()
    total_days = (end - start).days
    passed = (today - start).days
    left = (end - today).days

    left = max(left, 0)
    passed = max(passed, 0)

    return (
        f"Days passed: {passed}\n"
        f"Days left: {left}\n"
        f"Total study window: {total_days} days"
    )
