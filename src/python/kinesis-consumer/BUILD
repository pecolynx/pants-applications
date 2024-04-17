poetry_requirements(
    name="poetry",
    resolve="kinesis_consumer",
)

python_sources(
    name="src",
    resolve="kinesis_consumer",
    interpreter_constraints=["CPython>=3.11"],
    sources=["kinesis_consumer/**/*.py"],
    dependencies=[
        ":poetry",
        "src/python/lib-logging:kinesis_consumer_src",
    ],
)

python_source(
    name="set_property",
    source="set_properties.py",
)


python_tests(
    name="tests",
    resolve="kinesis_consumer",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[
        ":src",
    ],
    skip_mypy=True,
)

pex_binary(
    name="kinesis_consumer",
    resolve="kinesis_consumer",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="kinesis_consumer/main.py",
    dependencies=[
        ":src",
        ":poetry",
    ],
)

files(
    name="docker_files",
    sources=[
        "app.properties",
        "logback.xml",
        "requirements.txt",
        "run.sh",
        "set_properties.py",
    ],
)

docker_image(
    name="docker",
    image_tags=["{build_args.GIT_COMMIT}"],
    repository="kinesis_consumer",
    dependencies=[
        ":docker_files",
    ]
)
