# almoststable train

This template sets up an ML training job. Add a description of your model or
other useful information here.

## Running locally

Before anything else, create a virtual environment in the same directory as this
file. Then activate it and install the project in the virtual environment.

```shell
$ python -m venv .venv  # create virtualenv
$ source .venv/bin/active  # activate virtualenv
$ pip install .  # add project to virtualenv
```

Install [Docker](https://docker.com) or [PodMan](https://podman.io) to be able
to build and run containers locally. Get accustomed to using Docker/Podman
before using this project. We'll be using `docker` terminology here. Build and
tag a local Docker image.

```shell
$ docker build -t almoststable-train .
```

[Mlflow](https://mlflow.org) is used for model tracking. An `MLProject` file
configures tracking model training using locally built containers. Read it for
more hints. Have the Mlflow docs next to you, too.

Next, configure your training job. The sample training job takes in two
parameters: `alpha` and `L1 ratio`. For example, we track run a model training
session:

```shell
$ mlflow run . -P alpha=0.5
```

Have a look at the `./mlruns` folder.

## EduML Integration

Follow these steps to run the training job on the EduML cluster.

1. ensure your project builds and runs using Mlflow locally
1. confirm that there's a Docker image published in the GitHub Container
Registry for your project. Using the default config, the image location is:
`https://github.com/LauraDiosan-CS/almoststable-train/pkgs/container/almoststable-train`
1. confirm that `helm/almoststable-train/values.yaml` matches your GitHub
repository settings
1. use the specific tag name marked as latest (e.g. `main-f488fdb`) in your
`helm/almoststable-train/values.yaml`
1. commit and push the `values.yaml` file
1. make sure that the GitHub repo is registered with the EduML team:
   * wait for confirmation that the repository is registered
1. inspect the [training job logs](https://grafana.k8s.cs.ubbcluj.ro/d/fe3q1y9rzuakgf/logs?from=now-1h&to=now&timezone=browser)
1. check out [Mlflow](https://mlflow.k8s.cs.ubbcluj.ro)

### Updating the Training Job

To deploy an updated training job spec, at least two conditions must be met:
- a new version of the Docker image was built and published on GHCR, _and_
- the new version is referenced in the `values.yaml` file.
