# poetry_requirements(
#     name="poetry",
#     resolve="lib_logging",
# )

python_sources(
    name="src",
    resolve="lib_logging",
    sources=["lib_logging/**/*.py"],
)


python_tests(name="tests", resolve="lib_logging", sources=["tests/**/*_test.py"], dependencies=[])

# kinesis_consumer
# poetry_requirements(
#     name="kinesis_consumer_poetry",
#     resolve="kinesis_consumer",
# )
python_sources(
    name="kinesis_consumer_src",
    resolve="kinesis_consumer",
    sources=["lib_logging/**/*.py"],
)

# kinesis_producer
# poetry_requirements(
#     name="kinesis_producer_poetry",
#     resolve="kinesis_producer",
# )
python_sources(
    name="kinesis_producer_src",
    resolve="kinesis_producer",
    sources=["lib_logging/**/*.py"],
)

# multiprocessing_app
# poetry_requirements(
#     name="multiprocessing_app_poetry",
#     resolve="multiprocessing_app",
# )
python_sources(
    name="multiprocessing_app_src",
    resolve="multiprocessing_app",
    sources=["lib_logging/**/*.py"],
)
