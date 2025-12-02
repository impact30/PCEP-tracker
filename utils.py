from datetime import date

def render_progress_bar(done, total):
    ratio = done / total if total else 0
    filled = int(ratio * 30)
    bar = "#" * filled + "-" * (30 - filled)
    return f"[{bar}] {done}/{total} ({ratio*100:.1f}%)"

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
