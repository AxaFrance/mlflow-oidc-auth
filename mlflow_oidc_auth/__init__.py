import os

version = os.environ.get("MLFLOW_OIDC_AUTH_VERSION", "0.0.1")

__version__ = version
