poetry_requirements(
    name="poetry",
    resolve="lib_logging",
)

python_sources(
    name="src",
    resolve="lib_logging",
    sources=["lib_logging/**/*.py"],
)

# kinesis_consumer
poetry_requirements(
    name="kinesis_consumer_poetry",
    resolve="kinesis_consumer",
)
python_sources(
    name="kinesis_consumer_src",
    resolve="kinesis_consumer",
    sources=["lib_logging/**/*.py"],
)


python_tests(
    name="tests",
    resolve="pytest",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)
