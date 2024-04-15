poetry_requirements(
    name="poetry",
    resolve="redis_publisher",
)

python_sources(
    name="src",
    resolve="redis_publisher",
    interpreter_constraints=["CPython>=3.11"],
    sources=["redis_publisher/**/*.py"],
    dependencies=[
        "src/python/lib-redis:redis_publisher_poetry#redis",
        "src/python/lib-redis:redis_publisher_src",
    ]
)

pex_binary(
    name="redis_list_consumer",
    resolve="redis_publisher",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="redis_publisher/main.py",
)

python_tests(
    name="tests",
    resolve="redis_publisher",
    interpreter_constraints=["CPython>=3.11"],
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)
python_test_utils(
    name="test_utils",
    sources=[
        "tests/conftest.py",
    ]
)
