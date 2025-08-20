import os
import google.generativeai as genai
from utils.constants import ROUTES, CITIES

def summarize_rule_based(route_daily):
    """Fallback summary logic if Gemini API not available."""
    top_routes = route_daily.groupby('route')['interest'].mean().sort_values(ascending=False).head(3)
    summary = "Rule-based summary:\n"
    for r, val in top_routes.items():
        summary += f"- {r}: Avg interest {val:.1f}\n"
    return summary

def summarize_with_ai(route_daily):
    """AI summary using Gemini API, fallback to rule-based if error."""
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        return summarize_rule_based(route_daily)

    try:
        genai.configure(api_key=gemini_key)
        small = route_daily.copy()
        small['date'] = small['date'].astype(str)
        csv_sample = small.to_csv(index=False)

        prompt = (
            "You are a travel demand analyst. Given the CSV of route, date, and search interest, "
            "produce a concise bullet summary with: (1) top 3 routes by average interest, "
            "(2) any clear peaks with dates, (3) notable week-over-week or month-over-month changes, "
            "(4) suggested actions for hostel marketing in Australia (2 bullets)."
        )
        model = genai.GenerativeModel("gemini-2.5-flash")
        resp = model.generate_content(prompt + "\n\nCSV:\n" + csv_sample[:12000])
        return resp.text
    except Exception:
        return summarize_rule_based(route_daily)
