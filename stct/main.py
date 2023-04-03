import fire
from . import (
    constants,
    strip,
    infer,
    count_infer_output,
)




class Stct:
    """
    Explore static type coverage tools!
    """

    def strip(self) -> None:
        """
        Create a directory with copies of the vendored projects whose types have
        been stripped.
        """
        strip.strip_types(
            projects=constants.VENDORED_PROJECTS,
            percentages=[0.2, 0.4, 0.6, 0.8],
            stripped_project_root=constants.STRIPPED_PROJECT_ROOT,
        )

    def infer(self) -> None:
        infer.run_pyre_infer_on_stripped_projects(
            stripped_project_root=constants.STRIPPED_PROJECT_ROOT,
        )

    def count_infer_output(self) -> None:
        count_infer_output.count_infer_output_on_stripped_projects(
            stripped_project_root=constants.STRIPPED_PROJECT_ROOT,
        )


if __name__ == "__main__":
    fire.Fire(Stct())
