from dagster._utils.warnings import deprecation_warning

from dagster_embedded_elt.dlt.asset_decorator import build_dlt_asset_specs, dlt_assets
from dagster_embedded_elt.dlt.resource import DagsterDltResource
from dagster_embedded_elt.dlt.translator import DagsterDltTranslator

deprecation_warning(
    "The `dagster-embedded-elt` library",
    "0.26",
    additional_warn_text="Use `dagster-dlt` instead.",
)

__all__ = ["DagsterDltResource", "DagsterDltTranslator", "build_dlt_asset_specs", "dlt_assets"]
