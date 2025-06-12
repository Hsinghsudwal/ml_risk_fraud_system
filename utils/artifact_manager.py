import os
import io
import json
import pickle
import pandas as pd
from typing import Any, Dict, List, Optional, Union
from utils.logger import logger


class ArtifactManager:
    """Abstract base class for artifact storage."""

    def save(
        self, artifact: Any, subdir: str, name: str, pipeline_id: Optional[str] = None
    ) -> str:
        """Save an artifact to the store."""
        raise NotImplementedError("Subclasses must implement save()")

    def load(self, subdir: str, name: str) -> Any:
        """Load an artifact from the store."""
        raise NotImplementedError("Subclasses must implement load()")

    def exists(self, subdir: str, name: str) -> bool:
        """Check if an artifact exists in the store."""
        raise NotImplementedError("Subclasses must implement exists()")

    def list(self, subdir: str) -> List[str]:
        """List artifacts in a subdirectory."""
        raise NotImplementedError("Subclasses must implement list()")

    def save_binary(
        self, artifact, subdir: str, name: str, pipeline_id: str = None
    ) -> str:
        """Wrapper to save binary artifacts (e.g., evaluation plots, pickles)."""
        raise NotImplementedError("Subclasses must implement save binary()")

    def get_base_path(self) -> str:
        """Return the base storage path (for info/logging/debug)."""
        pass

    def resolve_path(self, relative_path: str) -> str:
        pass
