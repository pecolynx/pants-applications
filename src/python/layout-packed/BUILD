poetry_requirements(
    name="poetry",
    resolve="layout_packed",
)

python_sources(
    name="src",
    resolve="layout_packed",
    interpreter_constraints=["CPython>=3.11"],
    sources=["layout_packed/**/*.py"],
    dependencies=[
        ":poetry",
    ],
)

python_tests(
    name="tests",
    resolve="layout_packed",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[],
    skip_mypy=True,
)

pex_binary(
    name="layout_packed",
    resolve="layout_packed",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="layout_packed/main.py",
    layout="packed",
    execution_mode="venv",
    dependencies=[
        ":src",
        ":poetry",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="layout_packed",
)
