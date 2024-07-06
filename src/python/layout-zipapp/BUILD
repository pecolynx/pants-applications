poetry_requirements(
    name="poetry",
    resolve="layout_zipapp",
)

python_sources(
    name="src",
    resolve="layout_zipapp",
    interpreter_constraints=["CPython>=3.11"],
    sources=["layout_zipapp/**/*.py"],
    dependencies=[
        ":poetry",
    ],
)

python_tests(
    name="tests",
    resolve="layout_zipapp",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[],
    skip_mypy=True,
)

pex_binary(
    name="layout_zipapp",
    resolve="layout_zipapp",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="layout_zipapp/main.py",
    dependencies=[
        ":src",
        ":poetry",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="layout_zipapp",
)
