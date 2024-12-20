from typing import Any

import mlflow.sklearn
from mlflow.models import ModelSignature

from almoststable_train.mlflow.wrappers._base import mlflow_decorator


class tf_model(mlflow_decorator):
    @classmethod
    def _unsafe_optional_import(cls) -> None:
        import mlflow.tensorflow

    def _log_model(self, model: Any, sig: ModelSignature) -> None:
        mlflow.tensorflow.log_model(
            model, self._model_path, **self._extra_log_model_args(sig)
        )

    @property
    def _model_path(self) -> str:
        return "tensorflow"


class keras_model(mlflow_decorator):
    @classmethod
    def _unsafe_optional_import(cls) -> None:
        import mlflow.keras

    def _log_model(self, model: Any, sig: ModelSignature) -> None:
        mlflow.keras.log_model(
            model, self._model_path, **self._extra_log_model_args(sig)
        )

    @property
    def _model_path(self) -> str:
        return "keras"
