from typing import Optional, Dict, Any
import subprocess
from collections import Counter
from pathlib import Path
import json



def run_pyre(project_directory: Path) -> Optional[Dict[str, Any]]:
    project_config = (project_directory / ".pyre_configuration")
    project_config.write_text(json.dumps({
        "source_directories": ["."],
    }))
    try:
        report = subprocess.check_output(
            ["pyre", "-n", "report"],
            cwd=project_directory,
            stderr=subprocess.DEVNULL,
        )
        report_json = json.loads(report)
        return report_json
    except Exception:
        return None
    finally:
        try:
            project_config.unlink()
        except Exception:
            pass


def report_function_level_coverage(project_directory: Path) -> None:
    project_report = run_pyre(project_directory)
    if project_report is None:
        print(f"Failed to report on {project_directory}")
    else:
        annotation_kinds = [
            function["annotation_kind"]
            for module_report in project_report
            for function in module_report["function_annotations"]
        ]
        annotation_kind_counts = Counter(annotation_kinds)
        print(f"Stats for {project_directory}")
        print(annotation_kind_counts)



for project_directory in Path(".").iterdir():
    if project_directory.is_dir():
        report_function_level_coverage(project_directory)
    else:
        pass
