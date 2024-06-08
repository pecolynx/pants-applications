poetry_requirements(
    name="poetry",
    resolve="redis_client",
)

python_sources(
    name="src",
    resolve="redis_client",
    interpreter_constraints=["CPython>=3.11"],
    sources=["redis_client/**/*.py"],
    dependencies=[
        "src/python/lib-redis:redis_client_poetry#redis",
        # "src/python/lib-redis:redis_client_poetry#types-redis",
        # "src/python/lib-redis:redis_client_poetry#pydantic",
        "src/python/lib-redis:redis_client_src",
    ],
)

pex_binary(
    name="redis_client",
    resolve="redis_client",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="redis_client/main.py",
)

python_tests(
    name="tests",
    resolve="redis_client",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)
