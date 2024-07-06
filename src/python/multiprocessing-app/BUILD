poetry_requirements(
    name="poetry",
    resolve="multiprocessing_app",
)

python_sources(
    name="src",
    resolve="multiprocessing_app",
    interpreter_constraints=["CPython>=3.11"],
    sources=["multiprocessing_app/**/*.py"],
    dependencies=[
        ":poetry",
        "src/python/lib-logging:multiprocessing_app_src",
    ],
)

python_tests(
    name="tests",
    resolve="multiprocessing_app",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[],
    skip_mypy=True,
)

pex_binary(
    name="multiprocessing_app",
    resolve="multiprocessing_app",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="multiprocessing_app/main.py",
    dependencies=[
        ":src",
        ":poetry",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="multiprocessing_app",
    dependencies=[],
)
