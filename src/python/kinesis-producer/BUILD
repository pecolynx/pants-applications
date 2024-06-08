poetry_requirements(
    name="poetry",
    resolve="kinesis_producer",
)

python_sources(
    name="src",
    resolve="kinesis_producer",
    interpreter_constraints=["CPython>=3.11"],
    sources=["kinesis_producer/**/*.py", "kinesis_producer/main.py"],
    dependencies=[
        ":poetry",
        "src/python/lib-logging:kinesis_producer_src",
    ],
)

python_tests(
    name="tests",
    resolve="kinesis_producer",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[
        ":src",
    ],
    skip_mypy=True,
)

pex_binary(
    name="kinesis_producer",
    resolve="kinesis_producer",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="kinesis_producer/main.py",
    dependencies=[
        ":src",
        ":poetry",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="kinesis_producer",
    dependencies=[
        ":docker_files",
    ]
)
