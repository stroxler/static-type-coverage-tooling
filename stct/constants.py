from pathlib import Path



PROJECT_ROOT = Path(__file__).parent.parent
VENDORED_PROJECTS_ROOT = PROJECT_ROOT / "vendored_example_projects"
VENDORED_PROJECTS = [
    VENDORED_PROJECTS_ROOT / name
    for name in ["anyio"]
    # Focus on just anyio, so that we can do more repetitions to
    # average out the random noise in hint-stripping results.
    #
    # for name in ["urllib3", "mypy", "anyio"]
]

STRIPPED_PROJECT_ROOT = PROJECT_ROOT / "stripped_examples"
