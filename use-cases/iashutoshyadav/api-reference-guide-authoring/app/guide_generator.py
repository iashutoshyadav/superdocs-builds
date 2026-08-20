"""Mode 2: a described API/feature set -> a numbered getting-started guide, exported as a styled document.

Follows the SuperDocs skill's own documented pattern for from-scratch drafting: initialize an empty session
(upload an empty HTML shell), then send the full draft request via chat in one turn - SuperDocs writes the
document natively with real formatting, rather than us generating HTML ourselves and uploading it (which
the skill explicitly warns against: it wastes tokens and skips SuperDocs' own formatting layer entirely).
"""

from __future__ import annotations

from app.superdocs_client import SuperDocsClient

_EMPTY_DOCUMENT = b"<html><body></body></html>"


def generate_getting_started_guide(client: SuperDocsClient, feature_description: str, session_id: str) -> str:
    client.upload_document("guide.html", _EMPTY_DOCUMENT, session_id=session_id)
    message = (
        "Draft a numbered getting-started guide for the following API or feature: "
        f"{feature_description}\n\n"
        "Use clear, sequential numbered steps a brand-new user can follow from zero to their first "
        "successful call. Start with prerequisites, end with a working example. Where a specific detail "
        "(SDK package name, API key value, endpoint URL, etc.) isn't given above, write "
        "'Please fill: [what's missing]' rather than inventing a plausible-looking value. Do not add a "
        "team name, copyright line, version number, or publication date - none of that was given, and "
        "inventing it would be exactly the kind of unrequested fabrication this guide should avoid. "
        "The working example must be a single, self-contained, runnable snippet: every function you "
        "define must actually be called, and every variable you reference (e.g. a token or response you "
        "use later) must be assigned from that call first - never reference a variable that was never "
        "declared. If a detail you're using was given above, incorporate it exactly rather than "
        "replacing it with a placeholder."
    )
    client.chat(message, session_id=session_id)
    return client.export_document(session_id, format="markdown")
