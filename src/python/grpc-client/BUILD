poetry_requirements(
    name="poetry",
    resolve="grpc_client",
)

python_sources(
    name="src",
    resolve="grpc_client",
    sources=["grpc_client/**/*.py"],
)

pex_binary(
    name="grpc_client",
    resolve="grpc_client",
    interpreter_constraints=["CPython>=3.11"],
    entry_point="grpc_client/main.py",
)

python_tests(
    name="tests",
    resolve="pytest",
    sources=["tests/**/*_test.py"],
    dependencies=[
    ]
)
