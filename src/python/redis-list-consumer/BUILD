poetry_requirements(
    name="poetry",
    resolve="redis_list_consumer",
)

python_sources(
    name="src",
    resolve="redis_list_consumer",
    interpreter_constraints=["CPython>=3.11"],
    sources=["redis_list_consumer/**/*.py"],
    dependencies=[
        "src/python/lib-redis:redis_list_consumer_poetry#redis",
        "src/python/lib-redis:redis_list_consumer_src",
    ]
)

pex_binary(
    name="redis_list_consumer",
    resolve="redis_list_consumer",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="redis_list_consumer/main.py",
)

python_tests(
    name="tests",
    resolve="pytest",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)
