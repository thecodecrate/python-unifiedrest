import posixpath
from typing import Optional
from urllib.parse import urljoin, urlparse


def combine_urls_safely(base_url: Optional[str], relative_url: str) -> str:
    if not base_url:
        return relative_url

    parsed_base_url = urlparse(base_url)

    parsed_relative_url = urlparse(relative_url)

    base_parts: list[str] = []

    if parsed_base_url.scheme and parsed_base_url.netloc:
        base_parts += [f"{parsed_base_url.scheme}://"]

    if parsed_base_url.netloc:
        base_parts += [parsed_base_url.netloc.rstrip("/")]

    combined_base = "".join(base_parts)

    combined_path = posixpath.join(
        parsed_base_url.path.lstrip("/"),
        parsed_relative_url.path.lstrip("/"),
    )

    if parsed_base_url.query or parsed_relative_url.query:
        combined_path += f"?{parsed_relative_url.query}"

    combined_url = urljoin(combined_base, combined_path)

    assert_no_path_traversal(base_url, combined_url)

    return combined_url


def assert_no_path_traversal(base_url: str, combined_url: str) -> None:
    parsed_base = urlparse(base_url)

    parsed_combined = urlparse(combined_url)

    is_path_traversal = (
        parsed_base.netloc != parsed_combined.netloc
        or not parsed_combined.path.startswith(parsed_base.path)
    )

    if is_path_traversal:
        raise ValueError("URL navigates outside the base URL")
