poetry_requirements(
    name="poetry",
    resolve="lib_redis",
)

python_sources(
    name="src",
    resolve="lib_redis",
    sources=["lib_redis/**/*.py"],
)

# redis_list_consumer
poetry_requirements(
    name="redis_list_consumer_poetry",
    resolve="redis_list_consumer",
)
python_sources(
    name="redis_list_consumer_src",
    resolve="redis_list_consumer",
    sources=["lib_redis/**/*.py"],
)

python_tests(
    name="tests",
    resolve="pytest",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)